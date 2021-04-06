from flask import make_response
from flask_math.calculation.common.STR import LATEX
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from sympy import *
import numpy as np
from io import BytesIO


def graph(formula_1, lower_end_x, upper_end_x):
    x = symbols('x')
    formula_1 = sympify(formula_1)
    lower_end_x = float(lower_end_x)
    upper_end_x = float(upper_end_x)

    # データ作成
    t = np.linspace(lower_end_x, upper_end_x, 300)
    if(diff(formula_1, x) == 0):
        y = lambdify(x, formula_1, "numpy")(lower_end_x)*np.ones(300)
    else:
        y = lambdify(x, formula_1, "numpy")(t)

    fig = plt.figure(figsize=(7, 4))
    plt.plot(t, y)
    plt.title("$f(x)="+LATEX(formula_1)+"("+str(lower_end_x)+"<x<"+str(upper_end_x)+")$")
    # canvasにプロットした画像を出力
    canvas = FigureCanvasAgg(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    data = png_output.getvalue()
    # HTML側に渡すレスポンスを生成する
    response = make_response(data)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Length'] = len(data)
    return response
