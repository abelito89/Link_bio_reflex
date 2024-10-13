
# Link Bio Project

Este es un proyecto desarrollado con [Reflex](https://reflex.dev/), que permite la creación de una página web donde se muestran los enlaces a las redes sociales de un usuario, junto con un avatar y una pequeña descripción. El diseño de la página es simple y responsivo, apilando los elementos verticalmente en la pantalla.

## Estructura del Proyecto

El proyecto sigue una estructura modular organizada de la siguiente forma:

```plaintext
Link_bio/
│
├── assets/
│   └── icons/
│       └── avatar.jpg       # Imagen del avatar del usuario
│
├── Link_bio/
│   ├── components/
│   │   ├── footer.py        # Componente para el pie de página
│   │   ├── info_text.py     # Componente para el texto informativo
│   │   ├── link_button.py   # Componente para los botones con enlaces
│   │   ├── link_icon.py     # Componente para los iconos de los enlaces
│   │   ├── navbar.py        # Componente de la barra de navegación
│   │   └── title.py         # Componente para el título principal
│   │
│   ├── styles/
│   │   ├── colors.py        # Archivo que contiene los colores utilizados
│   │   ├── styles.py        # Archivo que define los estilos base y tamaños
│   │
│   └── views/
│       ├── header.py        # Vista del encabezado con avatar y descripción
│       ├── links.py         # Vista con los enlaces a las redes sociales
│
├── Link_bio_reflex/          # Archivos de Reflex generados automáticamente
├── venv/                     # Entorno virtual de Python
├── requirements.txt          # Dependencias del proyecto
└── README.md                 # Archivo de documentación
```
Requisitos
Para ejecutar este proyecto, necesitas tener instalados los siguientes paquetes de Python, que están especificados en el archivo requirements.txt:

```plaintext
Copiar código
reflex == 0.5.10
```
## Instalación
1. Clonar el repositorio:

```
git clone https://github.com/abelito89/Link_bio_reflex.git
cd link_bio_reflex
```
2. Crear un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate     # En Windows
```
3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```
## Estructura de Código
El archivo principal del proyecto es Link_bio.py, que contiene la lógica para generar la página web. A continuación se describe su funcionamiento:

### <span style="background-color: #343a40; padding: 2px 4px; border-radius: 3px;">index()</span> - Página Principal

Esta función define el diseño principal de la página, agrupando diferentes componentes dentro de un vstack. Los elementos incluidos son:

* <span style="background-color: #343a40; padding: 2px 4px; border-radius: 3px;">navbar()</span>: Barra de navegación en la parte superior. 

* <span style="background-color: #343a40; padding: 2px 4px; border-radius: 3px;">header()</span>
: Sección que contiene el avatar del usuario y su nombre. 

* <span style="background-color: #343a40; padding: 2px 4px; border-radius: 3px;">title()</span>
: Título que introduce la sección de enlaces a redes sociales.   
* <span style="background-color: #343a40; padding: 2px 4px; border-radius: 3px;">links()</span>
: Componente que lista los enlaces a redes sociales.   
* <span style="background-color: #343a40; padding: 2px 4px; border-radius: 3px;">footer()</span>
: Pie de página.  
## Ejemplo de Código:
```python
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                title("Redes sociales"),
                links(),
                rx.spacer(height="500px"),
                footer(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value
            )
        )
    )
```
## Estilos
El proyecto utiliza un archivo styles.py que contiene los estilos base y las constantes para los tamaños, facilitando la consistencia visual en toda la aplicación. Por ejemplo:

```python
MAX_WIDTH = "600px"
```

## Ejecución
Para ejecutar la aplicación:

```bash
reflex init
reflex run
```
La aplicación se compilará automáticamente y estará lista para servirse en un entorno local.

## Personalización
Puedes modificar los siguientes archivos para personalizar la página:

* <span style="background-color: #343a40; padding: 2px 4px; border-radius: 3px;">avatar.jpg</span>
: Cambia la imagen del avatar.
 
* <span style="background-color: #343a40; padding: 2px 4px; border-radius: 3px;">header.py</span>
: Ajusta el nombre y la descripción del usuario.  
* <span style="background-color: #343a40; padding: 2px 4px; border-radius: 3px;">links.py</span>
: Agrega o edita los enlaces a redes sociales.  
## Créditos  
Este proyecto fue desarrollado por Abel Gómez.