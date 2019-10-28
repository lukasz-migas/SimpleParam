"""Test String class"""
import pytest

import simpleparam as param

ip_regex = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"


class TestStringSetup(object):
    """Test String class"""

    @staticmethod
    def test_creation_good():
        """Test String - correct initilization"""
        value = "hello"
        str_a = param.String(value=value)
        assert str_a.value == value

    @staticmethod
    def test_creation_doc():
        """Test String - correct initilization"""
        value = "hello"
        doc = "I am a string"
        str_a = param.String(value=value, doc=doc)
        assert str_a.doc == doc

    @staticmethod
    def test_creation_name():
        """Test String - correct initilization"""
        value = "hello"
        name = "string value"
        str_a = param.String(value=value, name=name)
        assert str_a.name == name

    @staticmethod
    def test_allow_none():
        """Test String - correct initilization"""
        value = None
        str_a = param.String(value=value, allow_None=True)
        assert str_a.value == value

    @staticmethod
    def test_allow_any_dict():
        """Test String - correct initilization"""
        value = dict()
        str_a = param.String(value=value, allow_any=True)
        assert str_a.value == str(value)

    @staticmethod
    def test_allow_any_list():
        """Test String - correct initilization"""
        value = list()
        str_a = param.String(value=value, allow_any=True)
        assert str_a.value == str(value)

    @staticmethod
    def test_allow_any_int():
        """Test String - correct initilization"""
        value = 123
        str_a = param.String(value=value, allow_any=True)
        assert str_a.value == str(value)

    @staticmethod
    def test_saveable():
        """Test String - correct initilization"""
        value = "hello"
        str_a = param.String(value=value, saveable=True)
        assert str_a.value == value
        assert str_a.saveable

    @staticmethod
    def test_kind():
        """Test String - correct initilization"""
        value = "hello"
        str_a = param.String(value=value)
        assert str_a.kind == "String"

    @staticmethod
    def test_regex_correct():
        """Test String - correct initilization"""
        value = "127.0.0.1"
        str_a = param.String(value=value, regex=ip_regex)
        assert str_a.value == value

    @staticmethod
    def test_regex_allow_none():
        """Test String - correct initilization"""
        value = None
        str_a = param.String(value=value, regex=ip_regex, allow_None=True)
        assert str_a.value == value

    @staticmethod
    def test_badregex():
        """Test String - correct initilization"""
        with pytest.raises(ValueError) as __:
            value = "no.ip"
            str_a = param.String(value=value, regex=ip_regex)

    @staticmethod
    def test_notallow_any_int():
        """Test String - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = 42
            __ = param.String(value=value)

    @staticmethod
    def test_notallow_any_dict():
        """Test String - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = dict()
            __ = param.String(value=value)

    @staticmethod
    def test_notallow_any_list():
        """Test String - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = list()
            __ = param.String(value=value)

    @staticmethod
    def test_notallow_any_bool():
        """Test String - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = False
            __ = param.String(value=value)

    @staticmethod
    def test_notallow_none():
        """Test String - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = None
            __ = param.String(value=value, allow_None=False)


class TestStringOperations(object):
    """Test String class operations"""

    @staticmethod
    def test_add():
        value = "hello"
        str_a = param.String(value=value)
        assert str_a.value == value

        new_value = value + " world"
        str_a.value += " world"
        assert str_a.value == new_value

    @staticmethod
    def test_mul():
        value = "hello"
        str_a = param.String(value=value)
        assert str_a.value == value

        new_value = value * 3
        str_a.value *= 3
        assert str_a.value == new_value

    @staticmethod
    def test_contains():
        value = "hello"
        str_a = param.String(value=value)
        assert str_a.value == value
        assert "hel" in str_a.value

    @staticmethod
    def test_contains_basemethod():
        value = "hello"
        str_a = param.String(value=value)
        assert str_a.value == value
        assert str_a.__contains__("hel")

    @staticmethod
    def test_getitem():
        value = "hello"
        str_a = param.String(value=value)
        assert str_a.value[0] == "h"
        assert str_a.value[-1] == "o"

    @staticmethod
    def test_getitem_basemethod():
        value = "hello"
        str_a = param.String(value=value)
        assert str_a.__getitem__(0) == "h"
        assert str_a.__getitem__(-1) == "o"
