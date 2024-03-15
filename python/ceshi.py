import plotly.io as pio

fig = {
    'data': [
        {
            'type': 'bar',
            'x': [1, 2, 3],
            'y': [1, 3, 2]
        }
    ],
    'layout': {
        'title': {
            'text': 'Python 字典指定的图形'
        }
    }
}
# 要显示该字典定义的图，请使用低级的 plot .io.show 函数
pio.show(fig)