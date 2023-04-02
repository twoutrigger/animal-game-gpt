import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import time
import os
import random
from PIL import Image


class CustomDash(dash.Dash):
    def interpolate_index(self, **kwargs):
        return '''
        <!DOCTYPE html>
        <html>
            <head>
                <title>Placeholder</title>
                {metas}
                <link rel="canonical" href="https://www.liam.com/">
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
                <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
            </head>
            <body>
            <div><H1 style="font-family:Garamond;text-align:center;color:#2A3439;padding:10px;">Placeholder</H1></div>
            <br>
            {app_entry}
            {config}
            {scripts}
            {renderer}
            </body>
        </html>
        '''.format(
            metas=kwargs['metas'],
            app_entry=kwargs['app_entry'],
            config=kwargs['config'],
            scripts=kwargs['scripts'],
            renderer=kwargs['renderer'],
        )


meta_tags = [
    {'http-equiv': 'X-UA-Compatible', 'content': 'ie=edge'}, {'name': 'viewport',
                                                              'content': 'width=device-width, initial-scale=1.0'},
    {'name': 'description', 'content': 'Postcode Perimeter Check'},
    {'property': 'og:url', 'content': ''}, {
        'property': 'og:type', 'content': 'website'},
]

app = CustomDash(__name__, meta_tags=meta_tags, show_undo_redo=False)  # DASH
server = app.server

################################################

body = dbc.Container([

    dbc.Row([

        dbc.Col([], sm=3),

        dbc.Col([

            html.Br(),
            html.Br(),

            # html.Img(id='output-img'),

            html.Br(),
            html.Br(),

            dbc.Button('Placeholder', id='input-button', size="lg",
                style={'backgroundColor': '#B59DFA', 'color': '#013218', 'font-weight': 'bold'}),

            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),

            dcc.Loading(
                id="loading-1",
                type="default",
                children=[html.H3(id='output-text',
                                  style={'color': '#013218', 'font-weight': 'bold'})]
            ),

            html.Br(),

        ], sm=6),

        dbc.Col([], sm=3),

    ]),

    dbc.Row([
    
        dbc.Col([], sm=3),

        dbc.Col([
    
            dbc.Button('Rock', id='input-rock-button', size="lg",
                style={'backgroundColor': '#B59DFA', 'color': '#013218', 'font-weight': 'bold'})

        ], sm=2),

        dbc.Col([
    
            dbc.Button('Paper', id='input-paper-button', size="lg",
                style={'backgroundColor': '#B59DFA', 'color': '#013218', 'font-weight': 'bold'})

        ], sm=2),

        dbc.Col([
    
            dbc.Button('Scissors', id='input-scissors-button', size="lg",
                style={'backgroundColor': '#B59DFA', 'color': '#013218', 'font-weight': 'bold'})

        ], sm=2),

        dbc.Col([], sm=3)
    
    ]),

], className="mt-4", fluid=True)

app.layout = html.Div([body], style={
    'font-family': 'Garamond',
    # 'font-family': 'monospace',
    # 'font-family': 'sans-serif',
    'text-align': 'center',
    'margin': 'auto',
})

################################################


# @app.callback(
#     Output('output-img', 'children'),
#     Input('input-button', 'n_clicks')
# )
# def output_image(n_clicks):

#     image_path = 'assets/placeholder.jpg'

#     pil_image = Image.open(image_path)
    
#     return pil_image


@app.callback(
    Output('output-text', 'children'),
    [Input('input-button', 'n_clicks'),
     Input('input-rock-button', 'n_clicks'),
     Input('input-paper-button', 'n_clicks'),
     Input('input-scissors-button', 'n_clicks')]
)
def update_text(n_clicks, n_rock_clicks, n__paper_clicks, n_scissors_clicks):

    if n_clicks is not None:

        # need randomizer for opponent's move
        # need to specify logic for move vs move
        # need to track state-of-play, i.e. pre move, post move

        random_entity = random.choice(['rock', 'paper', 'scissors'])

        print(random_entity)

        ret = 'Placeholder'

        if ret is not None:

            outputText = ret

        else:
            outputText = ''

    else:
        outputText = 'Placeholder'

    # print(n_clicks)
    # time.sleep(1)

    return outputText

################################################


if __name__ == '__main__':
    # app.run_server()  # FLASK
    app.run_server(debug=True, dev_tools_hot_reload=True)  # DASH
