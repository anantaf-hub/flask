import flask

def test_flask_import():
    assert flask is not None

def test_flask_version():
    assert hasattr(flask, "__version__")
