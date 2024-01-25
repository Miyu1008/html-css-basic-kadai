#ランダム利用
import random

#変数numに0〜4までのランダムな整数を代入
num = random.randint(0,4)
#変数numの最初の値を出力する（確認用）
print(f"最初の値は{num}です。")

#変数numの値が0以外である場合、変数numの値を出力し続ける
while num != 0:
    num = random.randint(0,4)
    #次の条件式で比較される、変数numの現在の値を出力する
    print(f"現在の値は{num}です。")

#-------
#ランダム利用
import random
#変数numに0〜4までのランダム代入
num = random.randint(0,4)
#カウンタ変数を用意する
i = 1
#変数numの最初の値を出力する（確認）
print(f"最初の値は{num}です。")
#変数numの値が0以外である間、変数numの値を出力し続ける
while num != 0:
    #変数numに0〜4までのランダムな整数を代入する
    num = random.randint(0,4)
    #カウンタ変数iの値が5であれば、break文で繰り返し処理を強制終了する
    if i == 5:
        print("5回目なので繰り返し処理を強制終了します。")
        break
    #次の条件式で比較される、変数numの現在の値を出力する
    print(f"現在の値は{num}です。")
    #カウンタ変数の値を1増やす
    i = i + 1