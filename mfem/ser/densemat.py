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
            fp, pathname, description = imp.find_module('_densemat', [dirname(__file__)])
        except ImportError:
            import _densemat
            return _densemat
        if fp is not None:
            try:
                _mod = imp.load_module('_densemat', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _densemat = swig_import_helper()
    del swig_import_helper
else:
    import _densemat
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
import vector
import operators
import matrix
class DenseMatrix(matrix.Matrix):
    __swig_setmethods__ = {}
    for _s in [matrix.Matrix]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, DenseMatrix, name, value)
    __swig_getmethods__ = {}
    for _s in [matrix.Matrix]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, DenseMatrix, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _densemat.new_DenseMatrix(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def UseExternalData(self, d, h, w):
        return _densemat.DenseMatrix_UseExternalData(self, d, h, w)

    def ClearExternalData(self):
        return _densemat.DenseMatrix_ClearExternalData(self)

    def Size(self):
        return _densemat.DenseMatrix_Size(self)

    def SetSize(self, *args):
        return _densemat.DenseMatrix_SetSize(self, *args)

    def Data(self):
        return _densemat.DenseMatrix_Data(self)

    def __call__(self, *args):
        return _densemat.DenseMatrix___call__(self, *args)

    def __mul__(self, m):
        return _densemat.DenseMatrix___mul__(self, m)

    def Trace(self):
        return _densemat.DenseMatrix_Trace(self)

    def Elem(self, *args):
        return _densemat.DenseMatrix_Elem(self, *args)

    def Mult(self, *args):
        return _densemat.DenseMatrix_Mult(self, *args)

    def MultTranspose(self, *args):
        return _densemat.DenseMatrix_MultTranspose(self, *args)

    def AddMult(self, x, y):
        return _densemat.DenseMatrix_AddMult(self, x, y)

    def AddMult_a(self, a, x, y):
        return _densemat.DenseMatrix_AddMult_a(self, a, x, y)

    def AddMultTranspose_a(self, a, x, y):
        return _densemat.DenseMatrix_AddMultTranspose_a(self, a, x, y)

    def LeftScaling(self, s):
        return _densemat.DenseMatrix_LeftScaling(self, s)

    def InvLeftScaling(self, s):
        return _densemat.DenseMatrix_InvLeftScaling(self, s)

    def RightScaling(self, s):
        return _densemat.DenseMatrix_RightScaling(self, s)

    def InvRightScaling(self, s):
        return _densemat.DenseMatrix_InvRightScaling(self, s)

    def SymmetricScaling(self, s):
        return _densemat.DenseMatrix_SymmetricScaling(self, s)

    def InvSymmetricScaling(self, s):
        return _densemat.DenseMatrix_InvSymmetricScaling(self, s)

    def InnerProduct(self, *args):
        return _densemat.DenseMatrix_InnerProduct(self, *args)

    def Inverse(self):
        return _densemat.DenseMatrix_Inverse(self)

    def Invert(self):
        return _densemat.DenseMatrix_Invert(self)

    def Det(self):
        return _densemat.DenseMatrix_Det(self)

    def Weight(self):
        return _densemat.DenseMatrix_Weight(self)

    def Add(self, c, A):
        return _densemat.DenseMatrix_Add(self, c, A)

    def Assign(self, *args):
        return _densemat.DenseMatrix_Assign(self, *args)

    def __iadd__(self, v):
        ret = _densmat.DenseMatrix___iadd__(self, v)
        ret.thisown = self.thisown
        self.thisown = 0                  
        return ret



    def __isub__(self, v):
        ret = _densmat.DenseMatrix___isub__(self, v)  
        ret.thisown = self.thisown
        self.thisown = 0            
        return ret



    def __imul__(self, v):
        ret = _densmat.DenseMatrix___imul__(self, v)  
        ret.thisown = self.thisown
        self.thisown = 0            
        return ret



    def Neg(self):
        return _densemat.DenseMatrix_Neg(self)

    def Norm2(self, v):
        return _densemat.DenseMatrix_Norm2(self, v)

    def MaxMaxNorm(self):
        return _densemat.DenseMatrix_MaxMaxNorm(self)

    def FNorm(self):
        return _densemat.DenseMatrix_FNorm(self)

    def Eigenvalues(self, *args):
        return _densemat.DenseMatrix_Eigenvalues(self, *args)

    def Eigensystem(self, ev, evect):
        return _densemat.DenseMatrix_Eigensystem(self, ev, evect)

    def SingularValues(self, sv):
        return _densemat.DenseMatrix_SingularValues(self, sv)

    def Rank(self, tol):
        return _densemat.DenseMatrix_Rank(self, tol)

    def CalcSingularvalue(self, i):
        return _densemat.DenseMatrix_CalcSingularvalue(self, i)

    def CalcEigenvalues(self, arg2, vec):
        return _densemat.DenseMatrix_CalcEigenvalues(self, arg2, vec)

    def GetRow(self, r, row):
        return _densemat.DenseMatrix_GetRow(self, r, row)

    def GetColumn(self, c, col):
        return _densemat.DenseMatrix_GetColumn(self, c, col)

    def GetColumnReference(self, c, col):
        return _densemat.DenseMatrix_GetColumnReference(self, c, col)

    def SetRow(self, *args):
        return _densemat.DenseMatrix_SetRow(self, *args)

    def SetCol(self, *args):
        return _densemat.DenseMatrix_SetCol(self, *args)

    def GetDiag(self, d):
        return _densemat.DenseMatrix_GetDiag(self, d)

    def Getl1Diag(self, l):
        return _densemat.DenseMatrix_Getl1Diag(self, l)

    def GetRowSums(self, l):
        return _densemat.DenseMatrix_GetRowSums(self, l)

    def Diag(self, *args):
        return _densemat.DenseMatrix_Diag(self, *args)

    def Transpose(self, *args):
        return _densemat.DenseMatrix_Transpose(self, *args)

    def Symmetrize(self):
        return _densemat.DenseMatrix_Symmetrize(self)

    def Lump(self):
        return _densemat.DenseMatrix_Lump(self)

    def GradToCurl(self, curl):
        return _densemat.DenseMatrix_GradToCurl(self, curl)

    def GradToDiv(self, div):
        return _densemat.DenseMatrix_GradToDiv(self, div)

    def CopyRows(self, A, row1, row2):
        return _densemat.DenseMatrix_CopyRows(self, A, row1, row2)

    def CopyCols(self, A, col1, col2):
        return _densemat.DenseMatrix_CopyCols(self, A, col1, col2)

    def CopyMNt(self, A, row_offset, col_offset):
        return _densemat.DenseMatrix_CopyMNt(self, A, row_offset, col_offset)

    def CopyMN(self, *args):
        return _densemat.DenseMatrix_CopyMN(self, *args)

    def CopyMNDiag(self, *args):
        return _densemat.DenseMatrix_CopyMNDiag(self, *args)

    def AddMatrix(self, *args):
        return _densemat.DenseMatrix_AddMatrix(self, *args)

    def AddToVector(self, offset, v):
        return _densemat.DenseMatrix_AddToVector(self, offset, v)

    def GetFromVector(self, offset, v):
        return _densemat.DenseMatrix_GetFromVector(self, offset, v)

    def AdjustDofDirection(self, dofs):
        return _densemat.DenseMatrix_AdjustDofDirection(self, dofs)

    def Threshold(self, eps):
        return _densemat.DenseMatrix_Threshold(self, eps)

    def CheckFinite(self):
        return _densemat.DenseMatrix_CheckFinite(self)

    def Print(self, *args):
        return _densemat.DenseMatrix_Print(self, *args)

    def PrintMatlab(self, *args):
        return _densemat.DenseMatrix_PrintMatlab(self, *args)

    def PrintT(self, *args):
        return _densemat.DenseMatrix_PrintT(self, *args)

    def TestInversion(self):
        return _densemat.DenseMatrix_TestInversion(self)
    __swig_destroy__ = _densemat.delete_DenseMatrix
    __del__ = lambda self: None

    def __getitem__(self, *args):
        i, j = args[0][0], args[0][1]
        return _densemat.DenseMatrix___getitem__(self, i, j)



    def __setitem__(self, *args):
        i, j, v = args[0][0], args[0][1], args[1]
        return _densemat.DenseMatrix___setitem__(self, i, j, v)



    def GetDataArray(self):
        return _densemat.DenseMatrix_GetDataArray(self)
DenseMatrix_swigregister = _densemat.DenseMatrix_swigregister
DenseMatrix_swigregister(DenseMatrix)


def Add(*args):
    return _densemat.Add(*args)
Add = _densemat.Add

def Mult(b, c, a):
    return _densemat.Mult(b, c, a)
Mult = _densemat.Mult

def AddMult(b, c, a):
    return _densemat.AddMult(b, c, a)
AddMult = _densemat.AddMult

def CalcAdjugate(a, adja):
    return _densemat.CalcAdjugate(a, adja)
CalcAdjugate = _densemat.CalcAdjugate

def CalcAdjugateTranspose(a, adjat):
    return _densemat.CalcAdjugateTranspose(a, adjat)
CalcAdjugateTranspose = _densemat.CalcAdjugateTranspose

def CalcInverse(a, inva):
    return _densemat.CalcInverse(a, inva)
CalcInverse = _densemat.CalcInverse

def CalcInverseTranspose(a, inva):
    return _densemat.CalcInverseTranspose(a, inva)
CalcInverseTranspose = _densemat.CalcInverseTranspose

def CalcOrtho(J, n):
    return _densemat.CalcOrtho(J, n)
CalcOrtho = _densemat.CalcOrtho

def MultAAt(a, aat):
    return _densemat.MultAAt(a, aat)
MultAAt = _densemat.MultAAt

def MultADAt(A, D, ADAt):
    return _densemat.MultADAt(A, D, ADAt)
MultADAt = _densemat.MultADAt

def AddMultADAt(A, D, ADAt):
    return _densemat.AddMultADAt(A, D, ADAt)
AddMultADAt = _densemat.AddMultADAt

def MultABt(A, B, ABt):
    return _densemat.MultABt(A, B, ABt)
MultABt = _densemat.MultABt

def MultADBt(A, D, B, ADAt):
    return _densemat.MultADBt(A, D, B, ADAt)
MultADBt = _densemat.MultADBt

def AddMultABt(A, B, ABt):
    return _densemat.AddMultABt(A, B, ABt)
AddMultABt = _densemat.AddMultABt

def MultAtB(A, B, AtB):
    return _densemat.MultAtB(A, B, AtB)
MultAtB = _densemat.MultAtB

def AddMult_a_AAt(a, A, AAt):
    return _densemat.AddMult_a_AAt(a, A, AAt)
AddMult_a_AAt = _densemat.AddMult_a_AAt

def Mult_a_AAt(a, A, AAt):
    return _densemat.Mult_a_AAt(a, A, AAt)
Mult_a_AAt = _densemat.Mult_a_AAt

def MultVVt(v, vvt):
    return _densemat.MultVVt(v, vvt)
MultVVt = _densemat.MultVVt

def MultVWt(v, w, VWt):
    return _densemat.MultVWt(v, w, VWt)
MultVWt = _densemat.MultVWt

def AddMultVWt(v, w, VWt):
    return _densemat.AddMultVWt(v, w, VWt)
AddMultVWt = _densemat.AddMultVWt

def AddMult_a_VWt(a, v, w, VWt):
    return _densemat.AddMult_a_VWt(a, v, w, VWt)
AddMult_a_VWt = _densemat.AddMult_a_VWt

def AddMult_a_VVt(a, v, VVt):
    return _densemat.AddMult_a_VVt(a, v, VVt)
AddMult_a_VVt = _densemat.AddMult_a_VVt
class LUFactors(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LUFactors, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LUFactors, name)
    __repr__ = _swig_repr
    __swig_setmethods__["data"] = _densemat.LUFactors_data_set
    __swig_getmethods__["data"] = _densemat.LUFactors_data_get
    if _newclass:
        data = _swig_property(_densemat.LUFactors_data_get, _densemat.LUFactors_data_set)
    __swig_setmethods__["ipiv"] = _densemat.LUFactors_ipiv_set
    __swig_getmethods__["ipiv"] = _densemat.LUFactors_ipiv_get
    if _newclass:
        ipiv = _swig_property(_densemat.LUFactors_ipiv_get, _densemat.LUFactors_ipiv_set)
    ipiv_base = _densemat.LUFactors_ipiv_base

    def __init__(self, *args):
        this = _densemat.new_LUFactors(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def Factor(self, m):
        return _densemat.LUFactors_Factor(self, m)

    def Mult(self, m, n, X):
        return _densemat.LUFactors_Mult(self, m, n, X)

    def LSolve(self, m, n, X):
        return _densemat.LUFactors_LSolve(self, m, n, X)

    def USolve(self, m, n, X):
        return _densemat.LUFactors_USolve(self, m, n, X)

    def Solve(self, m, n, X):
        return _densemat.LUFactors_Solve(self, m, n, X)

    def GetInverseMatrix(self, m, X):
        return _densemat.LUFactors_GetInverseMatrix(self, m, X)
    __swig_getmethods__["SubMult"] = lambda x: _densemat.LUFactors_SubMult
    if _newclass:
        SubMult = staticmethod(_densemat.LUFactors_SubMult)

    def BlockFactor(self, m, n, A12, A21, A22):
        return _densemat.LUFactors_BlockFactor(self, m, n, A12, A21, A22)

    def BlockForwSolve(self, m, n, r, L21, B1, B2):
        return _densemat.LUFactors_BlockForwSolve(self, m, n, r, L21, B1, B2)

    def BlockBackSolve(self, m, n, r, U12, X2, Y1):
        return _densemat.LUFactors_BlockBackSolve(self, m, n, r, U12, X2, Y1)
    __swig_destroy__ = _densemat.delete_LUFactors
    __del__ = lambda self: None
LUFactors_swigregister = _densemat.LUFactors_swigregister
LUFactors_swigregister(LUFactors)

def LUFactors_SubMult(m, n, r, A21, X1, X2):
    return _densemat.LUFactors_SubMult(m, n, r, A21, X1, X2)
LUFactors_SubMult = _densemat.LUFactors_SubMult

class DenseMatrixInverse(matrix.MatrixInverse):
    __swig_setmethods__ = {}
    for _s in [matrix.MatrixInverse]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, DenseMatrixInverse, name, value)
    __swig_getmethods__ = {}
    for _s in [matrix.MatrixInverse]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, DenseMatrixInverse, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _densemat.new_DenseMatrixInverse(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def Size(self):
        return _densemat.DenseMatrixInverse_Size(self)

    def Factor(self, *args):
        return _densemat.DenseMatrixInverse_Factor(self, *args)

    def SetOperator(self, op):
        return _densemat.DenseMatrixInverse_SetOperator(self, op)

    def Mult(self, *args):
        return _densemat.DenseMatrixInverse_Mult(self, *args)

    def GetInverseMatrix(self, Ainv):
        return _densemat.DenseMatrixInverse_GetInverseMatrix(self, Ainv)

    def TestInversion(self):
        return _densemat.DenseMatrixInverse_TestInversion(self)
    __swig_destroy__ = _densemat.delete_DenseMatrixInverse
    __del__ = lambda self: None
DenseMatrixInverse_swigregister = _densemat.DenseMatrixInverse_swigregister
DenseMatrixInverse_swigregister(DenseMatrixInverse)

class DenseMatrixEigensystem(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DenseMatrixEigensystem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DenseMatrixEigensystem, name)
    __repr__ = _swig_repr

    def __init__(self, m):
        this = _densemat.new_DenseMatrixEigensystem(m)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def Eval(self):
        return _densemat.DenseMatrixEigensystem_Eval(self)

    def Eigenvalues(self):
        return _densemat.DenseMatrixEigensystem_Eigenvalues(self)

    def Eigenvectors(self):
        return _densemat.DenseMatrixEigensystem_Eigenvectors(self)

    def Eigenvalue(self, i):
        return _densemat.DenseMatrixEigensystem_Eigenvalue(self, i)

    def Eigenvector(self, i):
        return _densemat.DenseMatrixEigensystem_Eigenvector(self, i)
    __swig_destroy__ = _densemat.delete_DenseMatrixEigensystem
    __del__ = lambda self: None
DenseMatrixEigensystem_swigregister = _densemat.DenseMatrixEigensystem_swigregister
DenseMatrixEigensystem_swigregister(DenseMatrixEigensystem)

class DenseMatrixSVD(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DenseMatrixSVD, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DenseMatrixSVD, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _densemat.new_DenseMatrixSVD(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def Eval(self, M):
        return _densemat.DenseMatrixSVD_Eval(self, M)

    def Singularvalues(self):
        return _densemat.DenseMatrixSVD_Singularvalues(self)

    def Singularvalue(self, i):
        return _densemat.DenseMatrixSVD_Singularvalue(self, i)
    __swig_destroy__ = _densemat.delete_DenseMatrixSVD
    __del__ = lambda self: None
DenseMatrixSVD_swigregister = _densemat.DenseMatrixSVD_swigregister
DenseMatrixSVD_swigregister(DenseMatrixSVD)

class DenseTensor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DenseTensor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DenseTensor, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _densemat.new_DenseTensor(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def SizeI(self):
        return _densemat.DenseTensor_SizeI(self)

    def SizeJ(self):
        return _densemat.DenseTensor_SizeJ(self)

    def SizeK(self):
        return _densemat.DenseTensor_SizeK(self)

    def SetSize(self, i, j, k):
        return _densemat.DenseTensor_SetSize(self, i, j, k)

    def UseExternalData(self, ext_data, i, j, k):
        return _densemat.DenseTensor_UseExternalData(self, ext_data, i, j, k)

    def __call__(self, *args):
        return _densemat.DenseTensor___call__(self, *args)

    def GetData(self, k):
        return _densemat.DenseTensor_GetData(self, k)

    def Data(self):
        return _densemat.DenseTensor_Data(self)

    def AddMult(self, elem_dof, x, y):
        return _densemat.DenseTensor_AddMult(self, elem_dof, x, y)
    __swig_destroy__ = _densemat.delete_DenseTensor
    __del__ = lambda self: None
DenseTensor_swigregister = _densemat.DenseTensor_swigregister
DenseTensor_swigregister(DenseTensor)

# This file is compatible with both classic and new-style classes.


