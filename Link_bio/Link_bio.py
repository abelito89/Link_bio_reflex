import reflex as rx
from Link_bio.components.navbar import navbar
from Link_bio.views.header.header import header
from Link_bio.components.title import title 
from Link_bio.views.links.links import links
from Link_bio.components.footer import footer
import Link_bio.styles.styles as styles

class State(rx.State):
    pass

def index()->rx.Component:
    # componente de diseño utilizado para 
    # agrupar elementos y apilarlos verticalmente
    print("Rendering index...")
    box = rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                title("Redes sociales"),
                links(),
                rx.spacer(height="500px"),
                footer(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value
            )
        )
    )

    # Debugging: Print Box Properties
    print("Box Properties:")
    print(f"Max Width: {styles.MAX_WIDTH}")
    print(f"Margin Y: {styles.Size.BIG.value}")

    return box

app = rx.App(
    styles = styles.BASE_STYLE
)
# Debugging: Print Base Style
print("Base Style:")
print(styles.BASE_STYLE)
app.add_page(index)
app._compile