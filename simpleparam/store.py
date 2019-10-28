"""General class for storing parameters"""

PROTECTED = ["_name"]
N_PROTECTED = len(PROTECTED)


class ParameterStore(object):
    """Parameter store"""

    def __init__(self, name="ParameterStore"):
        """Parameter store

        Parameters
        ----------
        name : str, optional
            name of the parameters store, by default "ParameterStore"
        """

        self._name = name

    def __setattr__(self, name, val):
        if name in self.__dict__:
            if hasattr(self.__dict__[name], "value"):
                if hasattr(self.__dict__[name], "constant") and self.__dict__[name].constant:
                    raise ValueError("Parameter `%s` cannot be modified" % name)
                self.__dict__[name].value = val
        else:
            self.__dict__[name] = val

    def __repr__(self):
        return "{}(count={})".format(self._name, len(self.__dict__) - N_PROTECTED)

    def __str__(self):
        """Return a short representation of the name and class of this object."""
        return "<{} {}>".format(self.__class__.__name__, self._name)

    def __iter__(self):
        return iter(self.__dict__)

    def export_as_json(self):
        """Exports current instance as JSON dictionary"""
        _export = dict()

        for name, parameter in self.__dict__.items():
            # ignore reserved names
            if name in PROTECTED:
                continue

            # only export saveable objects
            if parameter.saveable:
                # base attributes of all parameters
                _export[name] = dict(
                    name=parameter.name,
                    value=parameter.value,
                    doc=parameter.doc,
                    kind=parameter.kind,
                    allow_None=parameter.allow_None,
                )
                # kind-specific attributes
                if parameter.kind in ["Number", "Integer"]:
                    _export[name].update(
                        dict(
                            auto_bound=parameter.auto_bound,
                            softbounds=parameter.softbounds,
                            hardbounds=parameter.hardbounds,
                            inclusive_bounds=parameter.inclusive_bounds,
                            step=parameter.step,
                            allow_None=parameter.allow_None,
                        )
                    )
                elif parameter.kind in ["String"]:
                    _export[name].update(dict(allow_any=parameter.allow_any, regex=parameter.regex))
                elif parameter.kind in ["Option", "Choice"]:
                    _export[name].update(dict(choices=parameter.choices))

        # return data
        return _export
