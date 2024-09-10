import reflex as rx
from Link_bio.components.navbar import navbar
from Link_bio.views.header.header import header
from Link_bio.views.links.links import links
from Link_bio.components.footer import footer

class State(rx.State):
    pass

def index()->rx.Component:
    # componente de diseño utilizado para 
    # agrupar elementos y apilarlos verticalmente
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer()
    )    

app = rx.App()
app.add_page(index)
app._compile