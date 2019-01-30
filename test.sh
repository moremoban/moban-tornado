pip freeze
nosetests --with-coverage --cover-package moban_mako --cover-package tests tests  docs/source moban_mako && flake8 . --exclude=.moban.d,docs --builtins=unicode,xrange,long
