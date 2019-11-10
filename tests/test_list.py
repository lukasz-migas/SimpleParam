"""Test List class"""
import pytest

import simpleparam as param


class TestListSetup(object):
    """Test item class"""

    @staticmethod
    def test_creation_good_str():
        """Test List - correct initilization"""
        value = ["boo", "hoo"]
        item = param.List(value=value)
        assert item.value == value

    @staticmethod
    def test_creation_good_int():
        """Test List - correct initilization"""
        value = [1, 2, 3]
        item = param.List(value=value)
        assert item.value == value

    @staticmethod
    def test_doc():
        """Test item - correct initilization"""
        value = [1, 2, 3]
        doc = "I am a list"
        item = param.List(value=value, doc=doc)
        assert item.doc == doc

    @staticmethod
    def test_allow_None():
        """Test List - correct initilization"""
        value = None
        item = param.List(value=value, allow_None=True)
        assert item.value is value

    @staticmethod
    def test_notallow_none():
        """Test item - incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = None
            item = param.List(value=value, allow_None=False)

    @staticmethod
    def test_kind():
        """Test List - correct initilization"""
        value = [1, 2312314]
        item = param.List(value=value)

        assert item.kind == "List"

    @staticmethod
    def test_creation_hardbounds():
        """Test List - correct initilization"""
        value = [1]
        hardbounds = [0, 2]

        item = param.List(value=value, hardbounds=hardbounds)
        assert item.value == value
        assert item.hardbounds == hardbounds

    @staticmethod
    def test_creation_hardbounds_tuple():
        """Test List - correct initilization"""
        value = [1]
        hardbounds = (0, 2)

        item = param.List(value=value, hardbounds=hardbounds)
        assert item.value == value
        assert item.hardbounds == list(hardbounds)

    @staticmethod
    def test_creation_hardbounds_too_short():
        """Test List - correct initilization"""
        with pytest.raises(ValueError) as __:
            value = [1]
            hardbounds = [0]
            __ = param.List(value=value, hardbounds=hardbounds)

    @staticmethod
    def test_creation_hardbounds_too_long():
        """Test List - correct initilization"""
        with pytest.raises(ValueError) as __:
            value = [1]
            hardbounds = [0, 2, 4]
            __ = param.List(value=value, hardbounds=hardbounds)

    @staticmethod
    def test_creation_outside_bounds_lower():
        """Test List - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = [1]
            __ = param.List(value=value, hardbounds=[2, 3])

    @staticmethod
    def test_creation_outside_bounds_upper():
        """Test List - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = [1, 3, 4, 5]
            __ = param.List(value=value, hardbounds=[0, 3])

    @staticmethod
    def test_creation_dict():
        """Test List - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = dict()
            __ = param.List(value=value)

    @staticmethod
    def test_creation_num():
        """Test List - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = 42
            __ = param.List(value=value)

    @staticmethod
    def test_creation_str():
        """Test List - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = "hello"
            __ = param.List(value=value)


class TestListOperations(object):
    """Test List class operations"""

    @staticmethod
    def test_contains():
        """Test List"""
        a = param.List([1, 2, 3], hardbounds=[0, 4])
        assert 1 in a

    @staticmethod
    def test_getitem():
        """Test List"""
        value = [1, 2, 3]
        expected = list(value)
        a = param.List(value, hardbounds=[0, 4])
        assert a[0] == expected[0]

    @staticmethod
    def test_setitem():
        """Test List"""
        value = [1, 2, 3]
        expected = list(value)
        a = param.List(value, hardbounds=[0, 4])
        a[0] = 42
        expected[0] = 42
        assert a.value == expected

    @staticmethod
    def test_delitem():
        value = [1, 2, 3]
        expected = list(value)
        a = param.List(value, hardbounds=[0, 4])
        del a[0]
        del expected[0]
        assert a.value == expected
