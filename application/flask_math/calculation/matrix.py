from sympy import *
from flask import flash
from flask_math.calculation.common.MATRIX import MATRIX
from flask_math.calculation.common.STR import LATEX

def calculation(matrixA,Ar,Ac,type):
    try:
        Ar,Ac=[int(Ar),int(Ac)]
        A=MATRIX(matrixA,Ar,Ac)

        if type=="A":
            anser=A
            anser_r=Ar
            anser_c=Ac
            output_type="MATRIX"

        elif type=="A^n":
            A=list(A.diagonalize())
            P=A[0]
            D=A[1]
            for i in range(0,Ac,1):
                D[i,i]="("+str(D[i,i])+")^n"
            anser=P*D*P.inv()
            anser_r=Ar
            anser_c=Ac
            output_type="MATRIX"

        elif type=="A^t":
            anser=A.transpose()
            anser_r=Ac
            anser_c=Ar
            output_type="MATRIX"

        elif type=="A^{-1}":
            anser=A.inv()
            anser_r=Ar
            anser_c=Ac
            output_type="MATRIX"

        elif type=="\widetilde{A}":
            anser=A.adjugate()
            anser_r=Ar
            anser_c=Ac
            output_type="MATRIX"

        elif type=="det(A)":
            anser=A.det()
            output_type="NUMBER"

        elif type=="rank(A)":
            anser=A.rank()
            output_type="NUMBER"

        elif type=="tr(A)":
            anser=A.trace()
            output_type="NUMBER"

        elif type=="λ":
            A=A.eigenvals()
            anser=""
            for B in A.items():
                anser+=LATEX(B[0])+"(重複度="+LATEX(B[1])+"), "
            output_type="NUMBER"

        elif type=="P":
            A=A.diagonalize()
            A=list(A)
            anser=A[0]
            anser_r=Ar
            anser_c=Ac
            output_type="MATRIX"

        elif type=="P^{-1}AP":
            A=A.diagonalize()
            A=list(A)
            anser=A[1]
            anser_r=Ar
            anser_c=Ac
            output_type="MATRIX"
    except:
        anser="Error"
        output_type="NUMBER"
        flash("エラー：もう一度入力してください")

    if(output_type=="MATRIX"):
        anser_2=[]
        for i in range(anser_r):
            A=anser.row(i)
            anser_2.append([])
            for j in range(anser_c):
                anser_2[i].append(A[j])
        
        anser_3="\\begin{pmatrix} "
        for i in range(anser_r):
            anser_3+=LATEX(anser_2[i][0])
            for j in range(anser_c-1):
                anser_3+="&"+LATEX(anser_2[i][j+1])
                anser_3+=" \\"+"\ "
        anser_3+=" \end{pmatrix}"
    elif(output_type=="NUMBER"):
        anser_3=anser

    return anser_3
