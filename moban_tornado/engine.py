import tornado.template
import moban.utils as utils
import os.path as path


class EngineTornado(object):

    def __init__(self, template_dirs, extensions=None):
        self.template_dirs = template_dirs

    def get_template(self, template_file):
        actual_file = utils.get_template_path(
            self.template_dirs, template_file
        )
        template_loader = tornado.template.Loader(path.dirname(actual_file))
        template = template_loader.load(template_file)
        return template

    def get_template_from_string(self, string):
        return tornado.template.Template(string)

    def apply_template(self, template, data, _):
        return template.generate(**data).decode("utf-8")
