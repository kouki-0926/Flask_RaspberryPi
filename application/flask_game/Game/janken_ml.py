# -*- coding: utf-8 -*-
import numpy as np
from sklearn.linear_model import Perceptron
from flask import flash

# ====1.分類器に入力するデータの準備=============================
# じゃんけんの手のベクトル形式を格納した配列。入力データとして用いる
# グー [1, 0, 0], チョキ [0, 1, 0], パー [0, 0, 1]
janken_array = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])


# じゃんけんの過去の手の初期化
# 過去何回分の手を覚えるか
n = 3
# 過去の人間の手とコンピュータの手をそれぞれn回分用意
ch_prev = np.zeros(3*n*2)
# 過去の手(ベクトル形式)をランダムに初期化
for i in range(2*n):
    ch_prev[3*i:3*i+3] = janken_array[np.random.randint(0, 3)]
# 過去の手(入力データ)をscikit_learn用の配列に変換
ch_prev_set = np.array([ch_prev])


# 今回の手(0～2の整数)をランダムに初期化
j = np.random.randint(0, 3)
# 今回の手(ターゲット)をscikit_learn用の配列に変換
h_now_set = np.array([j])


# ====2.機械学習の実行=============================
# 単純パーセプトロンを定義
clf = Perceptron(random_state=None)

# ランダムな入力でオンライン学習を1回行う。
# 初回の学習では、あり得るターゲット(0, 1, 2)を分類器に知らせる必要がある
clf.partial_fit(ch_prev_set, h_now_set, classes=[0, 1, 2])


# ====3.機械学習の結果の表示と評価=============================
def janken_ml(h_choice, result):
    global ch_prev, ch_prev_set, total
    h_choice -= 1
    if(h_choice < 0 or h_choice > 2):
        flash("0,1,2を入力してください")

    # 過去のじゃんけんの手(ベクトル形式)をscikit_learn形式に
    ch_prev_set = np.array([ch_prev])
    # 今回のじゃんけんの手(0～2の整数)をscikit_learn形式に
    h_now_set = np.array([h_choice])

    # コンピュータが、過去の手から人間の今回の手を予測
    h_predict = clf.predict(ch_prev_set)
    # 予測を元にコンピュータが決めた手
    # 予測がグーならパー、予測がチョキならグー、予測がパーならチョキ
    c_choice = (h_predict[0] + 2) % 3


    Anser = [[h_choice+1, c_choice+1], [], result]
    if (c_choice == h_choice):
        Anser[2][2] += 1
        Anser[1].append("あいこ")
    elif ((c_choice - h_choice == -2) or (c_choice - h_choice == 1)):
        Anser[2][0] += 1
        Anser[1].append("あなたの勝ち")
    else:
        Anser[2][1] += 1
        Anser[1].append("あなたの負け")

    total = 0
    for i in range(3):
        total += Anser[2][i]

    Anser[1].append("勝ち　: {}回, {}%".format(Anser[2][0], round(Anser[2][0]/total*100, 1)))
    Anser[1].append("負け　: {}回, {}%".format(Anser[2][1], round(Anser[2][1]/total*100, 1)))
    Anser[1].append("あいこ: {}回, {}%".format(Anser[2][2], round(Anser[2][2]/total*100, 1)))


    # 過去の手(入力データ)と今回の手(ターゲット)とでオンライン学習
    clf.partial_fit(ch_prev_set, h_now_set)
    # 過去の手の末尾に今回のコンピュータの手を追加
    ch_prev = np.append(ch_prev[3:], janken_array[c_choice])
    # 過去の手の末尾に今回の人間の手を追加
    ch_prev = np.append(ch_prev[3:], janken_array[h_choice])
    return Anser