import reflex as rx

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Budget Beacon", size="9"),
            rx.text(
                "To smarter spending, saving, and growing your wealth!",
                size="5",
            ),
            rx.link(
                rx.button("Start here!"),
                href="/login",
                is_external=False,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )