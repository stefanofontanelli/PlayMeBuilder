#!/usr/bin/env python

from distutils.core import setup

setup(name='PlayMeBuilder',
      version='0.1',
      description="A Python library to build Play.me API clients.",
      long_description="""\
PlayMe builds Play.me API clients for multiple programming languages and platform.
The official API can be found at http://lab.playme.com.
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Play.me API',
      author='Stefano Fontanelli',
      author_email='s.fontanelli@gmail.com',
      url='http://github.com/stefanofontanelli/playme/builder',
      license='GPLv3',
      packages=['PlayMeBuilder'],
      requires=['jinja2', 'MarkupSage'],
      scripts=['scripts/playme-builder'],
      package_data={'PlayMeBuilder': ['data/api.xml',
                                      'templates/python/{{api.name}}Client/setup.cfg',
                                      'templates/python/{{api.name}}Client/setup.tpl',
                                      'templates/python/{{api.name}}Client/{{api.name.lower()}}client/__init__.tpl',
                                      'templates/python/{{api.name}}Client/{{api.name.lower()}}client/client.tpl']},
      )
