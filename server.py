from flask import Flask
from flask_cors import CORS
from flask import send_file
from flask import request
from math import floor
import string
from urllib.parse import urlparse
import LinkShortener

host = 'https://link-short-light.herokuapp.com/'

app = Flask(__name__)
CORS(app)

short_url = LinkShortener()

@app.route('/')
def hello():
    return send_file('./index.html')

@app.route('/url', methods=['POST'])
def parse_url():
    url = request.form.get('url')
    my_short_url = short_url.shorten_url(url)
    return my_short_url

@app.route('/decode/<_id>')
def decode_url(_id):
    my_long_url = short_url.base62_decoder(_id)
    html = """
    <!DOCTYPE html>
        <html lang="en">
            <head>
                <script>
                    window.open('{}');
                </script>
            </head>
            <body>
            </body>
        </html>
    """.format(my_long_url)
    return html

if __name__ == '__main__':
    app.run()
