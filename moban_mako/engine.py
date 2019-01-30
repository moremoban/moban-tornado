from mako.template import Template
from mako.lookup import TemplateLookup


class EngineMako(object):

    def __init__(self, template_dirs, extensions=None):
        self.template_dirs = template_dirs
        self.template_lookup = TemplateLookup(directories=template_dirs)

    def get_template(self, template_file):
        template = self.template_lookup.get_template(template_file)
        return template

    def get_template_from_string(self, string):
        return Template(string)

    def apply_template(self, template, data, _):
        return template.render(**data)
