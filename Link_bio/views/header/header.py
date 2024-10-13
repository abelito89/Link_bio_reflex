import reflex as rx
from Link_bio.components.title import title
from Link_bio.components.link_icon import link_icon
from Link_bio.styles.styles import Size as Size
from Link_bio.styles.colors import Color

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Abel Gomez", 
                size="2xl", 
                src="avatar.jpg",
                padding = "0px",
                border="4px solid #6064f9",
                border_radius="50%",  # Convertir el avatar en un círculo
                ),
            rx.vstack(
                title("ABEL GÓMEZ MÉNDEZ"),
                rx.text("abelito89",
                        margin_top = "0px !important"
                        ),
                link_icon("https://github.com/abelito89"),
                align_items="flex-start",  # Alinear el texto al inicio
                justify_content="center",  # Centrar el texto verticalmente dentro de la vstack
                spacing=Size.SMALL.value,
            ),
            align_items="center",  # Alinear el avatar con el texto en el centro
            spacing="20px",
            width="100%", 
        ),
         rx.text("""Soy ingeniero en telecomunicaciones, desarrollador web
                 y cientifico de datos. Aquí podrás encontrar los 
                enlaces a mis redes sociales"""),
        spacing=Size.BIG.value  
        )
        
