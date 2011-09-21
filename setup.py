#!/usr/bin/env python

from distutils.core import setup

setup(name='PlayMeBuilder',
      version='0.1',
      description="A Python library to build Play.me API clients.",
      long_description="""\
PlayMe builds Play.me API clients for multiple programming languages and platform.
The official API can be found at http://lab.playme.com.
""",
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Operating System :: OS Independent', 
                   'Programming Language :: Python :: 2',
                   'Topic :: Software Development :: Code Generators'],
      keywords='Play.me API',
      author='Stefano Fontanelli',
      author_email='s.fontanelli@gmail.com',
      url='http://github.com/stefanofontanelli/PlayMeBuilder',
      license='GPL',
      packages=['PlayMeBuilder'],
      requires=['jinja2', 'MarkupSafe'],
      scripts=['scripts/playme-builder'],
      package_data={'PlayMeBuilder': ['data/api.xml',
                                      'templates/python/{{api.name}}Client/setup.cfg',
                                      'templates/python/{{api.name}}Client/setup.tpl',
                                      'templates/python/{{api.name}}Client/{{api.name.lower()}}client/__init__.tpl',
                                      'templates/python/{{api.name}}Client/{{api.name.lower()}}client/client.tpl']},
      )
