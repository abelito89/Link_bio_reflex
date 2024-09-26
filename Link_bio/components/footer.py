import reflex as rx
import datetime
from Link_bio.styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"2022-{datetime.date.today().year} Abelito",
            href="https://www.linkedin.com/in/abelgomezmendez/",
            is_external=True
        ),
        rx.text("Desarrollador de Python"),
        margin_botton = Size.BIG.value
    )