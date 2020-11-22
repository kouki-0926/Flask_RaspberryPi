from sympy import *
from flask import flash
from flask_math.calculation.common.MATRIX import MATRIX
from flask_math.calculation.common.STR import LATEX

def calculation(matrixA,Ar,Ac,type):
    try:
        Ar,Ac=[int(Ar),int(Ac)]
        A=MATRIX(matrixA,Ar,Ac)
        type=type+" = "

        if type=="A = ":
            anser=A
            anser_r=Ar
            anser_c=Ac
            output_type="MATRIX"

        elif type=="A^n = ":
            A=list(A.diagonalize())
            P=A[0]
            D=A[1]
            for i in range(0,Ac,1):
                D[i,i]="("+str(D[i,i])+")^n"
            anser=P*D*P.inv()
            anser_r=Ar
            anser_c=Ac
            output_type="MATRIX"

        elif type=="A^t = ":
            anser=A.transpose()
            anser_r=Ac
            anser_c=Ar
            output_type="MATRIX"

        elif type=="A^-1 = ":
            anser=A.inv()
            anser_r=Ar
            anser_c=Ac
            output_type="MATRIX"

        elif type=="A~ = ":
            anser=A.adjugate()
            anser_r=Ar
            anser_c=Ac
            output_type="MATRIX"

        elif type=="det(A) = ":
            anser=[A.det()]
            anser_r=Ar
            anser_c=Ac
            output_type="NUMBER"

        elif type=="rank(A) = ":
            anser=[A.rank()]
            anser_r=Ar
            anser_c=Ac
            output_type="NUMBER"

        elif type=="tr(A) = ":
            anser=[A.trace()]
            anser_r=Ar
            anser_c=Ac
            output_type="NUMBER"

        elif type=="λ = ":
            A=A.eigenvals()
            anser=[]
            for B in A.items():
                anser.append("λ="+str(B[0])+" (重複度="+str(B[1])+")")
            anser_r=Ar
            anser_c=Ac
            type=""
            output_type="NUMBER"

        elif type=="P = ":
            A=A.diagonalize()
            A=list(A)
            anser=A[0]
            anser_r=Ar
            anser_c=Ac
            output_type="MATRIX"

        elif type=="P^-1AP = ":
            A=A.diagonalize()
            A=list(A)
            anser=A[1]
            anser_r=Ar
            anser_c=Ac
            output_type="MATRIX"
    except:
        anser=["Error"]
        anser_r=""
        anser_c=""
        type=""
        output_type="NUMBER"
        flash("エラー：もう一度入力してください")

    if(output_type=="MATRIX"):
        anser_2=[]
        for i in range(anser_r):
            A=anser.row(i)
            anser_2.append([])
            for j in range(anser_c):
                anser_2[i].append(A[j])
        
        anser_3 = "\\begin{pmatrix} "
        for i in range(anser_r):
            anser_3+=LATEX(anser_2[i][0])
            for j in range(anser_c-1):
                anser_3+="&"+LATEX(anser_2[i][j+1])
                anser_3+=" \\"+"\ "
        anser_3+=" \end{pmatrix}"

    Anser=[anser_3,anser_r,anser_c,type,output_type]
    return Anser
