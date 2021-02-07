# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _sparsesmoothers
else:
    import _sparsesmoothers

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _sparsesmoothers.SWIG_PyInstanceMethod_New
_swig_new_static_method = _sparsesmoothers.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

import mfem._ser.vector
import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.operators
import mfem._ser.sparsemat
import mfem._ser.matrix
import mfem._ser.densemat
class SparseSmoother(mfem._ser.matrix.MatrixInverse):
    r"""Proxy of C++ mfem::SparseSmoother class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def SetOperator(self, a):
        r"""SetOperator(SparseSmoother self, Operator a)"""
        return _sparsesmoothers.SparseSmoother_SetOperator(self, a)
    SetOperator = _swig_new_instance_method(_sparsesmoothers.SparseSmoother_SetOperator)
    __swig_destroy__ = _sparsesmoothers.delete_SparseSmoother

# Register SparseSmoother in _sparsesmoothers:
_sparsesmoothers.SparseSmoother_swigregister(SparseSmoother)

class GSSmoother(SparseSmoother):
    r"""Proxy of C++ mfem::GSSmoother class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(GSSmoother self, int t=0, int it=1) -> GSSmoother
        __init__(GSSmoother self, SparseMatrix a, int t=0, int it=1) -> GSSmoother
        """
        _sparsesmoothers.GSSmoother_swiginit(self, _sparsesmoothers.new_GSSmoother(*args))

    def Mult(self, x, y):
        r"""Mult(GSSmoother self, Vector x, Vector y)"""
        return _sparsesmoothers.GSSmoother_Mult(self, x, y)
    Mult = _swig_new_instance_method(_sparsesmoothers.GSSmoother_Mult)
    __swig_destroy__ = _sparsesmoothers.delete_GSSmoother

# Register GSSmoother in _sparsesmoothers:
_sparsesmoothers.GSSmoother_swigregister(GSSmoother)

class DSmoother(SparseSmoother):
    r"""Proxy of C++ mfem::DSmoother class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(DSmoother self, int t=0, double s=1., int it=1) -> DSmoother
        __init__(DSmoother self, SparseMatrix a, int t=0, double s=1., int it=1) -> DSmoother
        """
        _sparsesmoothers.DSmoother_swiginit(self, _sparsesmoothers.new_DSmoother(*args))

    def Mult(self, x, y):
        r"""Mult(DSmoother self, Vector x, Vector y)"""
        return _sparsesmoothers.DSmoother_Mult(self, x, y)
    Mult = _swig_new_instance_method(_sparsesmoothers.DSmoother_Mult)
    __swig_destroy__ = _sparsesmoothers.delete_DSmoother

# Register DSmoother in _sparsesmoothers:
_sparsesmoothers.DSmoother_swigregister(DSmoother)


