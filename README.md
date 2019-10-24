# SimpleParam

A simplified copycat of the [param](https://param.pyviz.org/) library.

This library is certainly incomplete and is missing a lot of the awesome features of `param`, however, provides a nice
starting point.

## Usage

You can intilize `Parameter` like this:

```python
import simpleparam as param

number = param.Number(42)
number

>>> Parameter(name=param, value=42, doc=')
```

However, it is probably better to use parameters inside of a `ParameterStore`, where you can store multiple parameters together and take advantage of additional functionality (e.g. locking of parameters with `constant` or exporting parameters as JSON object using `export_as_json`):

```python
import simpleparam as param

class Config(param.ParameterStore):
    def __init__(self):
        sp.ParameterStore.**init**(self)

        # # you can add parameter docstrings by setting `doc`
        self.integer = param.Integer(42,
                                     doc="A not very important value")
        # `auto_bound` forces hard bounds on values that are outside the specification
        self.number = param.Number(42.,
                                   softbounds=[0, 100],
                                   hardbounds=[1, 100],
                                   auto_bound=True)
        # setting `allow_any` to False, will force values to be of `str` instance
        self.string = param.String("string",
                                   allow_any=False)
        # you can set internal parameter name by setting the value of `name`
        self.choice = param.Choice("foo",
                                   name="foo_bar_choice",
                                   choices=["foo", "bar"],
                                   )
        # parameters can be prevented from being changed by setting value of `constant
        self.color = param.Color("#FFFFFF",
                                 constant=True)
        self.bool = param.Bool(True)

config = Config()
config

>>> ParameterStore(count=6)
```

`ParameterStore` can be exported as JSON dictionary by simply calling `config.export_as_json()` to give:

```python
>>> {
'integer': {'name': 'param',
  'value': 42,
  'doc': 'A not very important value',
  'softbounds': None,
  'hardbounds': None,
  'kind': 'Integer'},
 'number': {'name': 'param',
  'value': 42.0,
  'doc': '',
  'softbounds': [0, 100],
  'hardbounds': [1, 100],
  'kind': 'Number'},
 'string': {'name': 'param', 'value': 'string', 'doc': '', 'kind': 'String'},
 'choice': {'name': 'foo_bar_choice',
  'value': 'foo',
  'doc': '',
  'choices': ['foo', 'bar'],
  'kind': 'Choice'},
 'color': {'name': 'param', 'value': '#FFFFFF', 'doc': '', 'kind': 'Color'},
 'bool': {'name': 'param', 'value': True, 'doc': '', 'kind': 'Bool'}
 }
```
