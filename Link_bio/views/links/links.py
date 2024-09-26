import reflex as rx
from Link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Facebook","Perfil de Facebook de Abel","https://www.facebook.com/profile.php?id=100009278560441"),
        link_button("LinkedIn","Perfil de LinkedIn de Abel","https://www.linkedin.com/in/abelgomezmendez/"),
        link_button("Twitter","Perfil de Twitter de Abel","https://twitter.com/Abelito_Metal"),
        width = "100%"  
    )