import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div([
    dcc.Upload(id='upload', children=html.Button('Upload an image')),
    html.Img(id='image', width=500)
])


# Preview image or video after taking without sending to the server. This is
# helpful because the app is much slower if you send content to the server
# first.
app.clientside_callback(
    """
    function(contents) {
        // document.write(contents)
        if (contents === undefined) {
            return "";
        } else {
            return contents;
        }
    }
    """,
    Output('image', 'src'),
    Input('upload', 'contents')
)


if __name__ == "__main__":
    app.run_server(debug=True)