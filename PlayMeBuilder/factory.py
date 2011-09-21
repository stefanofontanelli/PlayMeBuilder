
from collections import deque
from jinja2 import Environment
from jinja2 import PackageLoader
from jinja2 import Template
import os
import os.path
import shutil


class SourceFactory(object):

    def __init__(self, api):
        self._api = api

    def build(self, language, dst):

        src = os.path.join(__import__(__package__).__path__[0],
                           'templates',
                           language)
        dst = os.path.join(dst, self._api.name, language)

        # Copy dir and files of the selected template skeleton to 'dst'.
        for root, dirs, files in os.walk(src):

            base_dir = root.replace(src, '')
            if base_dir.startswith('/') or base_dir.startswith('\\'):
                base_dir = base_dir[1:]

            # Create skeleton dirs in 'dst'.
            for dir_ in dirs:
                # Replace template placeholders which could be in the dir name.
                os.makedirs(Template(os.path.join(dst,
                                                  base_dir,
                                                  dir_)).render(api=self._api))

            for name in files:
                src_file = open(os.path.join(root, name), 'r')
                template = Template(src_file.read()).render(api=self._api)
                dst_file = Template(os.path.join(dst,
                                                 base_dir,
                                                 name)).render(api=self._api)
                dst_file = open(dst_file.replace('.tpl', '.py'), 'w')
                dst_file.write(template)
                src_file.close()
                dst_file.close()
