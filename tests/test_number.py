"""Test Number class"""
import operator

import pytest

import simpleparam as param


class TestNumberSetup(object):
    """Test Number class"""

    @staticmethod
    def test_creation_float():
        """Test Number - correct initilization"""
        value = 1.0

        num_a = param.Number(value=value)
        assert num_a.value == value

    @staticmethod
    def test_creation_doc():
        """Test Number - correct initilization"""
        value = 42.01
        doc = "I am a float"

        num_a = param.Number(value=value, doc=doc)
        assert num_a.value == value
        assert num_a.doc == doc

    @staticmethod
    def test_creation_hardbounds():
        """Test Number - correct initilization"""
        value = -42.0
        hardbounds = [-100, 100]

        num_a = param.Number(value=value, hardbounds=hardbounds)
        assert num_a.value == value
        assert num_a.hardbounds == hardbounds

    @staticmethod
    def test_creation_hardbounds_inclusive():
        """Test Number - correct initilization"""
        value = -42
        hardbounds = [-42, 100]

        num_a = param.Number(value=value, hardbounds=hardbounds, inclusive_bounds=[True, True])
        assert num_a.value == value
        assert num_a.hardbounds == hardbounds

    @staticmethod
    def test_creation_hardbounds_autobound():
        """Test Number - correct initilization"""
        value = -150.0
        hardbounds = [-100, 100]

        num_a = param.Number(value=value, hardbounds=hardbounds, auto_bound=True)
        assert num_a.value == -100

    @staticmethod
    def test_creation_nohardbounds_autobound():
        """Test Number - correct initilization"""
        value = -150.0

        num_a = param.Number(value=value, auto_bound=True)
        assert num_a.value == value

    @staticmethod
    def test_allow_none():
        """Test Number - correct initilization"""
        value = None
        num_a = param.Number(value=value, allow_None=True)
        assert num_a.value == value

    @staticmethod
    def test_creation_softbounds():
        """Test Number - correct initilization"""
        value = -42.0
        softbounds = [-100, 100]
        num_a = param.Number(value=value, softbounds=softbounds)
        assert num_a.value == value
        assert num_a.softbounds == softbounds

    @staticmethod
    def test_creation_set_softbounds_get_softbounds():
        """Test Number - correct initilization"""
        value = 42.01
        softbounds = [-100, 100]

        num_a = param.Number(value=value, softbounds=softbounds)
        assert num_a.softbounds == softbounds
        assert num_a.get_soft_bounds() == softbounds

    @staticmethod
    def test_creation_set_hardbounds_get_hardbounds():
        """Test Number - correct initilization"""
        value = 99
        hardbounds = [-100, 100]

        num_a = param.Number(value=value, hardbounds=hardbounds)
        assert num_a.get_soft_bounds() == hardbounds

    @staticmethod
    def test_creation_set_none_get_none():
        """Test Number - correct initilization"""
        value = 11.01474
        num_a = param.Number(value=value)
        assert num_a.get_soft_bounds() == [None, None]

    @staticmethod
    def test_kind():
        """Test Number - correct initilization"""
        value = 11.01474
        num_a = param.Number(value=value)

        assert num_a.kind == "Number"

    @staticmethod
    def test_creation_outside_bounds_lower():
        """Test Number - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = -1
            __ = param.Number(value=value, hardbounds=[0, 41])

    @staticmethod
    def test_creation_outside_bounds_upper():
        """Test Number - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = 42
            __ = param.Number(value=value, hardbounds=[0, 41])

    @staticmethod
    def test_creation_bounds_not_inclusive_lower():
        """Test Number - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = -42
            __ = param.Number(value=value, hardbounds=[-42, 100], inclusive_bounds=[False, False])

    @staticmethod
    def test_creation_bounds_not_inclusive_upper():
        """Test Number - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = 120
            __ = param.Number(value=value, hardbounds=[-42, 100], inclusive_bounds=[False, False])

    @staticmethod
    def test_creation_notallow_none():
        """Test Number - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = None
            __ = param.Number(value=value, allow_None=False)

    @staticmethod
    def test_creation_str():
        """Test Number - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = "42"
            __ = param.Number(value=value)

    @staticmethod
    def test_creation_dict():
        """Test Number - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = dict()
            __ = param.Number(value=value)

    @staticmethod
    def test_creation_list():
        """Test Number - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = list()
            __ = param.Number(value=value)


class TestNumberOperations(object):
    """Test Number class operations"""

    @staticmethod
    def test_add():
        """Test Number - correct initilization"""
        value = 42.01
        num_a = param.Number(value=value)
        assert num_a.value == value

        new_value = value + 1
        num_a.value += 1
        assert num_a.value == new_value

    @staticmethod
    def test_sub():
        """Test Number - correct initilization"""
        value = 42.01
        num_a = param.Number(value=value)
        assert num_a.value == value

        new_value = value - 1
        num_a.value -= 1
        assert num_a.value == new_value

    @staticmethod
    def test_div():
        """Test Number - correct initilization"""
        value = 42.0
        num_a = param.Number(value=value)
        assert num_a.value == value

        new_value = value / 2
        num_a.value /= 2
        assert num_a.value == new_value

    @staticmethod
    def test_mul():
        """Test Number - correct initilization"""
        value = 42.01
        num_a = param.Number(value=value)
        assert num_a.value == value

        new_value = value * 2
        num_a.value *= 2
        assert num_a.value == new_value

    @staticmethod
    def test_pow():
        """Test Number - correct initilization"""
        value = 42.01
        num_a = param.Number(value=value)
        assert num_a.value == value

        new_value = value ** 2
        num_a.value **= 2
        assert num_a.value == new_value

    @staticmethod
    def test_floordiv():
        """Test Number - correct initilization"""
        value = 42.01
        num_a = param.Number(value=value)
        assert num_a.value == value

        new_value = value // 2
        num_a.value //= 2
        assert num_a.value == new_value

    @staticmethod
    def test_mod():
        """Test Number - correct initilization"""
        value = 42.01
        num_a = param.Number(value=value)
        assert num_a.value == value

        new_value = value % 2
        num_a.value %= 2
        assert num_a.value == new_value

    @staticmethod
    def test_rshift():
        """Test Number - correct initilization"""
        value = 42
        num_a = param.Number(value=value)
        assert num_a.value == value

        new_value = operator.rshift(value, 1)
        num_a.value >>= 1
        assert num_a.value == new_value

    @staticmethod
    def test_lshift():
        """Test Number - correct initilization"""
        value = 42
        num_a = param.Number(value=value)
        assert num_a.value == value

        new_value = operator.lshift(value, 1)
        num_a.value <<= 1
        assert num_a.value == new_value

    @staticmethod
    def test_lt():
        """Test Number - correct initilization"""
        value = 42.01
        num_a = param.Number(value=value)
        assert num_a.value == value

        assert num_a.value < 100

    @staticmethod
    def test_gt():
        """Test Number - correct initilization"""
        value = 42.01
        num_a = param.Number(value=value)
        assert num_a.value == value

        assert num_a.value > 1

    @staticmethod
    def test_abs():
        """Test Number - correct initilization"""
        value = -42.01
        num_a = param.Number(value=value)
        assert abs(num_a.value) == abs(value)

    @staticmethod
    def test_neg():
        """Test Number - correct initilization"""
        value = -42.01
        num_a = param.Number(value=value)
        assert -num_a.value == -value

    @staticmethod
    def test_pos():
        """Test Number - correct initilization"""
        value = -42.01
        num_a = param.Number(value=value)
        assert +num_a.value == +value
