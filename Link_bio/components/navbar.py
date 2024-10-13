import reflex as rx
from Link_bio.styles.styles import Size as Size
from Link_bio.styles.colors import Color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "abelito",
            style={
                "font_family": "Tahoma",
                "font-weight": "bold",
                "font-style": "italic" 
            }
        ),
        #propiedad que deja el componente fijo, sin moverse
        position = "sticky",
        #pinta de azul el componente, en este caso, todo el hstack
        bg = Color.CONTENT.value,
        #crea espacio adicional dentro de un elemento, entre su contenido y su borde
        padding_x = Size.BIG.value,
        padding_y = Size.MEDIUM.value,
        z_index = "999",
        top = "0"
    )