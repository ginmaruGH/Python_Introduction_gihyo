# 7-8.デリカテッセン
print("\n# 7-8.デリカテッセン\n")

sandwich_orders = ['ベジー', 'グリルチーズ', 'ターキー', 'ローストビーフ']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"{current_sandwich}サンドを調理中です。")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"ご注文の{sandwich}サンドができました。")
