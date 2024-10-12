import reflex as rx
import Link_bio.styles.styles as styles

def link_button(title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow_right",
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing="0.1em",
                    align_items="start",
                    padding_y="0.1em"
                ),
                align_items="center"
            ),
            # Estilos inline explícitos
            style={
                "width": "100%",
                "height": "100%",
                "justify_content": "flex-start",
                "background_color": styles.Color.CONTENT.value,  # Color de fondo
                "color": styles.TextColor.HEADER.value,  # Color de texto
                "border": f"1px solid {styles.Color.CONTENT.value}",  # Borde igual que el color de fondo
            },
            _hover={"background_color": styles.Color.SECONDARY.value},  # Hover explícito
        ),
        href=url,
        is_external=True,
        width="100%",
        padding_y="0.1em",
        margin_y="0.1em"
    )
