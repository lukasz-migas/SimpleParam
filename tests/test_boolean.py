"""Test Boolean class"""
import pytest

import simpleparam as param


class TestBooleanSetup(object):
    """Test Boolean class creation"""

    @staticmethod
    def test_creation_bool_true():
        """Test Boolean - correct initilization"""
        value = True
        bool_a = param.Boolean(value=value)
        assert bool_a.value == value

    @staticmethod
    def test_creation_bool_false():
        """Test Boolean - correct initilization"""
        value = True
        bool_a = param.Boolean(value=value)
        assert bool_a.value == value

    @staticmethod
    def test_creation_int_0():
        """Test Boolean - correct initilization"""
        value = 0
        bool_a = param.Boolean(value=value)
        assert bool_a.value == value

    @staticmethod
    def test_creation_int_1():
        """Test Boolean - correct initilization"""
        value = 1
        bool_a = param.Boolean(value=value)
        assert bool_a.value == value

    @staticmethod
    def test_kind():
        """Test Boolean - correct initilization"""
        value = True
        bool_a = param.Boolean(value=value)
        assert bool_a.kind == "Boolean"

    @staticmethod
    def test_full_setup():
        """Test Boolean - correct initilization"""
        value = False
        doc = "I am a bool"
        constant = True

        bool_a = param.Boolean(value=value, doc=doc, constant=constant)
        assert bool_a.value == value
        assert bool_a.doc == doc
        assert bool_a.constant == constant

    @staticmethod
    def test_allow_none():
        """Test Boolean - correct initilization"""
        value = None
        bool_a = param.Boolean(value=value, allow_None=True)
        assert bool_a.value == value

    @staticmethod
    def test_allow_change():
        """Test Boolean - correct initilization"""
        value = None
        bool_a = param.Boolean(value=value, allow_None=True)
        assert bool_a.value == value
        value = False
        bool_a.value = value
        assert bool_a.value == value

    @staticmethod
    def test_creation_int():
        """Test Boolean - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = 42
            __ = param.Boolean(value=value)

    @staticmethod
    def test_creation_str():
        with pytest.raises(ValueError) as __:
            value = "true"
            __ = param.Boolean(value=value)

    @staticmethod
    def test_creation_dict():
        with pytest.raises(ValueError) as __:
            value = dict()
            __ = param.Boolean(value=value)

    @staticmethod
    def test_creation_list():
        with pytest.raises(ValueError) as __:
            value = list()
            __ = param.Boolean(value=value)

    @staticmethod
    def test_notallow_none():
        with pytest.raises(ValueError) as __:
            value = None
            __ = param.Boolean(value=value, allow_None=False)

    @staticmethod
    def test_notallow_none_int_0():
        with pytest.raises(ValueError) as __:
            value = 2
            __ = param.Boolean(value=value, allow_None=False)

    @staticmethod
    def test_notallow_none_not_bool():
        with pytest.raises(ValueError) as __:
            value = "true"
            __ = param.Boolean(value=value, allow_None=False)


class TestBooleanOperations(object):
    """Test Boolean class operations"""

    @staticmethod
    def test_add():
        """Test Boolean - correct initilization"""
        value = False
        bool_a = param.Boolean(value=value)
        assert bool_a.value == value
        bool_a.value += 1
        assert bool_a.value

    @staticmethod
    def test_sub():
        """Test Boolean - correct initilization"""
        value = True
        bool_a = param.Boolean(value=value)
        assert bool_a.value == value
        bool_a.value -= 1
        assert bool_a.value == False

    @staticmethod
    def test_div():
        """Test Boolean - correct initilization"""
        with pytest.raises(ValueError) as __:
            value = True
            bool_a = param.Boolean(value=value)
            bool_a.value /= 0.5

    @staticmethod
    def test_mul():
        """Test Boolean - correct initilization"""
        with pytest.raises(ValueError) as __:
            value = True
            bool_a = param.Boolean(value=value)
            bool_a.value *= 0.5
