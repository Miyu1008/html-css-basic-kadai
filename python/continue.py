#ランダム利用
import random
#合計用の変数を用意
sum = 0
#変数sumの値が20以上になるまで繰り返し処理を行う
while sum < 20:
    #変数numに1〜10までのランダムな整数を代入する
    num = random.randint(1,10)

    print(f"{num}が出ました。")

    #変数numの値が偶数(2で割った余りが0)であれば、加算せずにconteinue文で次のループに進む
    if num % 2 == 0:
        print("偶数なので加算しません。")
        continue
    
    #変数sumに変数numの値を加算する
    sum = sum + num
    print(f"現在の合計は[sum]です")