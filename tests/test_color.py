"""Test Color class"""
import pytest

import simpleparam as param


class TestColor(object):
    """Test Color class"""

    @staticmethod
    def test_creation_hex():
        """Test Color - correct initilization"""
        value = "#FFF000"
        color = param.Color(value=value)
        assert color.value == value

    @staticmethod
    def test_creation_hex_nohash():
        """Test Color - correct initilization"""
        value = "FFF000"
        color = param.Color(value=value)
        assert color.value == value

    @staticmethod
    def test_creation_shorthex():
        """Test Color - correct initilization"""
        value = "#FFF"
        color = param.Color(value=value)
        assert color.value == value

    @staticmethod
    def test_creation_shorthex_nohash():
        """Test Color - correct initilization"""
        value = "FFF"
        color = param.Color(value=value)
        assert color.value == value

    @staticmethod
    def test_creation_change():
        """Test Color - correct initilization"""
        value = "#FFF"
        color = param.Color(value=value)
        assert color.value == value

        value = "#FFFF00"
        color.value = value
        assert color.value == value

    @staticmethod
    def test_creation_doc():
        """Test Color - correct initilization"""
        value = "#FFF000"
        doc = "I am a color"
        color = param.Color(value=value, doc=doc)
        assert color.doc == doc

    @staticmethod
    def test_kind():
        """Test Color - correct initilization"""
        value = "#FFF000"
        color = param.Color(value=value)

        assert color.kind == "Color"

    @staticmethod
    def test_creation_int():
        """Test Color - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = 42
            __ = param.Color(value=value)

    @staticmethod
    def test_creation_str():
        """Test Color - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = "true"
            __ = param.Color(value=value)

    @staticmethod
    def test_creation_dict():
        """Test Color - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = dict()
            __ = param.Color(value=value)

    @staticmethod
    def test_creation_list():
        """Test Color - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = list()
            __ = param.Color(value=value)

    @staticmethod
    def test_creation_none():
        """Test Color - throw error due to incorrect initilization"""
        with pytest.raises(TypeError) as __:
            value = None
            __ = param.Color(value=value, allow_None=True)

    @staticmethod
    def test_creation_shorthex_bad():
        """Test Color - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = "FFFF"
            __ = param.Color(value=value)

    @staticmethod
    def test_creation_rgb():
        """Test Color - throw error due to incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = "(255, 255, 255)"
            __ = param.Color(value=value)
