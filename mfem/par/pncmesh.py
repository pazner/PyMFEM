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
            fp, pathname, description = imp.find_module('_pncmesh', [dirname(__file__)])
        except ImportError:
            import _pncmesh
            return _pncmesh
        if fp is not None:
            try:
                _mod = imp.load_module('_pncmesh', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pncmesh = swig_import_helper()
    del swig_import_helper
else:
    import _pncmesh
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
import ncmesh
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
import communication
import sets
class ParNCMesh(ncmesh.NCMesh):
    __swig_setmethods__ = {}
    for _s in [ncmesh.NCMesh]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ParNCMesh, name, value)
    __swig_getmethods__ = {}
    for _s in [ncmesh.NCMesh]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ParNCMesh, name)
    __repr__ = _swig_repr

    def __init__(self, comm, ncmesh):
        this = _pncmesh.new_ParNCMesh(comm, ncmesh)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _pncmesh.delete_ParNCMesh
    __del__ = lambda self: None

    def Refine(self, refinements):
        return _pncmesh.ParNCMesh_Refine(self, refinements)

    def LimitNCLevel(self, max_nc_level):
        return _pncmesh.ParNCMesh_LimitNCLevel(self, max_nc_level)

    def CheckDerefinementNCLevel(self, deref_table, level_ok, max_nc_level):
        return _pncmesh.ParNCMesh_CheckDerefinementNCLevel(self, deref_table, level_ok, max_nc_level)

    def Derefine(self, derefs):
        return _pncmesh.ParNCMesh_Derefine(self, derefs)

    def Rebalance(self):
        return _pncmesh.ParNCMesh_Rebalance(self)

    def GetSharedVertices(self):
        return _pncmesh.ParNCMesh_GetSharedVertices(self)

    def GetSharedEdges(self):
        return _pncmesh.ParNCMesh_GetSharedEdges(self)

    def GetSharedFaces(self):
        return _pncmesh.ParNCMesh_GetSharedFaces(self)

    def GetSharedList(self, type):
        return _pncmesh.ParNCMesh_GetSharedList(self, type)

    def GetFaceOrientation(self, index):
        return _pncmesh.ParNCMesh_GetFaceOrientation(self, index)

    def GetOwner(self, type, index):
        return _pncmesh.ParNCMesh_GetOwner(self, type, index)

    def GetGroup(self, type, index, size):
        return _pncmesh.ParNCMesh_GetGroup(self, type, index, size)

    def RankInGroup(self, type, index, rank):
        return _pncmesh.ParNCMesh_RankInGroup(self, type, index, rank)

    def IsGhost(self, type, index):
        return _pncmesh.ParNCMesh_IsGhost(self, type, index)

    def ElementRank(self, index):
        return _pncmesh.ParNCMesh_ElementRank(self, index)

    def GetFaceNeighbors(self, pmesh):
        return _pncmesh.ParNCMesh_GetFaceNeighbors(self, pmesh)

    def SendRebalanceDofs(self, old_ndofs, old_element_dofs, old_global_offset, space):
        return _pncmesh.ParNCMesh_SendRebalanceDofs(self, old_ndofs, old_element_dofs, old_global_offset, space)

    def RecvRebalanceDofs(self, elements, dofs):
        return _pncmesh.ParNCMesh_RecvRebalanceDofs(self, elements, dofs)

    def GetRebalanceOldIndex(self):
        return _pncmesh.ParNCMesh_GetRebalanceOldIndex(self)

    def GetDerefineOldRanks(self):
        return _pncmesh.ParNCMesh_GetDerefineOldRanks(self)

    def GetBoundaryClosure(self, bdr_attr_is_ess, bdr_vertices, bdr_edges):
        return _pncmesh.ParNCMesh_GetBoundaryClosure(self, bdr_attr_is_ess, bdr_vertices, bdr_edges)

    def GetDebugMesh(self, debug_mesh):
        return _pncmesh.ParNCMesh_GetDebugMesh(self, debug_mesh)
ParNCMesh_swigregister = _pncmesh.ParNCMesh_swigregister
ParNCMesh_swigregister(ParNCMesh)

class NeighborDofMessage(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NeighborDofMessage, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NeighborDofMessage, name)
    __repr__ = _swig_repr

    def AddDofs(self, type, id, dofs):
        return _pncmesh.NeighborDofMessage_AddDofs(self, type, id, dofs)

    def Init(self, pncmesh, fec, ndofs):
        return _pncmesh.NeighborDofMessage_Init(self, pncmesh, fec, ndofs)

    def GetDofs(self, type, id, dofs, ndofs):
        return _pncmesh.NeighborDofMessage_GetDofs(self, type, id, dofs, ndofs)

    def __init__(self):
        this = _pncmesh.new_NeighborDofMessage()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _pncmesh.delete_NeighborDofMessage
    __del__ = lambda self: None
NeighborDofMessage_swigregister = _pncmesh.NeighborDofMessage_swigregister
NeighborDofMessage_swigregister(NeighborDofMessage)

class NeighborRowRequest(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NeighborRowRequest, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NeighborRowRequest, name)
    __repr__ = _swig_repr
    __swig_setmethods__["rows"] = _pncmesh.NeighborRowRequest_rows_set
    __swig_getmethods__["rows"] = _pncmesh.NeighborRowRequest_rows_get
    if _newclass:
        rows = _swig_property(_pncmesh.NeighborRowRequest_rows_get, _pncmesh.NeighborRowRequest_rows_set)

    def RequestRow(self, row):
        return _pncmesh.NeighborRowRequest_RequestRow(self, row)

    def RemoveRequest(self, row):
        return _pncmesh.NeighborRowRequest_RemoveRequest(self, row)

    def __init__(self):
        this = _pncmesh.new_NeighborRowRequest()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _pncmesh.delete_NeighborRowRequest
    __del__ = lambda self: None
NeighborRowRequest_swigregister = _pncmesh.NeighborRowRequest_swigregister
NeighborRowRequest_swigregister(NeighborRowRequest)

class NeighborRowReply(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NeighborRowReply, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NeighborRowReply, name)
    __repr__ = _swig_repr

    def AddRow(self, row, cols, srow):
        return _pncmesh.NeighborRowReply_AddRow(self, row, cols, srow)

    def HaveRow(self, row):
        return _pncmesh.NeighborRowReply_HaveRow(self, row)

    def GetRow(self, row, cols, srow):
        return _pncmesh.NeighborRowReply_GetRow(self, row, cols, srow)

    def __init__(self):
        this = _pncmesh.new_NeighborRowReply()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _pncmesh.delete_NeighborRowReply
    __del__ = lambda self: None
NeighborRowReply_swigregister = _pncmesh.NeighborRowReply_swigregister
NeighborRowReply_swigregister(NeighborRowReply)


def __lt__(a, b):
    return _pncmesh.__lt__(a, b)
__lt__ = _pncmesh.__lt__
# This file is compatible with both classic and new-style classes.


