import reflex as rx
import Link_bio.styles.styles as styles

def title(text:str):
    return rx.heading(
        text,
        style=styles.title_style
)