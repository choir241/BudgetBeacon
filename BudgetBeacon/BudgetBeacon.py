"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from .register import register
from .login import login
from .index import index

class State(rx.State):
    """The app state."""

    ...

app = rx.App()
app.add_page(index)
app.add_page(login)
app.add_page(register)
