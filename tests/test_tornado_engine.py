import os

from nose.tools import eq_
from moban.plugins import ENGINES, BaseEngine
from moban_tornado.engine import EngineTornado


def test_mako_engine_type():
    engine = ENGINES.get_engine("tornado", [], "")
    assert engine.engine_cls == EngineTornado
    pass


def test_mako_templates():
    output = "test.txt"
    path = os.path.join("tests", "fixtures", "tornado_tests")
    engine = BaseEngine([path], path, EngineTornado)
    engine.render_to_file("templates_tests.tornado", "templates_tests.yml", output)
    with open(output, "r") as output_file:
        expected_path = os.path.join("tests", "fixtures", "tornado_tests",
                                     "expected_output.txt")
        with open(expected_path) as expected_file:
            expected = expected_file.read()
            content = output_file.read()
            eq_(content, expected)
    os.unlink(output)


def test_mako_string_template():
    string_template = "hello {{ data }}!"
    output = "test.txt"
    path = os.path.join("tests", "fixtures", "tornado_tests")
    engine = BaseEngine([path], path, EngineTornado)
    engine.render_string_to_file(string_template, "templates_tests.yml", output)
    with open(output, "r") as output_file:
        expected = "hello world!"
        content = output_file.read()
        eq_(content, expected)
    os.unlink(output)
