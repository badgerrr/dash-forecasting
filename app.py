import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
            Dash: A web application framework for Python.
        '''),

    html.Label('Slider'),
    dcc.Slider(
        id='myslider',
        min=-10,
        max=10,
        step=1,
        marks={i: '{}'.format(i) for i in range(-10, 11) if i % 1 == 0},
        value=0,
    ),
    dcc.Graph(
        id='example-graph'
    ),
    dcc.Graph(
        id='example-graph2'
    ),
    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF'],
        multi=True
    ),
    html.Label('Radio Items test'),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),
])


def main():
    app.run_server(host='0.0.0.0',debug=True)


@app.callback(
    inputs=[Input(component_id='myslider', component_property='value')],
    output=Output(component_id='example-graph2', component_property='figure')
)
def dynamic_graph(slider_value):
    return {
        'data': [
            {'x': [1, 2, 3], 'y': [int(slider_value), 1, 2], 'name': 'SF', 'marker': {'color': 'rgb(26, 118, 255)'}},
            {'x': [1, 2, 3], 'y': [2, 4, 5], 'name': u'Montréal', 'marker': {'color': 'rgb(55, 83, 109)'}},
        ],
        'layout': {
            'title': 'Dash Data Visualization'
        }
    }

@app.callback(
    inputs=[Input(component_id='myslider', component_property='value')],
    output=Output(component_id='example-graph', component_property='figure')
)
def dynamic_graph(slider_value):
    return {
        'data': [
            {'x': [1, 2, 3], 'y': [int(slider_value), 1, 2], 'type': 'bar', 'name': 'SF'},
            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
        ],
        'layout': {
            'title': 'Dash Data Visualization'
        }
    }


if __name__ == '__main__':
       main()
