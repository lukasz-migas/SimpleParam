"""Test ParamStore class"""
import pytest

import simpleparam as param

ip_regex = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"


class TestParamStore(object):
    """Test Boolean class"""

    @staticmethod
    def test_creation_good():
        """Test ParameterStore - correct initilization"""

        class Config(param.ParameterStore):
            def __init__(self):
                param.ParameterStore.__init__(self)
                self.param_int = param.Integer(value=42)

        config = Config()
        assert config.param_int.value == 42

    @staticmethod
    def test_variable_not_constant():
        """Test ParameterStore - correct initilization of constant"""

        class Config(param.ParameterStore):
            def __init__(self):
                param.ParameterStore.__init__(self)
                self.const_int = param.Integer(value=666, constant=False)

        config = Config()
        assert config.const_int.value == 666
        value = 696
        config.const_int = value
        assert config.const_int.value == value

    @staticmethod
    def test_variable_constant():
        """Test ParameterStore - correct initilization of constant"""

        class Config(param.ParameterStore):
            def __init__(self):
                param.ParameterStore.__init__(self)
                self.const_int = param.Integer(value=666, constant=True)

        config = Config()
        assert config.const_int.value == 666
        assert config.const_int.constant

        with pytest.raises(ValueError) as __:
            config.const_int = 696

        assert config.const_int.value == 666

    @staticmethod
    def test_variables_exportable():
        """Test ParameterStore - correct initilization of constant"""

        class Config(param.ParameterStore):
            def __init__(self):
                param.ParameterStore.__init__(self)
                self.param_int = param.Integer(value=666)
                self.param_num = param.Number(value=42.0)
                self.param_color = param.Color(value="#FFF000")
                self.param_choice = param.Choice(value="boo", choices=["boo", "baa"])
                self.param_str = param.String("hello")
                self.param_regex = param.String(value="127.0.0.1", regex=ip_regex)
                self.param_bool = param.Boolean(False)
                self.param_option = param.Option(value=None, choices=[True, False])
                self.param_range = param.Range(value=[-100, 100], hardbounds=[-200, None])

                # non-param value which will not be taken into account during the count
                self.value = 123

        config = Config()
        export_dict = config.export_as_json()
        assert len(export_dict) == 9

    @staticmethod
    def test_variables_not_exportable():
        """Test ParameterStore - correct initilization of constant"""

        class Config(param.ParameterStore):
            def __init__(self):
                param.ParameterStore.__init__(self)
                self.param_int = param.Integer(value=666, saveable=False)

        config = Config()
        export_dict = config.export_as_json()
        assert not export_dict

    @staticmethod
    def test_str():
        """Test ParameterStore - correct initilization of constant"""

        class Config(param.ParameterStore):
            def __init__(self):
                param.ParameterStore.__init__(self)
                self.param_int = param.Integer(value=42)

        config = Config()
        assert str(config) == "<Config ParameterStore>"

    @staticmethod
    def test_repr():
        """Test ParameterStore - correct initilization of constant"""

        class Config(param.ParameterStore):
            def __init__(self):
                param.ParameterStore.__init__(self)
                self.param_int = param.Integer(value=42)

        config = Config()
        assert repr(config) == "ParameterStore(count=1)"
