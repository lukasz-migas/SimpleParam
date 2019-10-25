"""Test Choice class"""
import pytest

import simpleparam as param


class TestChoice(object):
    """Test Choice class"""

    @staticmethod
    def test_creation_good():
        """Test Choice - correct initilization"""
        value = "boo"
        choices = ["boo", "foo"]
        choice = param.Choice(value=value, choices=choices)
        assert choice.value == value
        assert choice.choices == choices

        choices = ["boo", "foo", "baz"]
        choice.choices = choices
        assert choice.choices == choices

        value = False
        choices = [True, False]
        choice = param.Choice(value=value, choices=choices)
        assert choice.value == value
        assert choice.choices == choices

        doc = "test doc"
        choice = param.Choice(value=value, doc=doc, choices=choices)
        assert choice.doc == doc

        value = None
        choices = [True, False]
        choice = param.Choice(value=value, choices=choices, allow_None=True)
        assert choice.value == value

        assert choice.kind == "Choice"

    # @staticmethod
    # def test_creation_bad():
    #     """Test Choice - throw error due to incorrect initilization"""
    #     with pytest.raises(ValueError) as __:
    #         value = 42
    #         __ = param.Choice(value=value)

    #     with pytest.raises(ValueError) as __:
    #         value = "true"
    #         __ = param.Choice(value=value)

    #     with pytest.raises(ValueError) as __:
    #         value = dict()
    #         __ = param.Choice(value=value)

    #     with pytest.raises(ValueError) as __:
    #         value = list()
    #         __ = param.Choice(value=value)

    #     with pytest.raises(ValueError) as __:
    #         value = None
    #         __ = param.Choice(value=value, allow_None=False)
