"""Test Boolean class"""
import pytest

import simpleparam as param


class TestBoolean(object):
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
                self.const_int = param.Number(value=666, constant=False)

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
                self.const_int = param.Number(value=666, constant=True)

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
                self.param_int = param.Number(value=666)

        config = Config()
        export_dict = config.export_as_json()
        assert len(export_dict) == 1

    @staticmethod
    def test_variables_not_exportable():
        """Test ParameterStore - correct initilization of constant"""

        class Config(param.ParameterStore):
            def __init__(self):
                param.ParameterStore.__init__(self)
                self.param_int = param.Number(value=666, saveable=False)

        config = Config()
        export_dict = config.export_as_json()
        assert len(export_dict) == 0
