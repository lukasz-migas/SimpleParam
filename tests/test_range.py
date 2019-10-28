"""Test Number class"""
import operator

import pytest

import simpleparam as param


class TestRangeSetup(object):
    """Test Range class"""

    @staticmethod
    def test_creation_float():
        """Test Number - correct initilization"""
        value = [0.0, 100.0]

        num_a = param.Range(value=value)
        assert num_a.value == value

    @staticmethod
    def test_creation_doc():
        """Test Number - correct initilization"""
        value = [0.0, 100.0]
        doc = "I am a range"

        num_a = param.Range(value=value, doc=doc)
        assert num_a.value == value
        assert num_a.doc == doc

    @staticmethod
    def test_creation_hardbounds():
        """Test Number - correct initilization"""
        value = [-100, 50]
        hardbounds = [-100, 100]

        num_a = param.Range(value=value, hardbounds=hardbounds)
        assert num_a.value == value
        assert num_a.hardbounds == hardbounds

    @staticmethod
    def test_creation_hardbounds_inclusive():
        """Test Number - correct initilization"""
        value = [-42, 100]
        hardbounds = [-42, 100]

        num_a = param.Range(value=value, hardbounds=hardbounds, inclusive_bounds=[True, True])
        assert num_a.value == value
        assert num_a.hardbounds == hardbounds

    @staticmethod
    def test_creation_hardbounds_autobound():
        """Test Number - correct initilization"""
        value = [-150.0, 999]
        hardbounds = [-100, 100]

        num_a = param.Range(value=value, hardbounds=hardbounds, auto_bound=True)
        assert num_a.value == [-100, 100]

    @staticmethod
    def test_creation_nohardbounds_autobound():
        """Test Number - correct initilization"""
        value = [0, 42]

        num_a = param.Range(value=value, auto_bound=True)
        assert num_a.value == value

    @staticmethod
    def test_allow_none():
        """Test Number - correct initilization"""
        value = None
        num_a = param.Range(value=value, allow_None=True)
        assert num_a.value == value

    @staticmethod
    def test_creation_softbounds():
        """Test Number - correct initilization"""
        value = [-42.0, 0]
        softbounds = [-100, 100]
        num_a = param.Range(value=value, softbounds=softbounds)
        assert num_a.value == value
        assert num_a.softbounds == softbounds

    @staticmethod
    def test_creation_softbounds_tuple():
        """Test Number - correct initilization"""
        value = [-42.0, 150]
        softbounds = (-100, 100)
        num_a = param.Range(value=value, softbounds=softbounds)
        assert num_a.value == value
        assert num_a.softbounds == list(softbounds)

    @staticmethod
    def test_creation_set_softbounds_get_softbounds():
        """Test Number - correct initilization"""
        value = [42.01, 999]
        softbounds = [-100, 100]

        num_a = param.Range(value=value, softbounds=softbounds)
        assert num_a.softbounds == softbounds
        assert num_a.get_soft_bounds() == softbounds

    @staticmethod
    def test_creation_set_hardbounds_get_hardbounds():
        """Test Number - correct initilization"""
        value = [99, 0]
        hardbounds = [-100, 100]

        num_a = param.Range(value=value, hardbounds=hardbounds)
        assert num_a.get_soft_bounds() == hardbounds

    @staticmethod
    def test_creation_set_none_get_none():
        """Test Number - correct initilization"""
        value = [11.01474, 4]
        num_a = param.Range(value=value)
        assert num_a.get_soft_bounds() == [None, None]

    @staticmethod
    def test_kind():
        """Test Number - correct initilization"""
        value = [11.01474, 0]
        num_a = param.Range(value=value)

        assert num_a.kind == "Range"

    @staticmethod
    def test_creation_outside_bounds_lower():
        """Test Number - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = [-1, 40]
            __ = param.Range(value=value, hardbounds=[0, 41])

    @staticmethod
    def test_creation_outside_bounds_upper():
        """Test Number - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = [42, -41]
            __ = param.Range(value=value, hardbounds=[0, 41])

    @staticmethod
    def test_creation_bounds_not_inclusive_lower():
        """Test Number - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = [-42, 100]
            __ = param.Range(value=value, hardbounds=[-42, 100], inclusive_bounds=[False, True])

    @staticmethod
    def test_creation_bounds_not_inclusive_upper():
        """Test Number - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = [-42, 120]
            __ = param.Range(value=value, hardbounds=[-42, 100], inclusive_bounds=[True, False])

    @staticmethod
    def test_creation_notallow_none():
        """Test Number - throw error due to incorrect initilization"""
        with pytest.raises(TypeError) as __:
            value = None
            __ = param.Range(value=value, allow_None=False)

    @staticmethod
    def test_creation_float():
        """Test Number - throw error due to incorrect initilization"""
        with pytest.raises(TypeError) as __:
            value = 1412.0
            __ = param.Range(value=value, allow_None=False)

    @staticmethod
    def test_creation_str():
        """Test Number - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = "42"
            __ = param.Range(value=value)

    @staticmethod
    def test_creation_dict():
        """Test Number - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = dict()
            __ = param.Range(value=value)

    @staticmethod
    def test_creation_list():
        """Test Number - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = list()
            __ = param.Range(value=value)

    @staticmethod
    def test_creation_too_many():
        """Test Number - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = [0, 100, 150]
            __ = param.Range(value=value)

    @staticmethod
    def test_creation_all_numeric():
        """Test Number - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = [0, None]
            __ = param.Range(value=value, allow_None=True)
