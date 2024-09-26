import reflex as rx
from enum import Enum #crear enumeraciones, que son conjuntos de nombres simbólicos (miembros) vinculados a valores únicos

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
    rx.button:{
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding":Size.SMALL.value,
        "margin_y":Size.SMALL.value

    },
    rx.link:{
        "text_decoration":"none",
        "_hover":{}
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