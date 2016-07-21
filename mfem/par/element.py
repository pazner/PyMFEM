# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_element', [dirname(__file__)])
        except ImportError:
            import _element
            return _element
        if fp is not None:
            try:
                _mod = imp.load_module('_element', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _element = swig_import_helper()
    del swig_import_helper
else:
    import _element
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


import array
import densemat
import vector
import operators
import matrix
import geom
import intrules
import table
class Element(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Element, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Element, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    POINT = _element.Element_POINT
    SEGMENT = _element.Element_SEGMENT
    TRIANGLE = _element.Element_TRIANGLE
    QUADRILATERAL = _element.Element_QUADRILATERAL
    TETRAHEDRON = _element.Element_TETRAHEDRON
    HEXAHEDRON = _element.Element_HEXAHEDRON

    def GetType(self):
        return _element.Element_GetType(self)

    def GetGeometryType(self):
        return _element.Element_GetGeometryType(self)

    def GetAttribute(self):
        return _element.Element_GetAttribute(self)

    def SetAttribute(self, attr):
        return _element.Element_SetAttribute(self, attr)

    def SetVertices(self, ind):
        return _element.Element_SetVertices(self, ind)

    def GetVertices(self, *args):
        return _element.Element_GetVertices(self, *args)

    def GetNVertices(self):
        return _element.Element_GetNVertices(self)

    def GetNEdges(self):
        return _element.Element_GetNEdges(self)

    def GetEdgeVertices(self, arg2):
        return _element.Element_GetEdgeVertices(self, arg2)

    def GetNFaces(self, nFaceVertices):
        return _element.Element_GetNFaces(self, nFaceVertices)

    def GetFaceVertices(self, fi):
        return _element.Element_GetFaceVertices(self, fi)

    def MarkEdge(self, *args):
        return _element.Element_MarkEdge(self, *args)

    def NeedRefinement(self, v_to_v, middle):
        return _element.Element_NeedRefinement(self, v_to_v, middle)

    def ResetTransform(self, tr):
        return _element.Element_ResetTransform(self, tr)

    def PushTransform(self, tr):
        return _element.Element_PushTransform(self, tr)

    def GetTransform(self):
        return _element.Element_GetTransform(self)

    def GetRefinementFlag(self):
        return _element.Element_GetRefinementFlag(self)

    def Duplicate(self, m):
        return _element.Element_Duplicate(self, m)
    __swig_destroy__ = _element.delete_Element
    __del__ = lambda self: None

    def GetVerticesArray(self):
        return _element.Element_GetVerticesArray(self)
Element_swigregister = _element.Element_swigregister
Element_swigregister(Element)

# This file is compatible with both classic and new-style classes.


