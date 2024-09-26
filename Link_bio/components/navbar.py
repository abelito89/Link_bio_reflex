import reflex as rx
from Link_bio.styles.styles import Size as Size

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Abelito",
        ),
        #propiedad que deja el componente fijo, sin moverse
        position = "sticky",
        #pinta de azul el componente, en este caso, todo el hstack
        bg = "blue",
        #crea espacio adicional dentro de un elemento, entre su contenido y su borde
        padding_x = Size.DEFAULT.value,
        padding_y = Size.SMALL.value,
        z_index = "999",
        top = "0"
    )