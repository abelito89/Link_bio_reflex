import reflex as rx
import datetime
from Link_bio.styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.vstack(
        rx.spacer(margin_top="70px"),
        rx.image(src="IA.ico"),
        rx.link(
            f"2022-{datetime.date.today().year} Abelito",
            href="https://www.linkedin.com/in/abelgomezmendez/",
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.text("Desarrollador de Python",
                font_size=Size.MEDIUM.value),
        margin_botton = Size.BIG.value
    )