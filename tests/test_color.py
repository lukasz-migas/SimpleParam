"""Test Color class"""
import pytest

import simpleparam as param


class TestColor(object):
    """Test Color class"""

    @staticmethod
    def test_creation_good():
        """Test Color - correct initilization"""
        value = "#FFF000"
        color = param.Color(value=value)
        assert color.value == value

        doc = "test doc"
        color = param.Color(value=value, doc=doc)
        assert color.doc == doc

        assert color.kind == "Color"

    @staticmethod
    def test_creation_bad():
        """Test Color - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = 42
            __ = param.Color(value=value)

        with pytest.raises(ValueError) as __:
            value = "true"
            __ = param.Color(value=value)

        with pytest.raises(ValueError) as __:
            value = dict()
            __ = param.Color(value=value)

        with pytest.raises(ValueError) as __:
            value = list()
            __ = param.Color(value=value)

        with pytest.raises(TypeError) as __:
            value = None
            __ = param.Color(value=value, allow_None=True)

        with pytest.raises(ValueError) as __:
            value = "FFFF"
            __ = param.Color(value=value)

        with pytest.raises(ValueError) as __:
            value = "(255, 255, 255)"
            __ = param.Color(value=value)
