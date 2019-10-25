"""Test Boolean class"""
import pytest

import simpleparam as param


class TestBoolean(object):
    """Test Boolean class"""

    @staticmethod
    def test_creation_good():
        """Test Boolean - correct initilization"""
        value = True
        bool_a = param.Boolean(value=value)
        assert bool_a.value == value

        value = False
        bool_a = param.Boolean(value=value)
        assert bool_a.value == value

        doc = "test doc"
        bool_a = param.Boolean(value=value, doc=doc)
        assert bool_a.doc == doc

        value = None
        bool_a = param.Boolean(value=value, doc=doc, allow_None=True)
        assert bool_a.value == value

        assert bool_a.kind == "Boolean"

    @staticmethod
    def test_creation_bad():
        """Test Boolean - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = 42
            __ = param.Boolean(value=value)

        with pytest.raises(ValueError) as __:
            value = "true"
            __ = param.Boolean(value=value)

        with pytest.raises(ValueError) as __:
            value = dict()
            __ = param.Boolean(value=value)

        with pytest.raises(ValueError) as __:
            value = list()
            __ = param.Boolean(value=value)

        with pytest.raises(ValueError) as __:
            value = None
            __ = param.Boolean(value=value, allow_None=False)
