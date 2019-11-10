"""Test ParamStore pickling"""
import pickle

import simpleparam as param
from simpleparam.store import PROTECTED

ip_regex = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"


class Config(param.ParameterStore):
    def __init__(self):
        param.ParameterStore.__init__(self)
        self.param_int = param.Integer(value=666)
        self.param_num = param.Number(value=42.0)
        self.param_num_bounds = param.Number(value=42.0, hardbounds=[None, 105])
        self.param_color = param.Color(value="#FFF000")
        self.param_choice = param.Choice(value="boo", choices=["boo", "baa"])
        self.param_str = param.String("hello")
        self.param_regex = param.String(value="127.0.0.1", regex=ip_regex)
        self.param_bool = param.Boolean(False)
        self.param_option = param.Option(value=None, choices=[True, False])
        self.param_range = param.Range(value=[-100, 100], hardbounds=[-200, None])
        self.param_list = param.List(value=[1, 2, 3], hardbounds=[0, 10])


class TestParamStorePickle(object):
    """Test Boolean class"""

    @staticmethod
    def test_variables_pickle():
        """Test ParameterStore - correct initilization of constant"""

        config = Config()
        pkl_dump = pickle.dumps(config)
        pkl_cls = pickle.loads(pkl_dump)

        for attr_name in config.__dict__:
            config_obj = config.__dict__[attr_name]
            pkl_obj = pkl_cls.__dict__[attr_name]
            assert config_obj == pkl_obj
            # skip
            if attr_name in PROTECTED:
                continue

            for name in config_obj.__slots__:
                assert config_obj.__slots__.index(name) == pkl_obj.__slots__.index(name)
