from plotly.graph_objs import Bar, Layout
from plotly import offline

days = [2,4,6]
score = [12,12,11]
# Visualize the results.
data = [Bar(y=score, x=days)]

x_axis_config = {'title': 'Days'}
y_axis_config = {'title': 'Score'}
my_layout = Layout(title='Memory flash score',
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='smart_goal.html')