"""Test String class"""
import pytest

import simpleparam as param


class TestString(object):
    """Test String class"""

    @staticmethod
    def test_creation_good():
        """Test String - correct initilization"""
        value = "hello"
        str_a = param.String(value=value)
        assert str_a.value == value

        doc = "test doc"
        str_a = param.String(value=value, doc=doc)
        assert str_a.doc == doc
        assert str_a.value == value

        name = "string value"
        str_a = param.String(value=value, doc=doc, name=name)
        assert str_a.name == name

        value = None
        str_a = param.String(value=value, doc=doc, name=name, allow_None=True)
        assert str_a.value == value

        value = dict()
        str_a = param.String(value=value, doc=doc, name=name, allow_any=True)
        assert str_a.value == str(value)

        value = list()
        str_a = param.String(value=value, doc=doc, name=name, allow_any=True)
        assert str_a.value == str(value)

        value = 123
        str_a = param.String(value=value, doc=doc, name=name, allow_any=True)
        assert str_a.value == str(value)

        value = "hello"
        str_a = param.String(value=value, saveable=True)
        assert str_a.value == value
        assert str_a.saveable

        assert str_a.kind == "String"

    @staticmethod
    def test_creation_bad():
        """Test String - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = 42
            __ = param.String(value=value)

        with pytest.raises(ValueError) as __:
            value = dict()
            __ = param.String(value=value)

        with pytest.raises(ValueError) as __:
            value = list()
            __ = param.String(value=value)

        with pytest.raises(ValueError) as __:
            value = False
            __ = param.String(value=value)

        with pytest.raises(ValueError) as __:
            value = None
            __ = param.String(value=value, allow_None=False)
