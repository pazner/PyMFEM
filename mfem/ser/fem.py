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
            fp, pathname, description = imp.find_module('_fem', [dirname(__file__)])
        except ImportError:
            import _fem
            return _fem
        if fp is not None:
            try:
                _mod = imp.load_module('_fem', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _fem = swig_import_helper()
    del swig_import_helper
else:
    import _fem
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


class Ordering(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Ordering, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Ordering, name)
    __repr__ = _swig_repr
    byNODES = _fem.Ordering_byNODES
    byVDIM = _fem.Ordering_byVDIM

    def __init__(self):
        this = _fem.new_Ordering()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _fem.delete_Ordering
    __del__ = lambda self: None
Ordering_swigregister = _fem.Ordering_swigregister
Ordering_swigregister(Ordering)

class RefinementData(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RefinementData, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RefinementData, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _fem.RefinementData_type_set
    __swig_getmethods__["type"] = _fem.RefinementData_type_get
    if _newclass:
        type = _swig_property(_fem.RefinementData_type_get, _fem.RefinementData_type_set)
    __swig_setmethods__["num_fine_elems"] = _fem.RefinementData_num_fine_elems_set
    __swig_getmethods__["num_fine_elems"] = _fem.RefinementData_num_fine_elems_get
    if _newclass:
        num_fine_elems = _swig_property(_fem.RefinementData_num_fine_elems_get, _fem.RefinementData_num_fine_elems_set)
    __swig_setmethods__["num_fine_dofs"] = _fem.RefinementData_num_fine_dofs_set
    __swig_getmethods__["num_fine_dofs"] = _fem.RefinementData_num_fine_dofs_get
    if _newclass:
        num_fine_dofs = _swig_property(_fem.RefinementData_num_fine_dofs_get, _fem.RefinementData_num_fine_dofs_set)
    __swig_setmethods__["fl_to_fc"] = _fem.RefinementData_fl_to_fc_set
    __swig_getmethods__["fl_to_fc"] = _fem.RefinementData_fl_to_fc_get
    if _newclass:
        fl_to_fc = _swig_property(_fem.RefinementData_fl_to_fc_get, _fem.RefinementData_fl_to_fc_set)
    __swig_setmethods__["I"] = _fem.RefinementData_I_set
    __swig_getmethods__["I"] = _fem.RefinementData_I_get
    if _newclass:
        I = _swig_property(_fem.RefinementData_I_get, _fem.RefinementData_I_set)
    __swig_destroy__ = _fem.delete_RefinementData
    __del__ = lambda self: None

    def __init__(self):
        this = _fem.new_RefinementData()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
RefinementData_swigregister = _fem.RefinementData_swigregister
RefinementData_swigregister(RefinementData)

class FiniteElementSpace(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FiniteElementSpace, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FiniteElementSpace, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _fem.new_FiniteElementSpace(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def GetMesh(self):
        return _fem.FiniteElementSpace_GetMesh(self)

    def GetNURBSext(self):
        return _fem.FiniteElementSpace_GetNURBSext(self)

    def StealNURBSext(self):
        return _fem.FiniteElementSpace_StealNURBSext(self)

    def Conforming(self):
        return _fem.FiniteElementSpace_Conforming(self)

    def Nonconforming(self):
        return _fem.FiniteElementSpace_Nonconforming(self)

    def GetConformingProlongation(self):
        return _fem.FiniteElementSpace_GetConformingProlongation(self)

    def GetConformingRestriction(self):
        return _fem.FiniteElementSpace_GetConformingRestriction(self)

    def GetRestrictionMatrix(self):
        return _fem.FiniteElementSpace_GetRestrictionMatrix(self)

    def GetVDim(self):
        return _fem.FiniteElementSpace_GetVDim(self)

    def GetOrder(self, i):
        return _fem.FiniteElementSpace_GetOrder(self, i)

    def GetFaceOrder(self, i):
        return _fem.FiniteElementSpace_GetFaceOrder(self, i)

    def GetNDofs(self):
        return _fem.FiniteElementSpace_GetNDofs(self)

    def GetVSize(self):
        return _fem.FiniteElementSpace_GetVSize(self)

    def GetTrueVSize(self):
        return _fem.FiniteElementSpace_GetTrueVSize(self)

    def GetNConformingDofs(self):
        return _fem.FiniteElementSpace_GetNConformingDofs(self)

    def GetConformingVSize(self):
        return _fem.FiniteElementSpace_GetConformingVSize(self)

    def GetOrdering(self):
        return _fem.FiniteElementSpace_GetOrdering(self)

    def FEColl(self):
        return _fem.FiniteElementSpace_FEColl(self)

    def GetNVDofs(self):
        return _fem.FiniteElementSpace_GetNVDofs(self)

    def GetNEDofs(self):
        return _fem.FiniteElementSpace_GetNEDofs(self)

    def GetNFDofs(self):
        return _fem.FiniteElementSpace_GetNFDofs(self)

    def GetNE(self):
        return _fem.FiniteElementSpace_GetNE(self)

    def GetNV(self):
        return _fem.FiniteElementSpace_GetNV(self)

    def GetNBE(self):
        return _fem.FiniteElementSpace_GetNBE(self)

    def GetElementType(self, i):
        return _fem.FiniteElementSpace_GetElementType(self, i)

    def GetElementVertices(self, i, vertices):
        return _fem.FiniteElementSpace_GetElementVertices(self, i, vertices)

    def GetBdrElementType(self, i):
        return _fem.FiniteElementSpace_GetBdrElementType(self, i)

    def GetElementTransformation(self, *args):
        return _fem.FiniteElementSpace_GetElementTransformation(self, *args)

    def GetBdrElementTransformation(self, i):
        return _fem.FiniteElementSpace_GetBdrElementTransformation(self, i)

    def GetAttribute(self, i):
        return _fem.FiniteElementSpace_GetAttribute(self, i)

    def GetBdrAttribute(self, i):
        return _fem.FiniteElementSpace_GetBdrAttribute(self, i)

    def GetElementDofs(self, i, dofs):
        return _fem.FiniteElementSpace_GetElementDofs(self, i, dofs)

    def GetBdrElementDofs(self, i, dofs):
        return _fem.FiniteElementSpace_GetBdrElementDofs(self, i, dofs)

    def GetFaceDofs(self, i, dofs):
        return _fem.FiniteElementSpace_GetFaceDofs(self, i, dofs)

    def GetEdgeDofs(self, i, dofs):
        return _fem.FiniteElementSpace_GetEdgeDofs(self, i, dofs)

    def GetVertexDofs(self, i, dofs):
        return _fem.FiniteElementSpace_GetVertexDofs(self, i, dofs)

    def GetElementInteriorDofs(self, i, dofs):
        return _fem.FiniteElementSpace_GetElementInteriorDofs(self, i, dofs)

    def GetNumElementInteriorDofs(self, i):
        return _fem.FiniteElementSpace_GetNumElementInteriorDofs(self, i)

    def GetEdgeInteriorDofs(self, i, dofs):
        return _fem.FiniteElementSpace_GetEdgeInteriorDofs(self, i, dofs)

    def DofsToVDofs(self, *args):
        return _fem.FiniteElementSpace_DofsToVDofs(self, *args)

    def DofToVDof(self, dof, vd, ndofs=-1):
        return _fem.FiniteElementSpace_DofToVDof(self, dof, vd, ndofs)

    def VDofToDof(self, vdof):
        return _fem.FiniteElementSpace_VDofToDof(self, vdof)
    __swig_getmethods__["AdjustVDofs"] = lambda x: _fem.FiniteElementSpace_AdjustVDofs
    if _newclass:
        AdjustVDofs = staticmethod(_fem.FiniteElementSpace_AdjustVDofs)

    def GetElementVDofs(self, i, vdofs):
        return _fem.FiniteElementSpace_GetElementVDofs(self, i, vdofs)

    def GetBdrElementVDofs(self, i, vdofs):
        return _fem.FiniteElementSpace_GetBdrElementVDofs(self, i, vdofs)

    def GetFaceVDofs(self, i, vdofs):
        return _fem.FiniteElementSpace_GetFaceVDofs(self, i, vdofs)

    def GetEdgeVDofs(self, i, vdofs):
        return _fem.FiniteElementSpace_GetEdgeVDofs(self, i, vdofs)

    def GetVertexVDofs(self, i, vdofs):
        return _fem.FiniteElementSpace_GetVertexVDofs(self, i, vdofs)

    def GetElementInteriorVDofs(self, i, vdofs):
        return _fem.FiniteElementSpace_GetElementInteriorVDofs(self, i, vdofs)

    def GetEdgeInteriorVDofs(self, i, vdofs):
        return _fem.FiniteElementSpace_GetEdgeInteriorVDofs(self, i, vdofs)

    def BuildElementToDofTable(self):
        return _fem.FiniteElementSpace_BuildElementToDofTable(self)

    def BuildDofToArrays(self):
        return _fem.FiniteElementSpace_BuildDofToArrays(self)

    def GetElementToDofTable(self):
        return _fem.FiniteElementSpace_GetElementToDofTable(self)

    def GetBdrElementToDofTable(self):
        return _fem.FiniteElementSpace_GetBdrElementToDofTable(self)

    def GetElementForDof(self, i):
        return _fem.FiniteElementSpace_GetElementForDof(self, i)

    def GetLocalDofForDof(self, i):
        return _fem.FiniteElementSpace_GetLocalDofForDof(self, i)

    def GetFE(self, i):
        return _fem.FiniteElementSpace_GetFE(self, i)

    def GetBE(self, i):
        return _fem.FiniteElementSpace_GetBE(self, i)

    def GetFaceElement(self, i):
        return _fem.FiniteElementSpace_GetFaceElement(self, i)

    def GetEdgeElement(self, i):
        return _fem.FiniteElementSpace_GetEdgeElement(self, i)

    def GetTraceElement(self, i, geom_type):
        return _fem.FiniteElementSpace_GetTraceElement(self, i, geom_type)

    def GetEssentialVDofs(self, bdr_attr_is_ess, ess_vdofs):
        return _fem.FiniteElementSpace_GetEssentialVDofs(self, bdr_attr_is_ess, ess_vdofs)

    def GetEssentialTrueDofs(self, bdr_attr_is_ess, ess_tdof_list):
        return _fem.FiniteElementSpace_GetEssentialTrueDofs(self, bdr_attr_is_ess, ess_tdof_list)
    __swig_getmethods__["MarkerToList"] = lambda x: _fem.FiniteElementSpace_MarkerToList
    if _newclass:
        MarkerToList = staticmethod(_fem.FiniteElementSpace_MarkerToList)
    __swig_getmethods__["ListToMarker"] = lambda x: _fem.FiniteElementSpace_ListToMarker
    if _newclass:
        ListToMarker = staticmethod(_fem.FiniteElementSpace_ListToMarker)

    def ConvertToConformingVDofs(self, dofs, cdofs):
        return _fem.FiniteElementSpace_ConvertToConformingVDofs(self, dofs, cdofs)

    def ConvertFromConformingVDofs(self, cdofs, dofs):
        return _fem.FiniteElementSpace_ConvertFromConformingVDofs(self, cdofs, dofs)

    def EliminateEssentialBCFromGRM(self, cfes, bdr_attr_is_ess, R):
        return _fem.FiniteElementSpace_EliminateEssentialBCFromGRM(self, cfes, bdr_attr_is_ess, R)

    def GlobalRestrictionMatrix(self, *args):
        return _fem.FiniteElementSpace_GlobalRestrictionMatrix(self, *args)

    def D2C_GlobalRestrictionMatrix(self, cfes):
        return _fem.FiniteElementSpace_D2C_GlobalRestrictionMatrix(self, cfes)

    def D2Const_GlobalRestrictionMatrix(self, cfes):
        return _fem.FiniteElementSpace_D2Const_GlobalRestrictionMatrix(self, cfes)

    def H2L_GlobalRestrictionMatrix(self, lfes):
        return _fem.FiniteElementSpace_H2L_GlobalRestrictionMatrix(self, lfes)

    def Update(self):
        return _fem.FiniteElementSpace_Update(self)

    def UpdateAndInterpolate(self, *args):
        return _fem.FiniteElementSpace_UpdateAndInterpolate(self, *args)

    def SaveUpdate(self):
        return _fem.FiniteElementSpace_SaveUpdate(self)

    def Save(self, out):
        return _fem.FiniteElementSpace_Save(self, out)
    __swig_destroy__ = _fem.delete_FiniteElementSpace
    __del__ = lambda self: None
FiniteElementSpace_swigregister = _fem.FiniteElementSpace_swigregister
FiniteElementSpace_swigregister(FiniteElementSpace)

def FiniteElementSpace_AdjustVDofs(vdofs):
    return _fem.FiniteElementSpace_AdjustVDofs(vdofs)
FiniteElementSpace_AdjustVDofs = _fem.FiniteElementSpace_AdjustVDofs

def FiniteElementSpace_MarkerToList(marker, list):
    return _fem.FiniteElementSpace_MarkerToList(marker, list)
FiniteElementSpace_MarkerToList = _fem.FiniteElementSpace_MarkerToList

def FiniteElementSpace_ListToMarker(list, marker_size, marker, mark_val=-1):
    return _fem.FiniteElementSpace_ListToMarker(list, marker_size, marker, mark_val)
FiniteElementSpace_ListToMarker = _fem.FiniteElementSpace_ListToMarker

# This file is compatible with both classic and new-style classes.


