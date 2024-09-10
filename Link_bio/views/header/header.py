import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Abel Gomez", size="xl"),
        rx.text("abelgomez"),
        rx.text("HOLA MI NOMBRE ES ABEL GOMEZ MENDEZ"),
        rx.text("""Soy ingeniero en telecomunicaciones, desarrollador web
                 y cientifico de datos. Aquí podrás encontrar los 
                enlaces a mis redes sociales""")
    )