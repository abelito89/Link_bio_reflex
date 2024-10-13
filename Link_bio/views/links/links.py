import reflex as rx
from Link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Facebook","Perfil de Facebook de Abel", "icons/icons8-facebook.svg","https://www.facebook.com/profile.php?id=100009278560441"),
        link_button("LinkedIn","Perfil de LinkedIn de Abel", "icons/icons8-linkedin.svg","https://www.linkedin.com/in/abelgomezmendez/"),
        link_button("Twitter","Perfil de Twitter de Abel", "icons/icons8-twitterx.svg","https://twitter.com/Abelito_Metal"),
        width = "100%"  
    )