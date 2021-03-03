import numpy as np

from . import backends
from . import blas
from . import helpers
from . import parser
from . import paths


def contract_path(*operands, **kwargs):
    valid_contract_kwargs = ['path', 'memory_limit', 'einsum_call', 'use_blas']
    unknown_kwargs = [k for (k, v) in kwargs.items() if k not in valid_contract_kwargs]
    if len(unknown_kwargs):
        raise TypeError("einsum_path: Did not understand the following kwargs: %s" % unknown_kwargs)

    path_type = kwargs.pop('path', 'greedy')
    memory_limit = kwargs.pop('memory_limit', None)

    # Hidden option, only einsum should call this
    einsum_call_arg = kwargs.pop("einsum_call", False)
    use_blas = kwargs.pop('use_blas', True)

    # Python side parsing
    input_subscripts, output_subscript, operands = parser.parse_einsum_input(operands)

    # Build a few useful list and sets
    input_list = input_subscripts.split(',')
    input_sets = [set(x) for x in input_list]
    output_set = set(output_subscript)
    indices = set(input_subscripts.replace(',', ''))


def _einsum(*operands, **kwargs):
    """Base einsum, but with pre-parse for valid characters if string given.
    """
    fn = backends.get_func('einsum', kwargs.pop('backend', 'numpy'))

    if not isinstance(operands[0], str):
        return fn(*operands, **kwargs)

    einsum_str, operands = operands[0], operands[1:]

    # Do we need to temporarily map indices into [a-z,A-Z] range?
    if not parser.has_valid_einsum_chars_only(einsum_str):

        # Explicitly find output str first so as to maintain order
        if '->' not in einsum_str:
            einsum_str += '->' + parser.find_output_str(einsum_str)

        einsum_str = parser.convert_to_valid_einsum_chars(einsum_str)

    return fn(einsum_str, *operands, **kwargs)

class ContractExpression1:
    """Helper class for storing an explicit ``contraction_list`` which can
    then be repeatedly called solely with the array arguments.
    """

    def __init__(self, contraction, contraction_list, constants_dict, **einsum_kwargs):
        self.contraction = contraction
        self.contraction_list = contraction_list
        self.einsum_kwargs = einsum_kwargs
        self.num_args = len(contraction_list[0][0]) + len(contraction_list[0][3]) - 1
        self.constants = None

        # perform as much of the contraction as possible if constants supplied
        if constants_dict:
            tmp_const_ops = [constants_dict.get(i, None) for i in range(self.num_args)]
            new_ops, new_contraction_list = self(*tmp_const_ops, parse_constants=True)
            self.contraction = format_const_einsum_str(contraction, constants_dict.keys())
            self.num_args -= len(constants_dict)
            self.contraction_list = new_contraction_list
            self.constants = new_ops

    def _normal_contract(self, arrays, out=None, backend='numpy', parse_constants=False):
        """The normal, core contraction.
        """
        return _core_contract(list(arrays), self.contraction_list, out=out, backend=backend,
                              parse_constants=parse_constants, **self.einsum_kwargs)

    def _convert_contract(self, arrays, out, backend, parse_constants=False):
        """Special contraction, i.e. contraction with a different backend
        but converting to and from that backend. Checks for
        ``self._{backend}_contract``, generates it if is missing, then calls it
        with ``arrays``.
        """
        convert_fn = "_{}_contract".format(backend)

        if not hasattr(self, convert_fn):
            setattr(self, convert_fn, backends.build_expression(backend, arrays, self))

        result = getattr(self, convert_fn)(*arrays)

        if out is not None:
            out[()] = result
            return out

        return result


class ContractExpression2:
    """Helper class for storing an explicit ``contraction_list`` which can
    then be repeatedly called solely with the array arguments.
    """

    def __init__(self, contraction, contraction_list, constants_dict, **einsum_kwargs):
        self.contraction = contraction
        self.contraction_list = contraction_list
        self.einsum_kwargs = einsum_kwargs
        self.num_args = len(contraction_list[0][0]) + len(contraction_list[0][3]) - 1
        self.constants = None

        # perform as much of the contraction as possible if constants supplied
        if constants_dict:
            tmp_const_ops = [constants_dict.get(i, None) for i in range(self.num_args)]
            new_ops, new_contraction_list = self(*tmp_const_ops, parse_constants=True)
            self.contraction = format_const_einsum_str(contraction, constants_dict.keys())
            self.num_args -= len(constants_dict)
            self.contraction_list = new_contraction_list
            self.constants = new_ops

    def _normal_contract(self, arrays, out=None, backend='numpy', parse_constants=False):
        """The normal, core contraction.
        """
        return _core_contract(list(arrays), self.contraction_list, out=out, backend=backend,
                              parse_constants=parse_constants, **self.einsum_kwargs)

    def _convert_contract(self, arrays, out, backend, parse_constants=False):
        """Special contraction, i.e. contraction with a different backend
        but converting to and from that backend. Checks for
        ``self._{backend}_contract``, generates it if is missing, then calls it
        with ``arrays``.
        """
        convert_fn = "_{}_contract".format(backend)

        if not hasattr(self, convert_fn):
            setattr(self, convert_fn, backends.build_expression(backend, arrays, self))

        result = getattr(self, convert_fn)(*arrays)

        if out is not None:
            out[()] = result
            return out

        return result

