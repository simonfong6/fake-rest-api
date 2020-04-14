#!/usr/bin/env python3
"""
Backend server.
"""
import logging

from flask import Flask
from flask import jsonify
from flask import render_template
from flask_cors import CORS

# Configure logging.
logging.basicConfig(filename='logs/server.log')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = Flask(__name__)

CORS(app)


@app.route('/')
def index():
    return render_template('index.html.jinja')

@app.route('/data')
def data():
    return jsonify({
        'eric': 'A+',
        'simon': 'C-',
        'derek': 'B',
        'isaac': 'A'
    })


def main(args):

    if args.debug:
        logger.setLevel(logging.DEBUG)

    app.run(
        host='0.0.0.0',
        debug=args.debug,
        port=args.port
    )


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()

    parser.add_argument('-p', '--port',
                        help="Port that the server will run on.",
                        type=int,
                        default=4321)
    parser.add_argument('-d', '--debug',
                        help="Whether or not to run in debug mode.",
                        default=False,
                        action='store_true')

    args = parser.parse_args()
    main(args)
