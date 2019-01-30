import os

from nose.tools import eq_
from moban.plugins import ENGINES, BaseEngine
from moban_mako.engine import EngineMako


def test_mako_engine_type():
    engine = ENGINES.get_engine("mako", [], "")
    assert engine.engine_cls == EngineMako
    pass


def test_mako_templates():
    output = "test.txt"
    path = os.path.join("tests", "fixtures", "mako_tests")
    engine = BaseEngine([path], path, EngineMako)
    engine.render_to_file("templates_tests.mako", "templates_tests.yml", output)
    with open(output, "r") as output_file:
        expected_path = os.path.join("tests", "fixtures", "mako_tests",
                                     "expected_output.txt")
        with open(expected_path) as expected_file:
            expected = expected_file.read()
            content = output_file.read()
            eq_(content, expected)
    os.unlink(output)


def test_mako_string_template():
    string_template = "hello ${data}!"
    output = "test.txt"
    path = os.path.join("tests", "fixtures", "mako_tests")
    engine = BaseEngine([path], path, EngineMako)
    engine.render_string_to_file(string_template, "templates_tests.yml", output)
    with open(output, "r") as output_file:
        expected = "hello world!"
        content = output_file.read()
        eq_(content, expected)
    os.unlink(output)
