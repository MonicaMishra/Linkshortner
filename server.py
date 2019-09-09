from flask import Flask
from flask_cors import CORS
from flask import send_file
from flask import request
from math import floor
import string
from urllib.parse import urlparse
import LinkShortener

host = 'https://localhost:5000/' ## to run on local host

app = Flask(__name__)
CORS(app)

short_url = LinkShortener() ## create an object from the class

@app.route('/') ## first link pointer
def hello():
    return send_file('./index.html')

@app.route('/url', methods=['POST']) ## need to read the url from user and later shorten from shorten_url in class LinkShortener
def parse_url():
    url = request.form.get('url')
    my_short_url = short_url.shorten_url(url)
    return my_short_url

@app.route('/decode/<_id>') ## read the encoded url and open a new window to show that the decoded url is the same as the one provided originally
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

if __name__ == '__main__': ## run the main function
    app.run()
