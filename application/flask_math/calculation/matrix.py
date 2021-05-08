from sympy import *
from flask import flash
from flask_math.calculation.common.MATRIX import MATRIX
from flask_math.calculation.common.STR import LATEX


def calculation(matrixA, type):
    try:
        list_A = MATRIX(matrixA)
        A, Ar, Ac = list_A[0], list_A[1], list_A[2]

        if type == "A":
            anser = "A="+LATEX(A)

        elif type == "A^n":
            if(Ar == Ac):
                P, D = list(A.diagonalize())
                for i in range(Ac):
                    D[i, i] = "("+str(D[i, i])+")^n"
                anser = "A^n="+LATEX(P*D*P.inv())
            else:
                flash("Error:正方行列を入力してください")
                anser = "正方行列を入力してください"

        elif type == "A^{-1}":
            if(Ar == Ac):
                anser = "A^{-1}="+LATEX(A.inv())
            else:
                flash("Error:正方行列を入力してください")
                anser = "正方行列を入力してください"

        elif type == "A^t":
            anser = "A^T="+LATEX(A.transpose())

        elif type == "\widetilde{A}":
            if(Ar == Ac):
                anser = "\widetilde{A}="+LATEX(A.adjugate())
            else:
                flash("Error:正方行列を入力してください")
                anser = "正方行列を入力してください"

        elif type == "det(A)":
            if(Ar == Ac):
                anser = "det(A)="+LATEX(A.det())
            else:
                flash("Error:正方行列を入力してください")
                anser = "正方行列を入力してください"

        elif type == "rank(A)":
            anser = "rank(A)="+LATEX(A.rank())

        elif type == "tr(A)":
            if(Ar == Ac):
                anser = "tr(A)="+LATEX(A.trace())
            else:
                flash("Error:正方行列を入力してください")
                anser = "正方行列を入力してください"

        elif type == "λ":
            if(Ar == Ac):
                A = A.eigenvals()
                anser = ""
                for B in A.items():
                    anser += ("\lambda="+LATEX(B[0])+"(n="+LATEX(B[1])+"), ")
            else:
                flash("Error:正方行列を入力してください")
                anser = "正方行列を入力してください"

        elif type == "P":
            if(Ar == Ac):
                A = list(A.diagonalize())
                anser = "P="+LATEX(A[0])
            else:
                flash("Error:正方行列を入力してください")
                anser = "正方行列を入力してください"

        elif type == "P^{-1}AP":
            if(Ar == Ac):
                A = list(A.diagonalize())
                anser = "P^{-1}AP="+LATEX(A[1])
            else:
                flash("Error:正方行列を入力してください")
                anser = "正方行列を入力してください"
    except:
        anser = "Error"
        flash("エラー：もう一度入力してください")
    return anser
