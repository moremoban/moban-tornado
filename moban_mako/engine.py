import moban.utils as utils
from mako.template import Template
import codecs


class EngineMako(object):

    def __init__(self, template_dirs, extensions=None):
        self.template_dirs = template_dirs

    def get_template(self, template_file):
        template_file_path = utils.get_template_path(
            self.template_dirs, template_file
        )

        with codecs.open(template_file_path, 'r', encoding='utf-8') as template:
            mako_template = Template(template)

        return mako_template

    def get_template_from_string(self, string):
        return Template(string)

    def apply_template(self, template, data, _):
        return template.render(data)
