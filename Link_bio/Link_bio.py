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
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
        header(),
        title("Redes sociales"),
        links(),
        footer(),
        max_width=styles.MAX_WIDTH, # le da al componente(vstack en este caso) un ancho máximo
        width = "100%", # hace que el contenido interno del componente ocupe el 100% del espacio en el ancho
        margin_y = styles.Size.BIG.value # le da un margen en el eje hacia fuera del componente   
    )

        )
        
    
    )

app = rx.App(
    styles = styles.BASE_STYLE
)
app.add_page(index)
app._compile