import flask

def test_create_app():
    app = flask.Flask(__name__)
    assert app is not None

def test_app_name():
    app = flask.Flask("test_app")
    assert app.name == "test_app"

def test_route_decorator():
    app = flask.Flask(__name__)

    @app.route("/")
    def home():
        return "Hello"

    assert "/" in [rule.rule for rule in app.url_map.iter_rules()]

def test_test_client():
    app = flask.Flask(__name__)

    @app.route("/")
    def home():
        return "Hello World"

    client = app.test_client()
    response = client.get("/")
    assert response.data == b"Hello World"

def test_status_code():
    app = flask.Flask(__name__)

    @app.route("/")
    def home():
        return "OK"

    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
