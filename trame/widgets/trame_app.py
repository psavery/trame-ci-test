from trame_app.widgets.trame_app import *


def initialize(server):
    from trame_app import module

    server.enable_module(module)
