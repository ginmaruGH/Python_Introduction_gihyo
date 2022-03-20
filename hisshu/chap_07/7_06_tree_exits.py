# 7-6.3つの出口
print("\n# 7-6.3つの出口\n")

prompt = "\n何歳ですか？"
prompt += "\n終わったら、'終了'と入力してください。>> "

active = True
while active:
    age = input(prompt)
    if age == '終了':
        break

    age = int(age)
    if age < 3:
        print(" チケット料金は無料です。")
    elif age < 13:
        print(" チケット料金は1,000円です。")
    elif age < 19:
        print(" チケット料金は1,500円です。")
    else:
        print(" 19歳以上は対象外です。終了します。")
        active = False
