from random import uniform
from flask import flash


result = [0, 0, 0]
result_2 = [0, 0, 0]
total = 0


def janken(n):
    try:
        global total
        te = ["グー", "チョキ", "パー"]
        nc = int(uniform(0, 100)) % 3+1

        Anser = ["君は["+str(te[n-1])+"]か。"]

        if (nc == n):
            Anser.append("俺も["+te[nc - 1]+"]だ。あいこだな。")
            result[2] += 1
        elif ((nc - n == -2) or (nc - n == 1)):
            Anser.append("俺は["+te[nc - 1]+"]だ。君の勝ちだな。")
            result[0] += 1
        else:
            Anser.append("俺は["+te[nc - 1]+"]だ。俺の勝ちだな。")
            result[1] += 1

        total += 1
        for i in range(3):
            result_2[i] = round(result[i]/total*100, 1)

        Anser.append("勝ち　: {}回, {}%".format(result[0], result_2[0]))
        Anser.append("負け　: {}回, {}%".format(result[1], result_2[1]))
        Anser.append("あいこ: {}回, {}%".format(result[2], result_2[2]))
    except:
        Anser = ["Error"]
        flash("Error")
    return Anser


def janken_reset():
    global result, total
    result = [0, 0, 0]
    total = 0
