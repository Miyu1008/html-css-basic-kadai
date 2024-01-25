for i in range(1,11):
    print(i)

#ループ変数の値が5であれば、break文で繰り返し処理を終了する
if i == 5:
    break   

#--------

#ランダム利用
import random
for i in range(1,11):
    #変数numに1〜20までのランダムな整数を代入
    num = random.randint(1,20)

print(f"{i}回目の結果は{num}です。")

#変数numの値が20であれば、break文で繰り返し処理を強制終了する
if num == 20:
    print("20が出たので繰り返し処理を強制終了します。")
    break

#------
for i in range(1,11):
#ループ変数iの値が奇数(2で割った余りが1)であれば、値を出力せずにcontinue文で次のループに進む
    if i % 2 == 1:
        continue
    print(i)  