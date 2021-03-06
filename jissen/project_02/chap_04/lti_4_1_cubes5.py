from matplotlib import pyplot as plt

# データを定義する
x_values = [1, 2, 3, 4, 5, 6]
cubes = [x**3 for x in x_values]

# プロットを作成する
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, cubes, edgecolor='none', s=40)

# グラフのタイトルと軸ラベルを設定する
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# 軸の目盛りラベルを設定する
ax.tick_params(axis='both', labelsize=14)

# グラフを表示する
plt.savefig(
    'jissen/project_02/chap_04/lti_4_1_cubes5.png'
)
plt.show()
