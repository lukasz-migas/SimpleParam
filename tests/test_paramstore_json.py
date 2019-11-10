"""Test ParamStore class"""
import json
import tempfile

import pytest

import simpleparam as param

ip_regex = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"


class Config(param.ParameterStore):
    def __init__(self):
        param.ParameterStore.__init__(self)
        self.param_int = param.Integer(value=666)
        self.param_num = param.Number(value=42.0)
        self.param_color = param.Color(value="#FFF000")
        self.param_choice = param.Choice(value="boo", choices=["boo", "baa"])
        self.param_str = param.String("hello", doc="Old doc")
        self.param_regex = param.String(value="127.0.0.1", regex=ip_regex)
        self.param_bool = param.Boolean(False)
        self.param_option = param.Option(value=None, choices=[True, False])
        self.param_range = param.Range(value=[-100, 100], hardbounds=[-200, None])
        self.param_list = param.List(value=[1, 2, 3], hardbounds=[0, 10])


class TestParamStore(object):
    """Test Boolean class"""

    @staticmethod
    def test_export_as_dict():
        """Test ParameterStore - correct initilization of constant"""

        config = Config()
        export_dict = config.export_as_dict()
        assert len(export_dict) == 10

        fd, path = tempfile.mkstemp(suffix="json")
        with open(path, "w") as f_ptr:
            json.dump(export_dict, f_ptr)

    @staticmethod
    def test_export_as_dict_and_load():
        config = Config()
        export_dict = config.export_as_dict()
        assert len(export_dict) == 10

        fd, path = tempfile.mkstemp(suffix="json")
        with open(path, "w") as f_ptr:
            json.dump(export_dict, f_ptr)

        with open(path, "r") as f_ptr:
            import_dict = json.load(f_ptr)

        assert export_dict == import_dict

    @staticmethod
    def test_export_as_dict_and_load_and_set():
        config = Config()
        export_dict = config.export_as_dict()
        assert len(export_dict) == 10

        fd, path = tempfile.mkstemp(suffix="json")
        with open(path, "w") as f_ptr:
            json.dump(export_dict, f_ptr)

        # change some values in dict
        config.param_int = 134
        config.param_bool = True
        config.param_str = "world"

        with open(path, "r") as f_ptr:
            import_dict = json.load(f_ptr)

        assert export_dict == import_dict

        config.load_from_dict(import_dict)

        assert config.param_int == 666
        assert config.param_bool == False  # noqa
        assert config.param_str == "hello"

    @staticmethod
    def test_export_as_dict_and_load_and_set_ignored():
        config = Config()
        export_dict = config.export_as_dict()
        assert len(export_dict) == 10

        fd, path = tempfile.mkstemp(suffix="json")
        with open(path, "w") as f_ptr:
            json.dump(export_dict, f_ptr)

        # change some values in dict
        config.param_int = 134
        config.param_bool = True
        config.param_str = "world"

        with open(path, "r") as f_ptr:
            import_dict = json.load(f_ptr)

        assert export_dict == import_dict

        config.load_from_dict(import_dict, ignored_attributes=["value"])

        assert config.param_int == 134
        assert config.param_bool == True  # noqa
        assert config.param_str == "world"

    @staticmethod
    def test_export_as_dict_and_load_and_set_allowed():
        config = Config()
        export_dict = config.export_as_dict()
        assert len(export_dict) == 10

        fd, path = tempfile.mkstemp(suffix="json")
        with open(path, "w") as f_ptr:
            json.dump(export_dict, f_ptr)

        # change some values in dict
        config.param_int = 134
        config.param_bool = True
        config.param_str = "world"
        config.param_str.doc = "New doc"

        with open(path, "r") as f_ptr:
            import_dict = json.load(f_ptr)

        assert export_dict == import_dict
        assert config.param_str.doc == "New doc"

        config.load_from_dict(import_dict, allowed_attributes=["value", "doc"])

        assert config.param_int == 666
        assert config.param_bool == False  # noqa
        assert config.param_str == "hello"
        assert config.param_str.doc == "Old doc"

    @staticmethod
    def test_export_as_dict_and_load_and_set_allowed_and_ignored():
        config = Config()

        with pytest.raises(ValueError) as __:
            config.load_from_dict(dict(), allowed_attributes=["value"], ignored_attributes=["doc"])
