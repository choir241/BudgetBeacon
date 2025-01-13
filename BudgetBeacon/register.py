import reflex as rx

class FormState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data:dict):
        """Handle the form submit."""
        self.form_data = form_data
        print(self.form_data)

def register() -> rx.Component:
        return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Sign up", size="9"),
            rx.form(
                rx.input(
                        type="text", 
                        placeholder="Your name",
                        name="name",
                        id="name"
                ),
                rx.input(
                        type="email",
                        name="email",
                        placeholder="Your email",
                        id="email"
                ),
                rx.input(
                        type="password", 
                        name="password",
                        placeholder="Your password",
                        id="password"
                ),
                rx.button(
                    "Submit",
                    type="submit"
                ),
            on_submit=FormState.handle_submit,
            ),
            rx.vstack(
                rx.text("Already have an account? ",
                        rx.link("Login here!",
                            href="/login",
                            is_external=False,
                        ),
                ),
                justify="center",
                display="flex"
            ),
        )
    ),
