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
            fp, pathname, description = imp.find_module('_ncmesh', [dirname(__file__)])
        except ImportError:
            import _ncmesh
            return _ncmesh
        if fp is not None:
            try:
                _mod = imp.load_module('_ncmesh', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ncmesh = swig_import_helper()
    del swig_import_helper
else:
    import _ncmesh
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


try:
    import weakref
    weakref_proxy = weakref.proxy
except Exception:
    weakref_proxy = lambda x: x


import mesh
import matrix
import vector
import array
import operators
import element
import densemat
import geom
import intrules
import table
import vertex
import sparsemat
import eltrans
import fe
import coefficient
class Refinement(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Refinement, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Refinement, name)
    __repr__ = _swig_repr
    __swig_setmethods__["index"] = _ncmesh.Refinement_index_set
    __swig_getmethods__["index"] = _ncmesh.Refinement_index_get
    if _newclass:
        index = _swig_property(_ncmesh.Refinement_index_get, _ncmesh.Refinement_index_set)
    __swig_setmethods__["ref_type"] = _ncmesh.Refinement_ref_type_set
    __swig_getmethods__["ref_type"] = _ncmesh.Refinement_ref_type_get
    if _newclass:
        ref_type = _swig_property(_ncmesh.Refinement_ref_type_get, _ncmesh.Refinement_ref_type_set)

    def __init__(self, index, type=7):
        this = _ncmesh.new_Refinement(index, type)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _ncmesh.delete_Refinement
    __del__ = lambda self: None
Refinement_swigregister = _ncmesh.Refinement_swigregister
Refinement_swigregister(Refinement)

class Embedding(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Embedding, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Embedding, name)
    __repr__ = _swig_repr
    __swig_setmethods__["parent"] = _ncmesh.Embedding_parent_set
    __swig_getmethods__["parent"] = _ncmesh.Embedding_parent_get
    if _newclass:
        parent = _swig_property(_ncmesh.Embedding_parent_get, _ncmesh.Embedding_parent_set)
    __swig_setmethods__["matrix"] = _ncmesh.Embedding_matrix_set
    __swig_getmethods__["matrix"] = _ncmesh.Embedding_matrix_get
    if _newclass:
        matrix = _swig_property(_ncmesh.Embedding_matrix_get, _ncmesh.Embedding_matrix_set)

    def __init__(self, elem, matrix=0):
        this = _ncmesh.new_Embedding(elem, matrix)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _ncmesh.delete_Embedding
    __del__ = lambda self: None
Embedding_swigregister = _ncmesh.Embedding_swigregister
Embedding_swigregister(Embedding)

class CoarseFineTransformations(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CoarseFineTransformations, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CoarseFineTransformations, name)
    __repr__ = _swig_repr
    __swig_setmethods__["point_matrices"] = _ncmesh.CoarseFineTransformations_point_matrices_set
    __swig_getmethods__["point_matrices"] = _ncmesh.CoarseFineTransformations_point_matrices_get
    if _newclass:
        point_matrices = _swig_property(_ncmesh.CoarseFineTransformations_point_matrices_get, _ncmesh.CoarseFineTransformations_point_matrices_set)
    __swig_getmethods__["embeddings"] = _ncmesh.CoarseFineTransformations_embeddings_get
    if _newclass:
        embeddings = _swig_property(_ncmesh.CoarseFineTransformations_embeddings_get)

    def __init__(self):
        this = _ncmesh.new_CoarseFineTransformations()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _ncmesh.delete_CoarseFineTransformations
    __del__ = lambda self: None
CoarseFineTransformations_swigregister = _ncmesh.CoarseFineTransformations_swigregister
CoarseFineTransformations_swigregister(CoarseFineTransformations)

class NCMesh(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NCMesh, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NCMesh, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _ncmesh.new_NCMesh(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _ncmesh.delete_NCMesh
    __del__ = lambda self: None

    def Dimension(self):
        return _ncmesh.NCMesh_Dimension(self)

    def SpaceDimension(self):
        return _ncmesh.NCMesh_SpaceDimension(self)

    def Refine(self, refinements):
        return _ncmesh.NCMesh_Refine(self, refinements)

    def LimitNCLevel(self, max_nc_level):
        return _ncmesh.NCMesh_LimitNCLevel(self, max_nc_level)

    def GetDerefinementTable(self):
        return _ncmesh.NCMesh_GetDerefinementTable(self)

    def CheckDerefinementNCLevel(self, deref_table, level_ok, max_nc_level):
        return _ncmesh.NCMesh_CheckDerefinementNCLevel(self, deref_table, level_ok, max_nc_level)

    def Derefine(self, derefs):
        return _ncmesh.NCMesh_Derefine(self, derefs)

    def GetFaceList(self):
        return _ncmesh.NCMesh_GetFaceList(self)

    def GetEdgeList(self):
        return _ncmesh.NCMesh_GetEdgeList(self)

    def MarkCoarseLevel(self):
        return _ncmesh.NCMesh_MarkCoarseLevel(self)

    def GetRefinementTransforms(self):
        return _ncmesh.NCMesh_GetRefinementTransforms(self)

    def GetDerefinementTransforms(self):
        return _ncmesh.NCMesh_GetDerefinementTransforms(self)

    def ClearTransforms(self):
        return _ncmesh.NCMesh_ClearTransforms(self)

    def GetEdgeMaster(self, v1, v2):
        return _ncmesh.NCMesh_GetEdgeMaster(self, v1, v2)

    def GetBoundaryClosure(self, bdr_attr_is_ess, bdr_vertices, bdr_edges):
        return _ncmesh.NCMesh_GetBoundaryClosure(self, bdr_attr_is_ess, bdr_vertices, bdr_edges)

    def GetElementGeometry(self):
        return _ncmesh.NCMesh_GetElementGeometry(self)

    def GetElementDepth(self, i):
        return _ncmesh.NCMesh_GetElementDepth(self, i)

    def PrintVertexParents(self, out):
        return _ncmesh.NCMesh_PrintVertexParents(self, out)

    def PrintCoarseElements(self, out):
        return _ncmesh.NCMesh_PrintCoarseElements(self, out)

    def LoadVertexParents(self, input):
        return _ncmesh.NCMesh_LoadVertexParents(self, input)

    def LoadCoarseElements(self, input):
        return _ncmesh.NCMesh_LoadCoarseElements(self, input)

    def SetVertexPositions(self, vertices):
        return _ncmesh.NCMesh_SetVertexPositions(self, vertices)

    def MemoryUsage(self):
        return _ncmesh.NCMesh_MemoryUsage(self)

    def PrintMemoryDetail(self):
        return _ncmesh.NCMesh_PrintMemoryDetail(self)
    __swig_setmethods__["GI"] = _ncmesh.NCMesh_GI_set
    __swig_getmethods__["GI"] = _ncmesh.NCMesh_GI_get
    if _newclass:
        GI = _swig_property(_ncmesh.NCMesh_GI_get, _ncmesh.NCMesh_GI_set)
NCMesh_swigregister = _ncmesh.NCMesh_swigregister
NCMesh_swigregister(NCMesh)
cvar = _ncmesh.cvar

# This file is compatible with both classic and new-style classes.


