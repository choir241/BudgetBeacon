import reflex as rx
from .appwrite import login

class FormState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data:dict):
        """Handle the form submit."""
        self.form_data = form_data
        login(self.form_data)

def login() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Login", size="9"),
            rx.form(
                rx.input(
                        type="text", 
                        placeholder="Your email",
                        name="email",
                        id="email"
                ),
                rx.input(
                        type="password", 
                        placeholder="Your password",
                        name="password",
                        id="password"
                ),
                rx.button(
                    "Submit",
                    type="submit"
                ),
            on_submit=FormState.handle_submit,
            ),
            rx.vstack(
                rx.text("Don't have an account? ",
                        rx.link("Sign up here!",
                            href="/register",
                            is_external=False,
                        ),
                ),
                justify="center",
                display="flex"
            ),
        )
    ),