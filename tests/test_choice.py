"""Test Choice class"""
import pytest

import simpleparam as param


class TestChoiceSetup(object):
    """Test Choice class"""

    @staticmethod
    def test_creation_good():
        """Test Choice - correct initilization"""
        value = "boo"
        choices = ["boo", "foo"]
        choice = param.Choice(value=value, choices=choices)
        assert choice.value == value
        assert choice.choices == choices

    @staticmethod
    def test_kind():
        """Test Choice - correct initilization"""
        value = "boo"
        choices = ["boo", "foo"]
        doc = "I am a choice"
        choice = param.Choice(value=value, doc=doc, choices=choices)
        assert choice.doc == doc

    @staticmethod
    def test_str():
        """Test Choice - correct initilization"""
        value = "boo"
        choices = ["boo", "foo"]
        choice = param.Choice(value=value, choices=choices)
        assert choice.value == value
        assert choice.choices == choices
        assert str(choice) == "Choice(name=param, value='boo', choices=['boo', 'foo'], doc='')"

    @staticmethod
    def test_change_choices():
        """Test Choice - correct initilization"""
        value = "boo"
        choices = ["boo", "foo"]
        choice = param.Choice(value=value, choices=choices)
        assert choice.value == value
        assert choice.choices == choices

        choices = ["boo", "foo", "baz"]
        choice.choices = choices
        assert choice.choices == choices

    @staticmethod
    def test_creation_bool():
        """Test Choice - correct initilization"""
        value = False
        choices = [True, False]
        choice = param.Choice(value=value, choices=choices)
        assert choice.value == value
        assert choice.choices == choices

    @staticmethod
    def test_allow_none():
        """Test Choice - correct initilization"""
        value = None
        choices = [True, False]
        choice = param.Choice(value=value, choices=choices, allow_None=True)

        assert choice.kind == "Choice"

    @staticmethod
    def test_missing_in_choice():
        """Test Choice - incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = "true"
            choices = [True, False]
            choice = param.Choice(value=value, choices=choices)

    @staticmethod
    def test_missing_choice_not_list():
        """Test Choice - incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = "true"
            choices = "true"
            choice = param.Choice(value=value, choices=choices)

    @staticmethod
    def test_notallow_none():
        """Test Choice - incorrect initilization"""
        with pytest.raises(ValueError) as __:
            value = None
            choices = [True, False]
            choice = param.Choice(value=value, choices=choices, allow_None=False)


class TestChoiceOperations(object):
    """Test Boolean class operations"""

    @staticmethod
    def test_add():
        """Test Boolean - correct initilization"""
        value = False
        choices = [True, False]
        choice = param.Choice(value=value, choices=choices)
        assert choice.value == value
        assert choice.choices == choices
        assert False in choices
