import flask


app = flask.Flask(__name__, template_folder='.')


@app.route('/')
def test():
    return flask.jsonify({"test": True})


if __name__ == '__main__':
    app.run('0.0.0.0', port=13300)
