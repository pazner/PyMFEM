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
    from . import _complex_fem
else:
    import _complex_fem

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _complex_fem.SWIG_PyInstanceMethod_New
_swig_new_static_method = _complex_fem.SWIG_PyStaticMethod_New

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

import mfem._par.vector
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.fespace
import mfem._par.coefficient
import mfem._par.globals
import mfem._par.matrix
import mfem._par.operators
import mfem._par.intrules
import mfem._par.sparsemat
import mfem._par.densemat
import mfem._par.eltrans
import mfem._par.fe
import mfem._par.geom
import mfem._par.fe_base
import mfem._par.fe_fixed_order
import mfem._par.element
import mfem._par.table
import mfem._par.hash
import mfem._par.fe_h1
import mfem._par.fe_nd
import mfem._par.fe_rt
import mfem._par.fe_l2
import mfem._par.fe_nurbs
import mfem._par.fe_pos
import mfem._par.fe_ser
import mfem._par.mesh
import mfem._par.sort_pairs
import mfem._par.ncmesh
import mfem._par.vtk
import mfem._par.vertex
import mfem._par.gridfunc
import mfem._par.bilininteg
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.linearform
import mfem._par.nonlininteg
import mfem._par.doftrans
import mfem._par.handle
import mfem._par.hypre
import mfem._par.restriction
import mfem._par.complex_operator
import mfem._par.bilinearform
import mfem._par.pgridfunc
import mfem._par.pfespace
import mfem._par.pmesh
import mfem._par.pncmesh
import mfem._par.communication
import mfem._par.sets
import mfem._par.plinearform
import mfem._par.pbilinearform
class ComplexGridFunction(mfem._par.vector.Vector):
    r"""Proxy of C++ mfem::ComplexGridFunction class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, f):
        r"""__init__(ComplexGridFunction self, FiniteElementSpace f) -> ComplexGridFunction"""
        _complex_fem.ComplexGridFunction_swiginit(self, _complex_fem.new_ComplexGridFunction(f))

    def Update(self):
        r"""Update(ComplexGridFunction self)"""
        return _complex_fem.ComplexGridFunction_Update(self)
    Update = _swig_new_instance_method(_complex_fem.ComplexGridFunction_Update)

    def ProjectCoefficient(self, *args):
        r"""
        ProjectCoefficient(ComplexGridFunction self, Coefficient real_coeff, Coefficient imag_coeff)
        ProjectCoefficient(ComplexGridFunction self, VectorCoefficient real_vcoeff, VectorCoefficient imag_vcoeff)
        """
        return _complex_fem.ComplexGridFunction_ProjectCoefficient(self, *args)
    ProjectCoefficient = _swig_new_instance_method(_complex_fem.ComplexGridFunction_ProjectCoefficient)

    def ProjectBdrCoefficient(self, real_coeff, imag_coeff, attr):
        r"""ProjectBdrCoefficient(ComplexGridFunction self, Coefficient real_coeff, Coefficient imag_coeff, intArray attr)"""
        return _complex_fem.ComplexGridFunction_ProjectBdrCoefficient(self, real_coeff, imag_coeff, attr)
    ProjectBdrCoefficient = _swig_new_instance_method(_complex_fem.ComplexGridFunction_ProjectBdrCoefficient)

    def ProjectBdrCoefficientNormal(self, real_coeff, imag_coeff, attr):
        r"""ProjectBdrCoefficientNormal(ComplexGridFunction self, VectorCoefficient real_coeff, VectorCoefficient imag_coeff, intArray attr)"""
        return _complex_fem.ComplexGridFunction_ProjectBdrCoefficientNormal(self, real_coeff, imag_coeff, attr)
    ProjectBdrCoefficientNormal = _swig_new_instance_method(_complex_fem.ComplexGridFunction_ProjectBdrCoefficientNormal)

    def ProjectBdrCoefficientTangent(self, real_coeff, imag_coeff, attr):
        r"""ProjectBdrCoefficientTangent(ComplexGridFunction self, VectorCoefficient real_coeff, VectorCoefficient imag_coeff, intArray attr)"""
        return _complex_fem.ComplexGridFunction_ProjectBdrCoefficientTangent(self, real_coeff, imag_coeff, attr)
    ProjectBdrCoefficientTangent = _swig_new_instance_method(_complex_fem.ComplexGridFunction_ProjectBdrCoefficientTangent)

    def FESpace(self, *args):
        r"""
        FESpace(ComplexGridFunction self) -> FiniteElementSpace
        FESpace(ComplexGridFunction self) -> FiniteElementSpace
        """
        return _complex_fem.ComplexGridFunction_FESpace(self, *args)
    FESpace = _swig_new_instance_method(_complex_fem.ComplexGridFunction_FESpace)

    def real(self, *args):
        r"""
        real(ComplexGridFunction self) -> GridFunction
        real(ComplexGridFunction self) -> GridFunction
        """
        return _complex_fem.ComplexGridFunction_real(self, *args)
    real = _swig_new_instance_method(_complex_fem.ComplexGridFunction_real)

    def imag(self, *args):
        r"""
        imag(ComplexGridFunction self) -> GridFunction
        imag(ComplexGridFunction self) -> GridFunction
        """
        return _complex_fem.ComplexGridFunction_imag(self, *args)
    imag = _swig_new_instance_method(_complex_fem.ComplexGridFunction_imag)

    def Sync(self):
        r"""Sync(ComplexGridFunction self)"""
        return _complex_fem.ComplexGridFunction_Sync(self)
    Sync = _swig_new_instance_method(_complex_fem.ComplexGridFunction_Sync)

    def SyncAlias(self):
        r"""SyncAlias(ComplexGridFunction self)"""
        return _complex_fem.ComplexGridFunction_SyncAlias(self)
    SyncAlias = _swig_new_instance_method(_complex_fem.ComplexGridFunction_SyncAlias)
    __swig_destroy__ = _complex_fem.delete_ComplexGridFunction

# Register ComplexGridFunction in _complex_fem:
_complex_fem.ComplexGridFunction_swigregister(ComplexGridFunction)

class ComplexLinearForm(mfem._par.vector.Vector):
    r"""Proxy of C++ mfem::ComplexLinearForm class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(ComplexLinearForm self, FiniteElementSpace fes, mfem::ComplexOperator::Convention convention=HERMITIAN) -> ComplexLinearForm
        __init__(ComplexLinearForm self, FiniteElementSpace fes, LinearForm lf_r, LinearForm lf_i, mfem::ComplexOperator::Convention convention=HERMITIAN) -> ComplexLinearForm
        """
        _complex_fem.ComplexLinearForm_swiginit(self, _complex_fem.new_ComplexLinearForm(*args))
    __swig_destroy__ = _complex_fem.delete_ComplexLinearForm

    def GetConvention(self):
        r"""GetConvention(ComplexLinearForm self) -> mfem::ComplexOperator::Convention"""
        return _complex_fem.ComplexLinearForm_GetConvention(self)
    GetConvention = _swig_new_instance_method(_complex_fem.ComplexLinearForm_GetConvention)

    def SetConvention(self, convention):
        r"""SetConvention(ComplexLinearForm self, mfem::ComplexOperator::Convention const & convention)"""
        return _complex_fem.ComplexLinearForm_SetConvention(self, convention)
    SetConvention = _swig_new_instance_method(_complex_fem.ComplexLinearForm_SetConvention)

    def AddDomainIntegrator(self, lfi_real, lfi_imag):
        r"""AddDomainIntegrator(ComplexLinearForm self, LinearFormIntegrator lfi_real, LinearFormIntegrator lfi_imag)"""
        val = _complex_fem.ComplexLinearForm_AddDomainIntegrator(self, lfi_real, lfi_imag)

        self._intg = (lfi_real, lfi_imag)
        if  hasattr(lfi_real, "thisown"): lfi_real.thisown=0
        if  hasattr(lfi_imag, "thisown"): lfi_imag.thisown=0
        lfi_imag.thisown=0


        return val


    def AddBoundaryIntegrator(self, *args):
        r"""
        AddBoundaryIntegrator(ComplexLinearForm self, LinearFormIntegrator lfi_real, LinearFormIntegrator lfi_imag)
        AddBoundaryIntegrator(ComplexLinearForm self, LinearFormIntegrator lfi_real, LinearFormIntegrator lfi_imag, intArray bdr_attr_marker)
        """
        val = _complex_fem.ComplexLinearForm_AddBoundaryIntegrator(self, *args)

        self._intg = args
        if  hasattr(args[0], "thisown"): args[1].thisown=0
        if  hasattr(args[1], "thisown"): args[1].thisown=0


        return val


    def AddBdrFaceIntegrator(self, *args):
        r"""
        AddBdrFaceIntegrator(ComplexLinearForm self, LinearFormIntegrator lfi_real, LinearFormIntegrator lfi_imag)
        AddBdrFaceIntegrator(ComplexLinearForm self, LinearFormIntegrator lfi_real, LinearFormIntegrator lfi_imag, intArray bdr_attr_marker)
        """
        val = _complex_fem.ComplexLinearForm_AddBdrFaceIntegrator(self, *args)

        self._intg = args
        if  hasattr(args[0], "thisown"): args[1].thisown=0
        if  hasattr(args[1], "thisown"): args[1].thisown=0


        return val


    def FESpace(self):
        r"""FESpace(ComplexLinearForm self) -> FiniteElementSpace"""
        return _complex_fem.ComplexLinearForm_FESpace(self)
    FESpace = _swig_new_instance_method(_complex_fem.ComplexLinearForm_FESpace)

    def real(self, *args):
        r"""
        real(ComplexLinearForm self) -> LinearForm
        real(ComplexLinearForm self) -> LinearForm
        """
        return _complex_fem.ComplexLinearForm_real(self, *args)
    real = _swig_new_instance_method(_complex_fem.ComplexLinearForm_real)

    def imag(self, *args):
        r"""
        imag(ComplexLinearForm self) -> LinearForm
        imag(ComplexLinearForm self) -> LinearForm
        """
        return _complex_fem.ComplexLinearForm_imag(self, *args)
    imag = _swig_new_instance_method(_complex_fem.ComplexLinearForm_imag)

    def Sync(self):
        r"""Sync(ComplexLinearForm self)"""
        return _complex_fem.ComplexLinearForm_Sync(self)
    Sync = _swig_new_instance_method(_complex_fem.ComplexLinearForm_Sync)

    def SyncAlias(self):
        r"""SyncAlias(ComplexLinearForm self)"""
        return _complex_fem.ComplexLinearForm_SyncAlias(self)
    SyncAlias = _swig_new_instance_method(_complex_fem.ComplexLinearForm_SyncAlias)

    def Update(self, *args):
        r"""
        Update(ComplexLinearForm self)
        Update(ComplexLinearForm self, FiniteElementSpace f)
        """
        return _complex_fem.ComplexLinearForm_Update(self, *args)
    Update = _swig_new_instance_method(_complex_fem.ComplexLinearForm_Update)

    def Assemble(self):
        r"""Assemble(ComplexLinearForm self)"""
        return _complex_fem.ComplexLinearForm_Assemble(self)
    Assemble = _swig_new_instance_method(_complex_fem.ComplexLinearForm_Assemble)

    def __call__(self, gf):
        r"""__call__(ComplexLinearForm self, ComplexGridFunction gf) -> std::complex< double >"""
        return _complex_fem.ComplexLinearForm___call__(self, gf)
    __call__ = _swig_new_instance_method(_complex_fem.ComplexLinearForm___call__)

# Register ComplexLinearForm in _complex_fem:
_complex_fem.ComplexLinearForm_swigregister(ComplexLinearForm)

class SesquilinearForm(object):
    r"""Proxy of C++ mfem::SesquilinearForm class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(SesquilinearForm self, FiniteElementSpace fes, mfem::ComplexOperator::Convention convention=HERMITIAN) -> SesquilinearForm
        __init__(SesquilinearForm self, FiniteElementSpace fes, BilinearForm bfr, BilinearForm bfi, mfem::ComplexOperator::Convention convention=HERMITIAN) -> SesquilinearForm
        """
        _complex_fem.SesquilinearForm_swiginit(self, _complex_fem.new_SesquilinearForm(*args))

    def GetConvention(self):
        r"""GetConvention(SesquilinearForm self) -> mfem::ComplexOperator::Convention"""
        return _complex_fem.SesquilinearForm_GetConvention(self)
    GetConvention = _swig_new_instance_method(_complex_fem.SesquilinearForm_GetConvention)

    def SetConvention(self, convention):
        r"""SetConvention(SesquilinearForm self, mfem::ComplexOperator::Convention const & convention)"""
        return _complex_fem.SesquilinearForm_SetConvention(self, convention)
    SetConvention = _swig_new_instance_method(_complex_fem.SesquilinearForm_SetConvention)

    def SetAssemblyLevel(self, assembly_level):
        r"""SetAssemblyLevel(SesquilinearForm self, mfem::AssemblyLevel assembly_level)"""
        return _complex_fem.SesquilinearForm_SetAssemblyLevel(self, assembly_level)
    SetAssemblyLevel = _swig_new_instance_method(_complex_fem.SesquilinearForm_SetAssemblyLevel)

    def real(self, *args):
        r"""
        real(SesquilinearForm self) -> BilinearForm
        real(SesquilinearForm self) -> BilinearForm
        """
        return _complex_fem.SesquilinearForm_real(self, *args)
    real = _swig_new_instance_method(_complex_fem.SesquilinearForm_real)

    def imag(self, *args):
        r"""
        imag(SesquilinearForm self) -> BilinearForm
        imag(SesquilinearForm self) -> BilinearForm
        """
        return _complex_fem.SesquilinearForm_imag(self, *args)
    imag = _swig_new_instance_method(_complex_fem.SesquilinearForm_imag)

    def AddDomainIntegrator(self, bfi_real, bfi_imag):
        r"""AddDomainIntegrator(SesquilinearForm self, BilinearFormIntegrator bfi_real, BilinearFormIntegrator bfi_imag)"""
        val = _complex_fem.SesquilinearForm_AddDomainIntegrator(self, bfi_real, bfi_imag)

        self._intg = (bfi_real, bfi_imag)
        if hasattr(bfi_real, "thisown"): bfi_real.thisown=0
        if hasattr(bfi_imag, "thisown"): bfi_imag.thisown=0


        return val


    def AddBoundaryIntegrator(self, *args):
        r"""
        AddBoundaryIntegrator(SesquilinearForm self, BilinearFormIntegrator bfi_real, BilinearFormIntegrator bfi_imag)
        AddBoundaryIntegrator(SesquilinearForm self, BilinearFormIntegrator bfi_real, BilinearFormIntegrator bfi_imag, intArray bdr_marker)
        """
        val = _complex_fem.SesquilinearForm_AddBoundaryIntegrator(self, *args)

        self._intg = args
        if  hasattr(args[0], "thisown"): args[1].thisown=0
        if  hasattr(args[1], "thisown"): args[1].thisown=0


        return val


    def AddInteriorFaceIntegrator(self, bfi_real, bfi_imag):
        r"""AddInteriorFaceIntegrator(SesquilinearForm self, BilinearFormIntegrator bfi_real, BilinearFormIntegrator bfi_imag)"""
        val = _complex_fem.SesquilinearForm_AddInteriorFaceIntegrator(self, bfi_real, bfi_imag)

        self._intg = (bfi_real, bfi_imag)
        if hasattr(bfi_real, "thisown"): bfi_real.thisown=0
        if hasattr(bfi_imag, "thisown"): bfi_imag.thisown=0


        return val


    def AddBdrFaceIntegrator(self, *args):
        r"""
        AddBdrFaceIntegrator(SesquilinearForm self, BilinearFormIntegrator bfi_real, BilinearFormIntegrator bfi_imag)
        AddBdrFaceIntegrator(SesquilinearForm self, BilinearFormIntegrator bfi_real, BilinearFormIntegrator bfi_imag, intArray bdr_marker)
        """
        val = _complex_fem.SesquilinearForm_AddBdrFaceIntegrator(self, *args)

        self._intg = args
        if  hasattr(args[0], "thisown"): args[1].thisown=0
        if  hasattr(args[1], "thisown"): args[1].thisown=0


        return val


    def Assemble(self, skip_zeros=1):
        r"""Assemble(SesquilinearForm self, int skip_zeros=1)"""
        return _complex_fem.SesquilinearForm_Assemble(self, skip_zeros)
    Assemble = _swig_new_instance_method(_complex_fem.SesquilinearForm_Assemble)

    def Finalize(self, skip_zeros=1):
        r"""Finalize(SesquilinearForm self, int skip_zeros=1)"""
        return _complex_fem.SesquilinearForm_Finalize(self, skip_zeros)
    Finalize = _swig_new_instance_method(_complex_fem.SesquilinearForm_Finalize)

    def AssembleComplexSparseMatrix(self):
        r"""AssembleComplexSparseMatrix(SesquilinearForm self) -> ComplexSparseMatrix"""
        return _complex_fem.SesquilinearForm_AssembleComplexSparseMatrix(self)
    AssembleComplexSparseMatrix = _swig_new_instance_method(_complex_fem.SesquilinearForm_AssembleComplexSparseMatrix)

    def FESpace(self):
        r"""FESpace(SesquilinearForm self) -> FiniteElementSpace"""
        return _complex_fem.SesquilinearForm_FESpace(self)
    FESpace = _swig_new_instance_method(_complex_fem.SesquilinearForm_FESpace)

    def FormLinearSystem(self, ess_tdof_list, x, b, A, X, B, copy_interior=0):
        r"""FormLinearSystem(SesquilinearForm self, intArray ess_tdof_list, Vector x, Vector b, OperatorHandle A, Vector X, Vector B, int copy_interior=0)"""
        return _complex_fem.SesquilinearForm_FormLinearSystem(self, ess_tdof_list, x, b, A, X, B, copy_interior)
    FormLinearSystem = _swig_new_instance_method(_complex_fem.SesquilinearForm_FormLinearSystem)

    def FormSystemMatrix(self, ess_tdof_list, A):
        r"""FormSystemMatrix(SesquilinearForm self, intArray ess_tdof_list, OperatorHandle A)"""
        return _complex_fem.SesquilinearForm_FormSystemMatrix(self, ess_tdof_list, A)
    FormSystemMatrix = _swig_new_instance_method(_complex_fem.SesquilinearForm_FormSystemMatrix)

    def RecoverFEMSolution(self, X, b, x):
        r"""RecoverFEMSolution(SesquilinearForm self, Vector X, Vector b, Vector x)"""
        return _complex_fem.SesquilinearForm_RecoverFEMSolution(self, X, b, x)
    RecoverFEMSolution = _swig_new_instance_method(_complex_fem.SesquilinearForm_RecoverFEMSolution)

    def Update(self, nfes=None):
        r"""Update(SesquilinearForm self, FiniteElementSpace nfes=None)"""
        return _complex_fem.SesquilinearForm_Update(self, nfes)
    Update = _swig_new_instance_method(_complex_fem.SesquilinearForm_Update)

    def SetDiagonalPolicy(self, dpolicy):
        r"""SetDiagonalPolicy(SesquilinearForm self, mfem::Matrix::DiagonalPolicy dpolicy)"""
        return _complex_fem.SesquilinearForm_SetDiagonalPolicy(self, dpolicy)
    SetDiagonalPolicy = _swig_new_instance_method(_complex_fem.SesquilinearForm_SetDiagonalPolicy)

    def GetDiagonalPolicy(self):
        r"""GetDiagonalPolicy(SesquilinearForm self) -> mfem::Matrix::DiagonalPolicy"""
        return _complex_fem.SesquilinearForm_GetDiagonalPolicy(self)
    GetDiagonalPolicy = _swig_new_instance_method(_complex_fem.SesquilinearForm_GetDiagonalPolicy)
    __swig_destroy__ = _complex_fem.delete_SesquilinearForm

# Register SesquilinearForm in _complex_fem:
_complex_fem.SesquilinearForm_swigregister(SesquilinearForm)

class ParComplexGridFunction(mfem._par.vector.Vector):
    r"""Proxy of C++ mfem::ParComplexGridFunction class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, pf):
        r"""__init__(ParComplexGridFunction self, ParFiniteElementSpace pf) -> ParComplexGridFunction"""
        _complex_fem.ParComplexGridFunction_swiginit(self, _complex_fem.new_ParComplexGridFunction(pf))

    def Update(self):
        r"""Update(ParComplexGridFunction self)"""
        return _complex_fem.ParComplexGridFunction_Update(self)
    Update = _swig_new_instance_method(_complex_fem.ParComplexGridFunction_Update)

    def ProjectCoefficient(self, *args):
        r"""
        ProjectCoefficient(ParComplexGridFunction self, Coefficient real_coeff, Coefficient imag_coeff)
        ProjectCoefficient(ParComplexGridFunction self, VectorCoefficient real_vcoeff, VectorCoefficient imag_vcoeff)
        """
        return _complex_fem.ParComplexGridFunction_ProjectCoefficient(self, *args)
    ProjectCoefficient = _swig_new_instance_method(_complex_fem.ParComplexGridFunction_ProjectCoefficient)

    def ProjectBdrCoefficient(self, real_coeff, imag_coeff, attr):
        r"""ProjectBdrCoefficient(ParComplexGridFunction self, Coefficient real_coeff, Coefficient imag_coeff, intArray attr)"""
        return _complex_fem.ParComplexGridFunction_ProjectBdrCoefficient(self, real_coeff, imag_coeff, attr)
    ProjectBdrCoefficient = _swig_new_instance_method(_complex_fem.ParComplexGridFunction_ProjectBdrCoefficient)

    def ProjectBdrCoefficientNormal(self, real_coeff, imag_coeff, attr):
        r"""ProjectBdrCoefficientNormal(ParComplexGridFunction self, VectorCoefficient real_coeff, VectorCoefficient imag_coeff, intArray attr)"""
        return _complex_fem.ParComplexGridFunction_ProjectBdrCoefficientNormal(self, real_coeff, imag_coeff, attr)
    ProjectBdrCoefficientNormal = _swig_new_instance_method(_complex_fem.ParComplexGridFunction_ProjectBdrCoefficientNormal)

    def ProjectBdrCoefficientTangent(self, real_coeff, imag_coeff, attr):
        r"""ProjectBdrCoefficientTangent(ParComplexGridFunction self, VectorCoefficient real_coeff, VectorCoefficient imag_coeff, intArray attr)"""
        return _complex_fem.ParComplexGridFunction_ProjectBdrCoefficientTangent(self, real_coeff, imag_coeff, attr)
    ProjectBdrCoefficientTangent = _swig_new_instance_method(_complex_fem.ParComplexGridFunction_ProjectBdrCoefficientTangent)

    def Distribute(self, *args):
        r"""
        Distribute(ParComplexGridFunction self, Vector tv)
        Distribute(ParComplexGridFunction self, Vector tv)
        """
        return _complex_fem.ParComplexGridFunction_Distribute(self, *args)
    Distribute = _swig_new_instance_method(_complex_fem.ParComplexGridFunction_Distribute)

    def ParallelProject(self, tv):
        r"""ParallelProject(ParComplexGridFunction self, Vector tv)"""
        return _complex_fem.ParComplexGridFunction_ParallelProject(self, tv)
    ParallelProject = _swig_new_instance_method(_complex_fem.ParComplexGridFunction_ParallelProject)

    def FESpace(self, *args):
        r"""
        FESpace(ParComplexGridFunction self) -> FiniteElementSpace
        FESpace(ParComplexGridFunction self) -> FiniteElementSpace
        """
        return _complex_fem.ParComplexGridFunction_FESpace(self, *args)
    FESpace = _swig_new_instance_method(_complex_fem.ParComplexGridFunction_FESpace)

    def ParFESpace(self, *args):
        r"""
        ParFESpace(ParComplexGridFunction self) -> ParFiniteElementSpace
        ParFESpace(ParComplexGridFunction self) -> ParFiniteElementSpace
        """
        return _complex_fem.ParComplexGridFunction_ParFESpace(self, *args)
    ParFESpace = _swig_new_instance_method(_complex_fem.ParComplexGridFunction_ParFESpace)

    def real(self, *args):
        r"""
        real(ParComplexGridFunction self) -> ParGridFunction
        real(ParComplexGridFunction self) -> ParGridFunction
        """
        return _complex_fem.ParComplexGridFunction_real(self, *args)
    real = _swig_new_instance_method(_complex_fem.ParComplexGridFunction_real)

    def imag(self, *args):
        r"""
        imag(ParComplexGridFunction self) -> ParGridFunction
        imag(ParComplexGridFunction self) -> ParGridFunction
        """
        return _complex_fem.ParComplexGridFunction_imag(self, *args)
    imag = _swig_new_instance_method(_complex_fem.ParComplexGridFunction_imag)

    def Sync(self):
        r"""Sync(ParComplexGridFunction self)"""
        return _complex_fem.ParComplexGridFunction_Sync(self)
    Sync = _swig_new_instance_method(_complex_fem.ParComplexGridFunction_Sync)

    def SyncAlias(self):
        r"""SyncAlias(ParComplexGridFunction self)"""
        return _complex_fem.ParComplexGridFunction_SyncAlias(self)
    SyncAlias = _swig_new_instance_method(_complex_fem.ParComplexGridFunction_SyncAlias)

    def ComputeL2Error(self, *args):
        r"""
        ComputeL2Error(ParComplexGridFunction self, Coefficient exsolr, Coefficient exsoli, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeL2Error(ParComplexGridFunction self, VectorCoefficient exsolr, VectorCoefficient exsoli, mfem::IntegrationRule const *[] irs=0, intArray elems=None) -> double
        """
        return _complex_fem.ParComplexGridFunction_ComputeL2Error(self, *args)
    ComputeL2Error = _swig_new_instance_method(_complex_fem.ParComplexGridFunction_ComputeL2Error)
    __swig_destroy__ = _complex_fem.delete_ParComplexGridFunction

# Register ParComplexGridFunction in _complex_fem:
_complex_fem.ParComplexGridFunction_swigregister(ParComplexGridFunction)

class ParComplexLinearForm(mfem._par.vector.Vector):
    r"""Proxy of C++ mfem::ParComplexLinearForm class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(ParComplexLinearForm self, ParFiniteElementSpace pf, mfem::ComplexOperator::Convention convention=HERMITIAN) -> ParComplexLinearForm
        __init__(ParComplexLinearForm self, ParFiniteElementSpace pf, ParLinearForm plf_r, ParLinearForm plf_i, mfem::ComplexOperator::Convention convention=HERMITIAN) -> ParComplexLinearForm
        """
        _complex_fem.ParComplexLinearForm_swiginit(self, _complex_fem.new_ParComplexLinearForm(*args))
    __swig_destroy__ = _complex_fem.delete_ParComplexLinearForm

    def GetConvention(self):
        r"""GetConvention(ParComplexLinearForm self) -> mfem::ComplexOperator::Convention"""
        return _complex_fem.ParComplexLinearForm_GetConvention(self)
    GetConvention = _swig_new_instance_method(_complex_fem.ParComplexLinearForm_GetConvention)

    def SetConvention(self, convention):
        r"""SetConvention(ParComplexLinearForm self, mfem::ComplexOperator::Convention const & convention)"""
        return _complex_fem.ParComplexLinearForm_SetConvention(self, convention)
    SetConvention = _swig_new_instance_method(_complex_fem.ParComplexLinearForm_SetConvention)

    def AddDomainIntegrator(self, lfi_real, lfi_imag):
        r"""AddDomainIntegrator(ParComplexLinearForm self, LinearFormIntegrator lfi_real, LinearFormIntegrator lfi_imag)"""
        val = _complex_fem.ParComplexLinearForm_AddDomainIntegrator(self, lfi_real, lfi_imag)

        self._intg = (lfi_real, lfi_imag)
        if  hasattr(lfi_real, "thisown"): lfi_real.thisown=0
        if  hasattr(lfi_imag, "thisown"): lfi_imag.thisown=0
        lfi_imag.thisown=0


        return val


    def AddBoundaryIntegrator(self, *args):
        r"""
        AddBoundaryIntegrator(ParComplexLinearForm self, LinearFormIntegrator lfi_real, LinearFormIntegrator lfi_imag)
        AddBoundaryIntegrator(ParComplexLinearForm self, LinearFormIntegrator lfi_real, LinearFormIntegrator lfi_imag, intArray bdr_attr_marker)
        """
        val = _complex_fem.ParComplexLinearForm_AddBoundaryIntegrator(self, *args)

        self._intg = args
        if  hasattr(args[0], "thisown"): args[1].thisown=0
        if  hasattr(args[1], "thisown"): args[1].thisown=0


        return val


    def AddBdrFaceIntegrator(self, *args):
        r"""
        AddBdrFaceIntegrator(ParComplexLinearForm self, LinearFormIntegrator lfi_real, LinearFormIntegrator lfi_imag)
        AddBdrFaceIntegrator(ParComplexLinearForm self, LinearFormIntegrator lfi_real, LinearFormIntegrator lfi_imag, intArray bdr_attr_marker)
        """
        val = _complex_fem.ParComplexLinearForm_AddBdrFaceIntegrator(self, *args)

        self._intg = args
        if  hasattr(args[0], "thisown"): args[1].thisown=0
        if  hasattr(args[1], "thisown"): args[1].thisown=0


        return val


    def ParFESpace(self):
        r"""ParFESpace(ParComplexLinearForm self) -> ParFiniteElementSpace"""
        return _complex_fem.ParComplexLinearForm_ParFESpace(self)
    ParFESpace = _swig_new_instance_method(_complex_fem.ParComplexLinearForm_ParFESpace)

    def real(self, *args):
        r"""
        real(ParComplexLinearForm self) -> ParLinearForm
        real(ParComplexLinearForm self) -> ParLinearForm
        """
        return _complex_fem.ParComplexLinearForm_real(self, *args)
    real = _swig_new_instance_method(_complex_fem.ParComplexLinearForm_real)

    def imag(self, *args):
        r"""
        imag(ParComplexLinearForm self) -> ParLinearForm
        imag(ParComplexLinearForm self) -> ParLinearForm
        """
        return _complex_fem.ParComplexLinearForm_imag(self, *args)
    imag = _swig_new_instance_method(_complex_fem.ParComplexLinearForm_imag)

    def Sync(self):
        r"""Sync(ParComplexLinearForm self)"""
        return _complex_fem.ParComplexLinearForm_Sync(self)
    Sync = _swig_new_instance_method(_complex_fem.ParComplexLinearForm_Sync)

    def SyncAlias(self):
        r"""SyncAlias(ParComplexLinearForm self)"""
        return _complex_fem.ParComplexLinearForm_SyncAlias(self)
    SyncAlias = _swig_new_instance_method(_complex_fem.ParComplexLinearForm_SyncAlias)

    def Update(self, pf=None):
        r"""Update(ParComplexLinearForm self, ParFiniteElementSpace pf=None)"""
        return _complex_fem.ParComplexLinearForm_Update(self, pf)
    Update = _swig_new_instance_method(_complex_fem.ParComplexLinearForm_Update)

    def Assemble(self):
        r"""Assemble(ParComplexLinearForm self)"""
        return _complex_fem.ParComplexLinearForm_Assemble(self)
    Assemble = _swig_new_instance_method(_complex_fem.ParComplexLinearForm_Assemble)

    def ParallelAssemble(self, *args):
        r"""
        ParallelAssemble(ParComplexLinearForm self, Vector tv)
        ParallelAssemble(ParComplexLinearForm self) -> HypreParVector
        """
        return _complex_fem.ParComplexLinearForm_ParallelAssemble(self, *args)
    ParallelAssemble = _swig_new_instance_method(_complex_fem.ParComplexLinearForm_ParallelAssemble)

    def __call__(self, gf):
        r"""__call__(ParComplexLinearForm self, ParComplexGridFunction gf) -> std::complex< double >"""
        return _complex_fem.ParComplexLinearForm___call__(self, gf)
    __call__ = _swig_new_instance_method(_complex_fem.ParComplexLinearForm___call__)

# Register ParComplexLinearForm in _complex_fem:
_complex_fem.ParComplexLinearForm_swigregister(ParComplexLinearForm)

class ParSesquilinearForm(object):
    r"""Proxy of C++ mfem::ParSesquilinearForm class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(ParSesquilinearForm self, ParFiniteElementSpace pf, mfem::ComplexOperator::Convention convention=HERMITIAN) -> ParSesquilinearForm
        __init__(ParSesquilinearForm self, ParFiniteElementSpace pf, ParBilinearForm pbfr, ParBilinearForm pbfi, mfem::ComplexOperator::Convention convention=HERMITIAN) -> ParSesquilinearForm
        """
        _complex_fem.ParSesquilinearForm_swiginit(self, _complex_fem.new_ParSesquilinearForm(*args))

    def GetConvention(self):
        r"""GetConvention(ParSesquilinearForm self) -> mfem::ComplexOperator::Convention"""
        return _complex_fem.ParSesquilinearForm_GetConvention(self)
    GetConvention = _swig_new_instance_method(_complex_fem.ParSesquilinearForm_GetConvention)

    def SetConvention(self, convention):
        r"""SetConvention(ParSesquilinearForm self, mfem::ComplexOperator::Convention const & convention)"""
        return _complex_fem.ParSesquilinearForm_SetConvention(self, convention)
    SetConvention = _swig_new_instance_method(_complex_fem.ParSesquilinearForm_SetConvention)

    def SetAssemblyLevel(self, assembly_level):
        r"""SetAssemblyLevel(ParSesquilinearForm self, mfem::AssemblyLevel assembly_level)"""
        return _complex_fem.ParSesquilinearForm_SetAssemblyLevel(self, assembly_level)
    SetAssemblyLevel = _swig_new_instance_method(_complex_fem.ParSesquilinearForm_SetAssemblyLevel)

    def real(self, *args):
        r"""
        real(ParSesquilinearForm self) -> ParBilinearForm
        real(ParSesquilinearForm self) -> ParBilinearForm
        """
        return _complex_fem.ParSesquilinearForm_real(self, *args)
    real = _swig_new_instance_method(_complex_fem.ParSesquilinearForm_real)

    def imag(self, *args):
        r"""
        imag(ParSesquilinearForm self) -> ParBilinearForm
        imag(ParSesquilinearForm self) -> ParBilinearForm
        """
        return _complex_fem.ParSesquilinearForm_imag(self, *args)
    imag = _swig_new_instance_method(_complex_fem.ParSesquilinearForm_imag)

    def AddDomainIntegrator(self, bfi_real, bfi_imag):
        r"""AddDomainIntegrator(ParSesquilinearForm self, BilinearFormIntegrator bfi_real, BilinearFormIntegrator bfi_imag)"""
        val = _complex_fem.ParSesquilinearForm_AddDomainIntegrator(self, bfi_real, bfi_imag)

        self._intg = (bfi_real, bfi_imag)
        if hasattr(bfi_real, "thisown"): bfi_real.thisown=0
        if hasattr(bfi_imag, "thisown"): bfi_imag.thisown=0


        return val


    def AddBoundaryIntegrator(self, *args):
        r"""
        AddBoundaryIntegrator(ParSesquilinearForm self, BilinearFormIntegrator bfi_real, BilinearFormIntegrator bfi_imag)
        AddBoundaryIntegrator(ParSesquilinearForm self, BilinearFormIntegrator bfi_real, BilinearFormIntegrator bfi_imag, intArray bdr_marker)
        """
        val = _complex_fem.ParSesquilinearForm_AddBoundaryIntegrator(self, *args)

        self._intg = args
        if  hasattr(args[0], "thisown"): args[1].thisown=0
        if  hasattr(args[1], "thisown"): args[1].thisown=0


        return val


    def AddInteriorFaceIntegrator(self, bfi_real, bfi_imag):
        r"""AddInteriorFaceIntegrator(ParSesquilinearForm self, BilinearFormIntegrator bfi_real, BilinearFormIntegrator bfi_imag)"""
        val = _complex_fem.ParSesquilinearForm_AddInteriorFaceIntegrator(self, bfi_real, bfi_imag)

        self._intg = (bfi_real, bfi_imag)
        if hasattr(bfi_real, "thisown"): bfi_real.thisown=0
        if hasattr(bfi_imag, "thisown"): bfi_imag.thisown=0


        return val


    def AddBdrFaceIntegrator(self, *args):
        r"""
        AddBdrFaceIntegrator(ParSesquilinearForm self, BilinearFormIntegrator bfi_real, BilinearFormIntegrator bfi_imag)
        AddBdrFaceIntegrator(ParSesquilinearForm self, BilinearFormIntegrator bfi_real, BilinearFormIntegrator bfi_imag, intArray bdr_marker)
        """
        val = _complex_fem.ParSesquilinearForm_AddBdrFaceIntegrator(self, *args)

        self._intg = args
        if  hasattr(args[0], "thisown"): args[1].thisown=0
        if  hasattr(args[1], "thisown"): args[1].thisown=0


        return val


    def Assemble(self, skip_zeros=1):
        r"""Assemble(ParSesquilinearForm self, int skip_zeros=1)"""
        return _complex_fem.ParSesquilinearForm_Assemble(self, skip_zeros)
    Assemble = _swig_new_instance_method(_complex_fem.ParSesquilinearForm_Assemble)

    def Finalize(self, skip_zeros=1):
        r"""Finalize(ParSesquilinearForm self, int skip_zeros=1)"""
        return _complex_fem.ParSesquilinearForm_Finalize(self, skip_zeros)
    Finalize = _swig_new_instance_method(_complex_fem.ParSesquilinearForm_Finalize)

    def ParallelAssemble(self):
        r"""ParallelAssemble(ParSesquilinearForm self) -> ComplexHypreParMatrix"""
        return _complex_fem.ParSesquilinearForm_ParallelAssemble(self)
    ParallelAssemble = _swig_new_instance_method(_complex_fem.ParSesquilinearForm_ParallelAssemble)

    def ParFESpace(self):
        r"""ParFESpace(ParSesquilinearForm self) -> ParFiniteElementSpace"""
        return _complex_fem.ParSesquilinearForm_ParFESpace(self)
    ParFESpace = _swig_new_instance_method(_complex_fem.ParSesquilinearForm_ParFESpace)

    def FormLinearSystem(self, ess_tdof_list, x, b, A, X, B, copy_interior=0):
        r"""FormLinearSystem(ParSesquilinearForm self, intArray ess_tdof_list, Vector x, Vector b, OperatorHandle A, Vector X, Vector B, int copy_interior=0)"""
        return _complex_fem.ParSesquilinearForm_FormLinearSystem(self, ess_tdof_list, x, b, A, X, B, copy_interior)
    FormLinearSystem = _swig_new_instance_method(_complex_fem.ParSesquilinearForm_FormLinearSystem)

    def FormSystemMatrix(self, ess_tdof_list, A):
        r"""FormSystemMatrix(ParSesquilinearForm self, intArray ess_tdof_list, OperatorHandle A)"""
        return _complex_fem.ParSesquilinearForm_FormSystemMatrix(self, ess_tdof_list, A)
    FormSystemMatrix = _swig_new_instance_method(_complex_fem.ParSesquilinearForm_FormSystemMatrix)

    def RecoverFEMSolution(self, X, b, x):
        r"""RecoverFEMSolution(ParSesquilinearForm self, Vector X, Vector b, Vector x)"""
        return _complex_fem.ParSesquilinearForm_RecoverFEMSolution(self, X, b, x)
    RecoverFEMSolution = _swig_new_instance_method(_complex_fem.ParSesquilinearForm_RecoverFEMSolution)

    def Update(self, nfes=None):
        r"""Update(ParSesquilinearForm self, FiniteElementSpace nfes=None)"""
        return _complex_fem.ParSesquilinearForm_Update(self, nfes)
    Update = _swig_new_instance_method(_complex_fem.ParSesquilinearForm_Update)
    __swig_destroy__ = _complex_fem.delete_ParSesquilinearForm

# Register ParSesquilinearForm in _complex_fem:
_complex_fem.ParSesquilinearForm_swigregister(ParSesquilinearForm)



