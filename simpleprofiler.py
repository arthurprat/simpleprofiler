import sys
import cProfile
from cStringIO import StringIO
from debug_toolbar.panels import DebugPanel, render_to_string
from django.conf import settings

class SimpleProfilerPanel(DebugPanel):
    name = 'SimpleProfiler'
    has_content = True
    template = 'simpleprofiler.html'

    def nav_title(self):
        return 'Simple Profiler'

    def title(self):
        return 'Simple Profiler'

    def url(self):
        return ''

    def content(self):
        if hasattr(self, 'results'):
            context = self.context.copy()
            context.update({
                'results' : [{
                        'name' : x.code if isinstance(x.code, str) else x.code.co_name,
                        'filename' : None if isinstance(x.code, str) else x.code.co_filename,
                        'line' : None if isinstance(x.code, str) else x.code.co_firstlineno,
                        'callcount' : x.callcount,
                        'inlinetime' : x.inlinetime,
                        'reccallcount' : x.reccallcount,
                        'totaltime' : x.totaltime,
                        'avgtime' : x.totaltime / x.callcount
                    } for x in self.results]
                })
        return render_to_string(self.template, context)

    def process_view(self, request, callback, callback_args, callback_kwargs):
        if settings.DEBUG:
            self.profiler = cProfile.Profile()
            args = (request,) + callback_args
            return self.profiler.runcall(callback, *args, **callback_kwargs)

    def process_response(self, request, response):
        if settings.DEBUG:
            self.profiler.create_stats()
            self.results = self.profiler.getstats()
        return response
