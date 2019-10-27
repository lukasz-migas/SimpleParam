"""Test Integer class"""
import pytest
import operator

import simpleparam as param


class TestIntegerSetup(object):
    """Test Integer class"""

    @staticmethod
    def test_creation_float():
        """Test Integer - correct initilization"""
        value = 1

        num_a = param.Integer(value=value)
        assert num_a.value == value

    @staticmethod
    def test_creation_doc():
        """Test Integer - correct initilization"""
        value = 42
        doc = "I am an int"

        num_a = param.Integer(value=value, doc=doc)
        assert num_a.value == value
        assert num_a.doc == doc

    @staticmethod
    def test_creation_hardbounds():
        """Test Integer - correct initilization"""
        value = -42
        hardbounds = [-100, 100]

        num_a = param.Integer(value=value, hardbounds=hardbounds)
        assert num_a.value == value
        assert num_a.hardbounds == hardbounds

    @staticmethod
    def test_creation_hardbounds_inclusive():
        """Test Integer - correct initilization"""
        value = -42
        hardbounds = [-42, 100]

        num_a = param.Integer(value=value, hardbounds=hardbounds, inclusive_bounds=[True, True])
        assert num_a.value == value
        assert num_a.hardbounds == hardbounds

    @staticmethod
    def test_creation_hardbounds_autobound():
        """Test Integer - correct initilization"""
        value = -150
        hardbounds = [-100, 100]

        num_a = param.Integer(value=value, hardbounds=hardbounds, auto_bound=True)
        assert num_a.value == -100

    @staticmethod
    def test_allow_none():
        """Test Integer - correct initilization"""
        value = None
        num_a = param.Integer(value=value, allow_None=True)
        assert num_a.value == value

    @staticmethod
    def test_creation_softbounds():
        """Test Integer - correct initilization"""
        value = -42
        softbounds = [-100, 100]
        num_a = param.Integer(value=value, softbounds=softbounds)
        assert num_a.value == value
        assert num_a.softbounds == softbounds

    @staticmethod
    def test_creation_set_softbounds_get_softbounds():
        """Test Integer - correct initilization"""
        value = 42
        softbounds = [-100, 100]

        num_a = param.Integer(value=value, softbounds=softbounds)
        assert num_a.softbounds == softbounds
        assert num_a.get_soft_bounds() == softbounds

    @staticmethod
    def test_creation_set_hardbounds_get_hardbounds():
        """Test Integer - correct initilization"""
        value = 99
        hardbounds = [-100, 100]

        num_a = param.Integer(value=value, hardbounds=hardbounds)
        assert num_a.get_soft_bounds() == hardbounds

    @staticmethod
    def test_creation_set_none_get_none():
        """Test Integer - correct initilization"""
        value = 11
        num_a = param.Integer(value=value)
        assert num_a.get_soft_bounds() == [None, None]

    @staticmethod
    def test_kind():
        """Test Integer - correct initilization"""
        value = 11
        num_a = param.Integer(value=value)

        assert num_a.kind == "Integer"

    @staticmethod
    def test_creation_outside_bounds():
        """Test Integer - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = 42
            __ = param.Integer(value=value, hardbounds=[0, 41])

    @staticmethod
    def test_creation_bounds_not_inclusive():
        """Test Integer - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = -42
            __ = param.Integer(value=value, hardbounds=[-42, 100], inclusive_bounds=[False, False])

    @staticmethod
    def test_creation_notallow_none():
        """Test Integer - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = None
            __ = param.Integer(value=value, allow_None=False)

    @staticmethod
    def test_creation_float():
        """Test Integer - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = 42.30474
            __ = param.Integer(value=value)

    @staticmethod
    def test_creation_str():
        """Test Integer - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = "42"
            __ = param.Integer(value=value)

    @staticmethod
    def test_creation_dict():
        """Test Integer - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = dict()
            __ = param.Integer(value=value)

    @staticmethod
    def test_creation_list():
        """Test Integer - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = list()
            __ = param.Integer(value=value)

    @staticmethod
    def test_creation_incorrect_softbounds_count():
        """Test Integer - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = 1
            __ = param.Integer(value=value, softbounds=[0, 10, 20])

    @staticmethod
    def test_creation_incorrect_hardbounds_count():
        """Test Integer - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = 1
            __ = param.Integer(value=value, hardbounds=[0, 10, 20])

    @staticmethod
    def test_creation_incorrect_change_softbounds():
        """Test Integer - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = 1
            int_a = param.Integer(value=value, softbounds=[0, 10])
            int_a.softbounds = [0, 10, 20]

    @staticmethod
    def test_creation_incorrect_change_hardbounds():
        """Test Integer - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = 1
            int_a = param.Integer(value=value, hardbounds=[0, 10])
            int_a.hardbounds = [0, 10, 20]


class TestIntegerOperations(object):
    """Test Integer class operations"""

    @staticmethod
    def test_add():
        """Test Integer - correct operation"""
        value = 42
        num_a = param.Integer(value=value)
        assert num_a.value == value

        new_value = value + 1
        num_a.value += 1
        assert num_a.value == new_value

    @staticmethod
    def test_add_float():
        """Test Integer - incorrect operation"""
        with pytest.raises(ValueError) as __:
            value = 42
            num_a = param.Integer(value=value)
            assert num_a.value == value

            num_a.value += 1.5

    @staticmethod
    def test_sub():
        """Test Integer - correct operation"""
        value = 42
        num_a = param.Integer(value=value)
        assert num_a.value == value

        new_value = value - 1
        num_a.value -= 1
        assert num_a.value == new_value

    @staticmethod
    def test_sub_float():
        """Test Integer - incorrect operation"""
        with pytest.raises(ValueError) as __:
            value = 42
            num_a = param.Integer(value=value)
            assert num_a.value == value

            num_a.value -= 1.5

    @staticmethod
    def test_div():
        """Test Integer - incorrect operation"""
        with pytest.raises(ValueError) as __:
            value = 42
            num_a = param.Integer(value=value)
            assert num_a.value == value

            num_a.value /= 2

    @staticmethod
    def test_mul():
        """Test Integer - correct operation"""
        value = 42
        num_a = param.Integer(value=value)
        assert num_a.value == value

        new_value = value * 2
        num_a.value *= 2
        assert num_a.value == new_value

    @staticmethod
    def test_mul_float():
        """Test Integer - incorrect operation"""
        with pytest.raises(ValueError) as __:
            value = 42
            num_a = param.Integer(value=value)
            assert num_a.value == value

            num_a.value *= 1.5

    @staticmethod
    def test_pow():
        """Test Integer - correct operation"""
        value = 42
        num_a = param.Integer(value=value)
        assert num_a.value == value

        new_value = value ** 2
        num_a.value **= 2
        assert num_a.value == new_value

    @staticmethod
    def test_floordiv():
        """Test Integer - correct operation"""
        value = 42
        num_a = param.Integer(value=value)
        assert num_a.value == value

        new_value = value // 2
        num_a.value //= 2
        assert num_a.value == new_value

    @staticmethod
    def test_mod():
        """Test Integer - correct operation"""
        value = 42
        num_a = param.Integer(value=value)
        assert num_a.value == value

        new_value = value % 2
        num_a.value %= 2
        assert num_a.value == new_value

    @staticmethod
    def test_mod_float():
        """Test Integer - incorrect operation"""
        with pytest.raises(ValueError) as __:
            value = 42
            num_a = param.Integer(value=value)
            assert num_a.value == value

            num_a.value %= 1.5

    @staticmethod
    def test_rshift():
        """Test Integer - correct operation"""
        value = 42
        num_a = param.Integer(value=value)
        assert num_a.value == value

        new_value = operator.rshift(value, 1)
        num_a.value >>= 1
        assert num_a.value == new_value

    @staticmethod
    def test_lshift():
        """Test Integer - correct operation"""
        value = 42
        num_a = param.Integer(value=value)
        assert num_a.value == value

        new_value = operator.lshift(value, 1)
        num_a.value <<= 1
        assert num_a.value == new_value

    @staticmethod
    def test_lt():
        """Test Integer - correct operation"""
        value = 42
        num_a = param.Integer(value=value)
        assert num_a.value == value

        assert num_a.value < 100

    @staticmethod
    def test_gt():
        """Test Integer - correct operation"""
        value = 42
        num_a = param.Integer(value=value)
        assert num_a.value == value

        assert num_a.value > 1

    @staticmethod
    def test_abs():
        """Test Integer - correct operation"""
        value = -42
        num_a = param.Integer(value=value)
        assert abs(num_a.value) == abs(value)

    @staticmethod
    def test_neg():
        """Test Integer - correct operation"""
        value = -42
        num_a = param.Integer(value=value)
        assert -num_a.value == -value

    @staticmethod
    def test_pos():
        """Test Integer - correct operation"""
        value = -42
        num_a = param.Integer(value=value)
        assert +num_a.value == +value
