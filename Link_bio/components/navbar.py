import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Abelito",
            height = "40px" #tamaño del texto
        ),
        #propiedad que deja el componente fijo, sin moverse
        position = "sticky",
        #pinta de azul el componente, en este caso, todo el hstack
        bg = "blue",
        #crea espacio adicional dentro de un elemento, entre su contenido y su borde
        padding_x = "16px",
        padding_y = "8px",
        z_index = "999"
    )