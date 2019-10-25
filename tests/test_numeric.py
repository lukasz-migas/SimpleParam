"""Test Numeric classes"""
import pytest

import simpleparam as param


class TestNumber(object):
    """Test Number class"""

    @staticmethod
    def test_creation_good():
        """Test Number - correct initilization"""
        value = 1.0
        num_a = param.Number(value=value)
        assert num_a.value == value

        value = 42.01
        num_a = param.Number(value=value, doc="test doc")
        assert num_a.value == value

        value = -42.0
        num_a = param.Number(value=value, hardbounds=[-100, 100])
        assert num_a.value == value

        value = -42
        num_a = param.Number(value=value, hardbounds=[-42, 100], inclusive_bounds=[True, True])
        assert num_a.value == value

        value = -42.0247
        num_a = param.Number(value=value, softbounds=[-100, 100])
        assert num_a.value == value

        value = -150.0
        num_a = param.Number(value=value, hardbounds=[-100, 100], auto_bound=True)
        assert num_a.value == -100

        value = None
        num_a = param.Number(value=value, allow_None=True)
        assert num_a.value == value

    @staticmethod
    def test_creation_bad():
        """Test Number - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = 42
            __ = param.Number(value=value, hardbounds=[0, 41])

        with pytest.raises(ValueError) as __:
            value = -42
            __ = param.Number(value=value, hardbounds=[-42, 100], inclusive_bounds=[False, False])

        with pytest.raises(ValueError) as __:
            value = None
            __ = param.Number(value=value, allow_None=False)

        with pytest.raises(ValueError) as __:
            value = "42"
            __ = param.Number(value=value)

        with pytest.raises(ValueError) as __:
            value = None
            __ = param.Number(value=value, allow_None=False)


class TestInteger(object):
    """Test Integer class"""

    @staticmethod
    def test_creation_good():
        """Test Integer - correct initilization"""
        value = 1
        num_a = param.Integer(value=value)
        assert num_a.value == value

        value = 42
        num_a = param.Integer(value=value, doc="test doc")
        assert num_a.value == value

        value = -42
        num_a = param.Integer(value=value, hardbounds=[-100, 100])
        assert num_a.value == value

        value = -42
        num_a = param.Integer(value=value, hardbounds=[-42, 100], inclusive_bounds=[True, True])
        assert num_a.value == value

        value = -42
        num_a = param.Integer(value=value, softbounds=[-100, 100])
        assert num_a.value == value

        value = -150
        num_a = param.Integer(value=value, hardbounds=[-100, 100], auto_bound=True)
        assert num_a.value == -100

        value = None
        num_a = param.Integer(value=value, allow_None=True)
        assert num_a.value == value

    @staticmethod
    def test_creation_bad():
        """Test Integer - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = 42
            __ = param.Integer(value=value, hardbounds=[0, 41])

        with pytest.raises(ValueError) as __:
            value = -42
            __ = param.Integer(value=value, hardbounds=[-42, 100], inclusive_bounds=[False, False])

        with pytest.raises(ValueError) as __:
            value = None
            __ = param.Integer(value=value, allow_None=False)

        with pytest.raises(ValueError) as __:
            value = "42"
            __ = param.Integer(value=value)

        with pytest.raises(ValueError) as __:
            value = None
            __ = param.Integer(value=value, allow_None=False)
