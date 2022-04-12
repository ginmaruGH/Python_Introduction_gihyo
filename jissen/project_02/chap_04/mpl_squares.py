import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# グラフのタイトルと軸のラベルを設定する
ax.set_title("Square Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 目盛りラベルのスタイルを設定する
ax.tick_params(axis='both', labelsize=14)

plt.show()
