import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"2022-{datetime.date.today().year} Abelito",
            href="https://www.linkedin.com/in/abelgomezmendez/",
            is_external=True
        ),
        rx.text("Desarrollador de Python")
    )