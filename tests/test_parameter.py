"""Test Parameter class"""
import operator

import pytest

import simpleparam as param


class TestParameterSetup(object):
    """Test Parameter class"""

    @staticmethod
    def test_creation_float():
        """Test Parameter - correct initilization"""
        value = 1.0

        num_a = param.Parameter(value=value)
        assert num_a.value == value

    @staticmethod
    def test_creation_doc():
        """Test Parameter - correct initilization"""
        value = 42.01
        doc = "I am a parameter"

        num_a = param.Parameter(value=value, doc=doc)
        assert num_a.value == value
        assert num_a.doc == doc

    @staticmethod
    def test_allow_none():
        """Test Parameter - correct initilization"""
        value = None
        num_a = param.Parameter(value=value, allow_None=True)
        assert num_a.value == value

    @staticmethod
    def test_kind():
        """Test Parameter - correct initilization"""
        value = 11.01474
        num_a = param.Parameter(value=value)

        assert num_a.kind == "Parameter"


class TestParameterOperations(object):
    """Test Parameter class operations"""

    @staticmethod
    def test_add():
        """Test Parameter - correct initilization"""
        value = 42.01
        num_a = param.Parameter(value=value)
        assert num_a.value == value

        new_value = value + 1
        num_a.value += 1
        assert num_a.value == new_value

    @staticmethod
    def test_sub():
        """Test Parameter - correct initilization"""
        value = 42.01
        num_a = param.Parameter(value=value)
        assert num_a.value == value

        new_value = value - 1
        num_a.value -= 1
        assert num_a.value == new_value

    @staticmethod
    def test_div():
        """Test Parameter - correct initilization"""
        value = 42.0
        num_a = param.Parameter(value=value)
        assert num_a.value == value

        new_value = value / 2
        num_a.value /= 2
        assert num_a.value == new_value

    @staticmethod
    def test_mul():
        """Test Parameter - correct initilization"""
        value = 42.01
        num_a = param.Parameter(value=value)
        assert num_a.value == value

        new_value = value * 2
        num_a.value *= 2
        assert num_a.value == new_value

    @staticmethod
    def test_pow():
        """Test Parameter - correct initilization"""
        value = 42.01
        num_a = param.Parameter(value=value)
        assert num_a.value == value

        new_value = value ** 2
        num_a.value **= 2
        assert num_a.value == new_value

    @staticmethod
    def test_floordiv():
        """Test Parameter - correct initilization"""
        value = 42.01
        num_a = param.Parameter(value=value)
        assert num_a.value == value

        new_value = value // 2
        num_a.value //= 2
        assert num_a.value == new_value

    @staticmethod
    def test_mod():
        """Test Parameter - correct initilization"""
        value = 42.01
        num_a = param.Parameter(value=value)
        assert num_a.value == value

        new_value = value % 2
        num_a.value %= 2
        assert num_a.value == new_value

    @staticmethod
    def test_rshift():
        """Test Parameter - correct initilization"""
        value = 42
        num_a = param.Parameter(value=value)
        assert num_a.value == value

        new_value = operator.rshift(value, 1)
        num_a.value >>= 1
        assert num_a.value == new_value

    @staticmethod
    def test_lshift():
        """Test Parameter - correct initilization"""
        value = 42
        num_a = param.Parameter(value=value)
        assert num_a.value == value

        new_value = operator.lshift(value, 1)
        num_a.value <<= 1
        assert num_a.value == new_value

    @staticmethod
    def test_lt():
        """Test Parameter - correct initilization"""
        value = 42.01
        num_a = param.Parameter(value=value)
        assert num_a.value == value

        assert num_a.value < 100

    @staticmethod
    def test_gt():
        """Test Parameter - correct initilization"""
        value = 42.01
        num_a = param.Parameter(value=value)
        assert num_a.value == value

        assert num_a.value > 1

    @staticmethod
    def test_abs():
        """Test Parameter - correct initilization"""
        value = -42.01
        num_a = param.Parameter(value=value)
        assert abs(num_a.value) == abs(value)

    @staticmethod
    def test_neg():
        """Test Parameter - correct initilization"""
        value = -42.01
        num_a = param.Parameter(value=value)
        assert -num_a.value == -value

    @staticmethod
    def test_pos():
        """Test Parameter - correct initilization"""
        value = -42.01
        num_a = param.Parameter(value=value)
        assert +num_a.value == +value
