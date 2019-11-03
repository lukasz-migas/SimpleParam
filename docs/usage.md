# Usage

## Parameter

Each parameter has certain attributes associated with it, which can simplify creation of self-explanatory parameters. For instance, in a GUI application a widget (e.g. number input) would require a tooltip, which if defined as a `Parameter` could be included in the `doc` attribute.

You can initilize individual `Parameter` using simple synthax:

```python
import simpleparam as param

number = param.Number(42, doc="I am the answer")
number
>>> 42

number.doc
"I am the answer"
```

### Value, range and type checking

Before any value is set, it is validated against its class characteristics (e.g. Integer -> all values must be integers).

```python
number = param.Number("42")
[ ... ]
>>> ValueError: Parameter 'param' only takes numeric values

integer = param.Integer(1.0)
[ ... ]
>>> ValueError: Parameter 'param' must be an integer not '<class 'float'>'

value = param.Range([1], hardbounds=[0, 100])
[ ... ]
>>> ValueError: Range parameter 'param' must have two values

color = param.Color("#FFFF")
[ ... ]
>>> ValueError: Color 'param' only accepts valid RGB hex codes.

value = param.Boolean(2)
[ ... ]
ValueError: Boolean 'param' only takes a Boolean value or None.
```

Built-in range-checking

```python
number = param.Number(42, hardbounds=[0, 41])
[ ... ]
>>> ValueError: Parameter 'param' must be at most 41
```

Which can be relaxed to allow value correction if its set outside of the hard boundary

```python
number = param.Number(42, hardbounds=[0, 41], auto_bound=True)
number
>>> 41
number = param.Number(42, hardbounds=[0, None], auto_bound=True)
number
>>> 42
```

Range checking is also performed in the `Range` parameter where each value is checked against the `hardbounds`

```python
number = param.Range([0, 100], hardbounds=[0, 100])
number.value = [-1, 100]
[ ... ]
>>> ValueError: Parameter 'param' must be at least 0
```

When creating `Choice`, any value to be set after it has been initilized will be checked against set choices

```python
choice = param.Choice("Hello", choices=["Hello", "World"])
choice.value = "Goodbye"
[ ... ]
>>> ValueError: Value `Goodbye` not in the provided choices: ['Hello', 'World']
```

Choices can be updated of course

```python
choice = param.Choice("Hello", choices=["Hello", "World"])
choice.choices = ["Hello", "World", "Goodbye"]
choice.value = "Goodbye"
choice
>>> "Goodbye"
```

### Operations

You can do the typical numerical operations on each parameter:

```python
number.value += 6
number
>>> 48

number.value /= 4
number
>>>  12.0
```

!!! Important
    When using `Parameter` outside of the `ParameterStore`, operations such as addition, subtraction, etc must be performed on the `value` attribute of the variable, otherwise it will be overwritten by the new value.

```python
number = param.Number(42, doc="I am the answer")
print(type(number))
number.value += 1
print(type(number))
>>> <class 'simpleparam.Number'>
>>> <class 'simpleparam.Number'>
```

and not

```python
number = param.Number(42, doc="I am the answer")
print(type(number))
number += 1
print(type(number))
>>> <class 'simpleparam.Number'>
>>> <class 'int'>
```

## ParameterStore

However, it is probably better to use parameters inside of a `ParameterStore`, where you can store multiple parameters together and take advantage of additioncal functionality (e.g. locking of parameters by setting them as `constant`, marking parameters as `saveable` or quickly generating self-explenatory JSON configuration files by using the `export_as_json` file).

### Creation

```python
import simpleparam as param

class Config(param.ParameterStore):
    def __init__(self):
        super(Config, self).__init__()

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
        self.bool = param.Boolean(True)
        self.range = param.Range(value=[0, 100], hardbounds=[0, 100])

config = Config()
config

>>> ParameterStore(count=7)
```

### Exporting to dictionary

`ParameterStore` can be exported as JSON dictionary by simply calling `config.export_as_dict()` to give:

```python
export_dict = config.export_as_dict()
export_dict
>>> {
{'integer': {'name': 'param',
  'value': 42,
  'doc': 'A not very important value',
  'kind': 'Integer',
  'allow_None': True,
  'auto_bound': False,
  'softbounds': None,
  'hardbounds': None,
  'inclusive_bounds': [True, True],
  'step': None},
 'number': {'name': 'param',
  'value': 42.0,
  'doc': '',
  'kind': 'Number',
  'allow_None': True,
  'auto_bound': True,
  'softbounds': [0, 100],
  'hardbounds': [1, 100],
  'inclusive_bounds': [True, True],
  'step': None},
 'string': {'name': 'param',
  'value': 'string',
  'doc': '',
  'kind': 'String',
  'allow_None': True,
  'allow_any': False,
  'regex': None},
 'choice': {'name': 'foo_bar_choice',
  'value': 'foo',
  'doc': '',
  'kind': 'Choice',
  'allow_None': True,
  'choices': ['foo', 'bar']},
 'color': {'name': 'param',
  'value': '#FFFFFF',
  'doc': '',
  'kind': 'Color'},
 'bool': {'name': 'param',
  'value': True,
  'doc': '',
  'kind': 'Boolean',
  'allow_None': True},
 'range': {'name': 'param',
  'value': [0, 100],
  'doc': '',
  'kind': 'Range',
  'allow_None': True,
  'auto_bound': False,
  'softbounds': None,
  'hardbounds': [0, 100],
  'inclusive_bounds': [True, True],
  'step': None}}
```

### Importing from dictionary

which can be later read-in by using the `config.load_from_dict(export_dict)`. Of course, if any value was changed in the `export_dict` object, this will be reflected in the instance of `Config`

```python
class Config(param.ParameterStore):
    def __init__(self):
        super(Config, self).__init__()
        self.integer = param.Integer(42)

config = Config()
config.integer = 103
output = config.export_as_dict()
output
>>>
{'integer': {'name': 'param',
  'value': 199,  # lets change the value
  'doc': 'Lets change the documentation also',  # and add some documentation
  'kind': 'Integer',
  'allow_None': True,
  'auto_bound': False,
  'softbounds': None,
  'hardbounds': None,
  'inclusive_bounds': [True, True],
  'step': None}}
```

and now lets load it to see the changes

```python
config = Config()
config.load_from_dict(output)
print(config.integer, config.integer.doc)
>>> 199 'Lets change the documentation also'
```

If you want to preserve certain values, for instance `doc`, you can set the value of `ignored_attributes=['doc']` which will ensure that the value of `doc` is not overwritten when loading data from a dictionary.

```python
config = Config()
config.load_from_dict(output, ignored_attributes=['doc'])
print(config.integer, config.integer.doc)
>>> 199 ''
```

You can also specify which value you want to load, for instance you only want to update the value of `doc` while keeping everything else unchanged. To do this, you can specify the `allowed_attributes=['doc']`.

```python
config = Config()
config.load_from_dict(output, allowed_attributes=['doc'])
print(config.integer, config.integer.doc)
>>> 42 Lets change the documentation also
```

!!! Important
    You cannot specify both `allowed_attributes` and `ignored_attributes`. This will result in an error.
