pip freeze
nosetests --with-coverage --cover-package moban_tornado --cover-package tests tests  docs/source moban_tornado && flake8 . --exclude=.moban.d,docs --builtins=unicode,xrange,long
