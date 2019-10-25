"""General class for storing parameters"""

PROTECTED = ["_name"]


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
        return "{}(count={})".format(self._name, len(self.__dict__) - len(PROTECTED))

    def __iter__(self):
        return iter(self.__dict__)

    def items(self):
        """Return dictionary items"""
        return self.__dict__.items()

    def values(self):
        """Return dictionary values"""
        return self.__dict__.values()

    def export_as_json(self):
        """Exports current instance as JSON dictionary"""
        _export = dict()

        for name, parameter in self.items():
            # ignore reserved names
            if name in PROTECTED:
                continue

            # only export saveable objects
            if parameter.saveable:
                # kind-specific actions
                if parameter.kind in ["Parameter", "Number", "Integer"]:
                    _export[name] = dict(
                        name=parameter.name,
                        value=parameter.value,
                        doc=parameter.doc,
                        softbounds=parameter.softbounds,
                        hardbounds=parameter.hardbounds,
                        kind=parameter.kind,
                    )
                elif parameter.kind in ["Bool", "String", "Color"]:
                    _export[name] = dict(
                        name=parameter.name, value=parameter.value, doc=parameter.doc, kind=parameter.kind
                    )
                elif parameter.kind in ["Option", "Choice"]:
                    _export[name] = dict(
                        name=parameter.name,
                        value=parameter.value,
                        doc=parameter.doc,
                        choices=parameter.choices,
                        kind=parameter.kind,
                    )

        # return data
        return _export
