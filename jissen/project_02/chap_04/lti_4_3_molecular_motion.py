import matplotlib.pyplot as plt

from random_walk import RandomWalk

# プログラムが動作している間、新しいランダムウォークを作成し続ける
while True:
    # ランダムウォークを作成する
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # ランダムウォークの点を描画する
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=1, zorder=1)

    # 開始点と終了点を強調する
    # zorder引数を指定して、折れ線グラフの前に点を表示する
    ax.scatter(0, 0, c='green', edgecolors='none', s=100, zorder=2)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100, zorder=2)

    # グラフのタイトルと軸のラベルを設定する
    ax.set_title("Let's Try It! 4-3.Molecular motion", fontsize=24)

    # 軸を削除する
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)

    plt.savefig(
        'jissen/project_02/chap_04/lti_4_3_molecular_motion.png',
        bbox_inches='tight'
    )
    plt.show()

    keep_running = input("別のランダムウォークを生成しますか？（y/n）>> ")
    if keep_running == 'n':
        break
