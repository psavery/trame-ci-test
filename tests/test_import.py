def test_import():
    from trame_app.widgets.trame_app import CustomWidget  # noqa: F401

    # For components only, the CustomWidget is also importable via trame
    from trame.widgets.trame_app import CustomWidget  # noqa: F401,F811
