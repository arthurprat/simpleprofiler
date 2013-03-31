Simple Profiler
===============

A simple profiler that adds a panel to your django-debug-toolbar.
Note that there is an undocumented profiler panel provided with django-debug-toolbar :
just add `'debug_toolbar.panels.profiling.ProfilingDebugPanel'` to your `DEBUG_TOOLBAR_PANELS` setting.
It also uses Python's cProfile, but I didn't like the layout so I made that one, which just puts
ncalls, totaltime, inlinetime, etc in one big table.

How-to
-----

Put `simpleprofiler.py` somewhere in your Django project.

Add `somewhere.simpleprofiler.SimpleProfilerPanel` to your `DEBUG_TOOLBAR_PANELS` setting (if it doesn't exist yet, create it).

Put `simpleprofiler.html` in your `templates` folder.

Notes
-----

In the template file I use the [sorttable.js](http://www.kryogenix.org/code/browser/sorttable/) javascript so you can sort results by total time, call count etc.
It should work without that library but you won't be able to sort the table.

Python 2.7+ is required.
Used with Django 1.5 and django-debug-toolbar 0.9.4.
