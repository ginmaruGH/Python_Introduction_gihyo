from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# 2つの8面サイコロを作成する
die_1 = Die(num_sides=8)
die_2 = Die(num_sides=8)

# サイコロを転がし、結果をリストに格納する
results = []
for roll_num in range(1_000_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 結果を分析する
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# 結果を可視化する
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

plot_title = '2個の8面サイコロを1,000,000回転がした結果'
x_axis_config = {'title': '結果', 'dtick': 1}
y_axis_config = {'title': '発生した回数'}
my_layout = Layout(
    title=plot_title,
    xaxis=x_axis_config, yaxis=y_axis_config
)
offline.plot(
    {'data': data, 'layout': my_layout},
    filename='jissen/project_02/chap_04/lti_4_6_d8_d8.html'
)
