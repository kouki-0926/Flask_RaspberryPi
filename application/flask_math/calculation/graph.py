from sympy import *
from sympy.plotting import plot,plot3d
from flask import flash

x,y=symbols('x y')

def graph(Formula,Lower_end,Upper_end,dimension,number):
    try:
        Formula=sympify(Formula)
        lower_end_x=sympify(Lower_end[0])
        upper_end_x=sympify(Upper_end[0])
        if number=="1":
            if dimension=="2D":
                plot(Formula[0],(x,lower_end_x,upper_end_x),legend=True)
            elif dimension=="3D":
                lower_end_y=sympify(Lower_end[1])
                upper_end_y=sympify(Upper_end[1])
                plot3d(Formula[0],(x, lower_end_x, upper_end_x),(y, lower_end_y, upper_end_y))
        elif number=="2":
            if dimension=="2D":
                plot(Formula[0],Formula[1],(x,lower_end_x,upper_end_x),legend=True)
            elif dimension=="3D":
                lower_end_y=sympify(Lower_end[1])
                upper_end_y=sympify(Upper_end[1])
                plot3d(Formula[0],Formula[1],(x, lower_end_x, upper_end_x),(y, lower_end_y, upper_end_y))
    except:
        flash("エラー：もう一度入力してください")
