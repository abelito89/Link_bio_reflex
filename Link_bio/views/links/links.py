import reflex as rx
from Link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Facebook","https://www.facebook.com/profile.php?id=100009278560441"),
        link_button("LinkedIn","https://www.linkedin.com/in/abelgomezmendez/"),
        link_button("Twitter","https://twitter.com/Abelito_Metal")  
    )