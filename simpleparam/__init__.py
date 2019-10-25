"""
Simplified version of the `param` library (https://param.pyviz.org/).

`simpleparam` tries to emulate the best features of `param` by providing a subset of availabel classes/objects while
making it slightly easier to use while also allowing easy expansion
"""
import re

from .store import ParameterStore  # noqa
from .utilities import is_number

__all__ = ["Parameter", "Number", "Integer", "String", "Boolean", "Choice", "Option", "Color", "ParameterStore"]


class Parameter(object):
    """
    Base class for most of the other classes
    """

    __slots__ = [
        "name",
        "doc",
        "_value",
        "bounds",
        "_softbounds",
        "hardbounds",
        "saveable",
        "allow_None",
        "inclusive_bounds",
        "auto_bound",
        "step",
        "_kind",
        "constant",
    ]

    def __init__(self, **kws):
        self.name = kws.get("name", "param")
        self.doc = kws.get("doc", "")
        self._value = kws.get("value", None)
        self._softbounds = kws.get("softbounds", None)
        self.hardbounds = kws.get("hardbounds", None)
        self.allow_None = kws.get("allow_None", True)
        self.auto_bound = kws.get("auto_bound", False)
        self.inclusive_bounds = kws.get("inclusive_bounds", [True, True])
        self.saveable = kws.get("saveable", True)
        self._kind = kws.get("kind", "Parameter")
        self.constant = kws.get("constant", False)
        self.step = kws.get("step", None)

    def __repr__(self):
        return "Parameter(name='%s', value=%s, doc='%s')" % (self.name, self.value, self.doc)

    def _validate(self, val):
        """Implements validation for the parameter"""
        return val

    def _validate_bool(self, val):
        """Ensure value is either True/False"""
        if val in [True, False]:
            return val
        raise ValueError("Value must be a Boolean")

    @property
    def value(self):
        """Get `value`"""
        return self._value

    @value.setter
    def value(self, value):
        """Set `value`"""
        self._value = self._validate(value)

    @property
    def kind(self):
        """Get `kind`"""
        return self._kind

    @kind.setter
    def kind(self, value):
        """Set `kind`"""
        self._kind = self._validate(value)


class Number(Parameter):
    """
    Number class, allowing storing of `numeric` objects
    """

    def __init__(self, value, kind="Number", **kws):
        super(Number, self).__init__(value=value, kind=kind, **kws)

        self.value = self._validate(self._value)

    # Allow softbounds to be used like a normal attribute, as it
    # probably should have been already (not _softbounds)
    @property
    def softbounds(self):
        """Get `softbounds`"""
        return self._softbounds

    @softbounds.setter
    def softbounds(self, value):
        """Set `softbounds`"""
        self._softbounds = value

    def _validate(self, val):
        """
        Checks that the value is numeric and that it is within the hard
        bounds; if not, an exception is raised.
        """
        if self.allow_None and val is None:
            return val

        if not is_number(val):
            raise ValueError("Parameter '%s' only takes numeric values" % (self.name))

        if self.auto_bound:
            val = self.crop_to_bounds(val)

        self._check_bounds(val)
        return val

    def _check_bounds(self, val):

        if self.hardbounds is not None:
            vmin, vmax = self.hardbounds
            incmin, incmax = self.inclusive_bounds

            # Could simplify: see https://github.com/ioam/param/issues/83
            if vmax is not None:
                if incmax is True:
                    if not val <= vmax:
                        raise ValueError("Parameter '{}' must be at most {}".format(self.name, vmax))
                else:
                    if not val < vmax:
                        raise ValueError("Parameter '{}' must be less than {}".format(self.name, vmax))

            if vmin is not None:
                if incmin is True:
                    if not val >= vmin:
                        raise ValueError("Parameter '{}' must be at least {}".format(self.name, vmin))
                else:
                    if not val > vmin:
                        raise ValueError("Parameter '{}' must be greater than {}".format(self.name, vmin))

    def get_soft_bounds(self):
        """
        For each soft bound (upper and lower), if there is a defined bound (not equal to None)
        then it is returned, otherwise it defaults to the hard bound. The hard bound could still be None.
        """
        if self.hardbounds is None:
            hard_lower, hard_upper = (None, None)
        else:
            hard_lower, hard_upper = self.hardbounds

        if self.softbounds is None:
            soft_lower, soft_upper = (None, None)
        else:
            soft_lower, soft_upper = self.softbounds

        if soft_lower is None:
            lower = hard_lower
        else:
            lower = soft_lower

        if soft_upper is None:
            upper = hard_upper
        else:
            upper = soft_upper

        return (lower, upper)

    def crop_to_bounds(self, val):
        """
        Return the given value cropped to be within the hard bounds
        for this parameter.

        If a numeric value is passed in, check it is within the hard
        bounds. If it is larger than the high bound, return the high
        bound. If it's smaller, return the low bound. In either case, the
        returned value could be None.  If a non-numeric value is passed
        in, set to be the default value (which could be None).  In no
        case is an exception raised; all values are accepted.
        """
        # Currently, values outside the bounds are silently cropped to
        # be inside the bounds; it may be appropriate to add a warning
        # in such cases.
        if is_number(val):
            if self.hardbounds is None:
                return val
            vmin, vmax = self.hardbounds
            if vmin is not None:
                if val < vmin:
                    return vmin

            if vmax is not None:
                if val > vmax:
                    return vmax

        elif self.allow_None and val is None:
            return val

        else:
            # non-numeric value sent in: reverts to default value
            return self.value

        return val


class Integer(Number):
    """
    Integer class, allowing storing of `integer` objects
    """

    def __init__(self, value, kind="Integer", **kws):
        super(Integer, self).__init__(value=value, kind=kind, **kws)

        self.value = self._validate(self._value)

    def _validate(self, val):
        if self.allow_None and val is None:
            return

        if not isinstance(val, int):
            raise ValueError("Parameter '%s' must be an integer." % self.name)

        if self.auto_bound:
            val = self.crop_to_bounds(val)

        self._check_bounds(val)

        return val


class Boolean(Parameter):
    """
    Bool class, allowing storing of `boolean` objects
    """

    def __init__(self, value, kind="Boolean", **kws):
        super(Boolean, self).__init__(value=value, kind=kind, **kws)

        self.value = self._validate(self._value)

    def _validate(self, val):
        """
        Checks that the value is numeric and that it is within the hard
        bounds; if not, an exception is raised.
        """
        if self.allow_None:
            if not isinstance(val, bool) and val is not None:
                raise ValueError("Boolean '%s' only takes a Boolean value or None." % self.name)

            if val is not True and val is not False and val is not None:
                raise ValueError("Boolean '%s' must be True, False, or None." % self.name)
        else:
            if not isinstance(val, bool):
                raise ValueError("Boolean '%s' only takes a Boolean value." % self.name)

            if val is not True and val is not False:
                raise ValueError("Boolean '%s' must be True or False." % self.name)
        return val


class String(Parameter):
    """
    String class, allowing storing of `string` object
    """

    __slots__ = ["name", "doc", "_value", "allow_None", "allow_any", "saveable", "constant"]

    def __init__(self, value, kind="String", **kws):
        super(String, self).__init__(value=value, kind=kind, **kws)

        self.allow_any = kws.get("allow_any", False)
        self.value = self._validate(self._value)

    def _validate(self, val):
        """
        Checks that the value is string-like
        """
        if self.allow_None and val is None:
            return val

        if self.allow_any:
            return str(val)

        if not isinstance(val, str):
            raise ValueError("Parameter '%s' only takes string values" % (self.name))

        return val


class Color(Parameter):
    """
    Color parameter defined as a hex RGB string with an optional #
    prefix.
    """

    __slots__ = ["name", "doc", "_value", "saveable", "_kind", "allow_None", "constant"]

    def __init__(self, value=None, kind="Color", **kwargs):
        super(Color, self).__init__(value=value, allow_None=False, kind=kind, **kwargs)
        self._validate(value)

    def _validate(self, val):
        if self.allow_None and val is None:
            return
        if not isinstance(val, str):
            raise ValueError("Color '%s' only takes a string value." % self.name)
        if not re.match("^#?(([0-9a-fA-F]{2}){3}|([0-9a-fA-F]){3})$", val):
            raise ValueError("Color '%s' only accepts valid RGB hex codes." % self.name)


class Option(object):
    """
    Base class for `Choice` allowing specification of choices
    """

    __slots__ = ["name", "doc", "_value", "_choices", "saveable", "allow_None", "_kind", "constant"]

    def __init__(self, **kws):
        self.name = kws.get("name", "param")
        self.doc = kws.get("doc", "")
        self._value = kws.get("value", None)
        self._choices = kws.get("choices", [])
        self.allow_None = kws.get("allow_None", True)
        self.saveable = kws.get("saveable", True)
        self._kind = kws.get("kind", "Option")
        self.constant = kws.get("constant", False)

    def __repr__(self):
        return "Choice(name=%s, value=%s, choices=`%s`, doc='%s)" % (self.name, self.value, self.choices, self.doc)

    def _validate(self, val):
        """Implements validation for the parameter"""
        if val in self.choices:
            return val
        raise ValueError("Value `{}` not in the provided choices: {}".format(val, self.choices))

    def _validate_choices(self, val):
        """Ensure choices are a list"""
        if isinstance(val, list):
            return val
        raise ValueError("Choices must be a `list`")

    @property
    def value(self):
        """Get `value`"""
        return self._value

    @value.setter
    def value(self, value):
        """Set `value`"""
        self._value = self._validate(value)

    @property
    def choices(self):
        """Get `choices`"""
        return self._choices

    @choices.setter
    def choices(self, value):
        """Set `choices`"""
        self._choices = self._validate_choices(value)

    @property
    def kind(self):
        """Get `_kind`"""
        return self._kind

    @kind.setter
    def kind(self, value):
        """Set `_kind`"""
        self._kind = self._validate(value)


class Choice(Option):
    """
    Choice class, allowing specifying list of choices and default  value
    """

    def __init__(self, value, choices, kind="Choice", **kws):
        super(Choice, self).__init__(value=value, choices=choices, kind=kind, **kws)

        self._validate_choices(choices)
        self.value = self._validate(self._value)
