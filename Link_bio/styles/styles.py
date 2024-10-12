import reflex as rx
from enum import Enum #crear enumeraciones, que son conjuntos de nombres simbólicos (miembros) vinculados a valores únicos
from .colors import Color as Color
from .colors import TextColor as TextColor

# Debugging: Imprime los valores de los colores
print("Color Values:")
print(f"PRIMARY: {Color.PRIMARY.value}")
print(f"SECONDARY: {Color.SECONDARY.value}")
print(f"BACKGROUND: {Color.BACKGROUND.value}")
print(f"CONTENT: {Color.CONTENT.value}")

#Constants
MAX_WIDTH = "600px"


#Sizes
#Ayuda a mantener dimensiones proporcionales para que sea responsiva
class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"

#Styles, se configura en el lanzamiento de la app

BASE_STYLE = {
    "background_color": f"{Color.BACKGROUND.value} !important",
    "button": {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "margin_y": Size.SMALL.value,
        "color": f"{Color.CONTENT.value} !important",  # Color del texto del botón
        "background_color": f"{Color.CONTENT.value} !important",  # Color de fondo
        "border": "2px solid transparent",  # Elimina el borde predeterminado
        "outline": "none",  # Elimina el contorno en el focus
        "_hover": {
            "background_color": f"{Color.SECONDARY.value} !important",  # Cambia el color al hacer hover
        },
        "_focus": {
            "outline": "none",  # Asegúrate de que no haya contorno en el focus
        }
    },
    "link": {
        "text_decoration": "none",
        "_hover": {},
        "border": "none",  # Elimina el borde del enlace
        "outline": "none",
    }
}


button_title_style = dict(
    font_size = Size.DEFAULT.value
)

button_body_style = dict(
    font_size = Size.MEDIUM.value
)

title_style = dict(
    Size="lg",
    width="100%",
    padding_top = Size.DEFAULT.value
)