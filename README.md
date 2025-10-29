# UDLA Sistema Perfumes

## Descripción

Aplicación web desarrollada en Django para la gestión de aromas y perfumes. Utiliza Bootstrap para los estilos y Bootstrap Icons para los íconos.

## Requisitos

- Python 3.10 o superior
- Django 4.x
- Base de datos SQL ya existente (ver carpeta `sql`)

## Instalación y configuración

1. **Instala Python 3.10 o superior**  
   Descárgalo desde [python.org](https://www.python.org/downloads/) si no lo tienes instalado.

2. **Crea y activa un entorno virtual:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Activa el modo desarrollador (opcional pero recomendado):**

   ```bash
   export DJANGO_SETTINGS_MODULE=udla_sistema_perfumes.settings
   export DEBUG=1
   ```

4. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Si no existen las apps necesarias, créalas:**

   ```bash
   python manage.py startapp aromas
   python manage.py startapp marcas
   python manage.py startapp generos
   python manage.py startapp perfumes
   ```

6. **Configura la base de datos en `settings.py`** con los datos de tu base ya creada.  
   No ejecutes migraciones para crear tablas, Django solo mapeará los modelos a las tablas existentes.

7. **Realiza las migraciones usando `--fake-initial` para mapear modelos a tablas existentes:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate --fake-initial
   ```

8. **Si necesitas crear o poblar la base de datos, utiliza los scripts que están en la carpeta `sql`.**

9. **Inicia el servidor de desarrollo:**

   ```bash
   python manage.py runserver
   ```

## Notas

- No ejecutes `python manage.py migrate` sin `--fake-initial` si ya tienes las tablas creadas, para evitar errores.
- Asegúrate de que tus modelos tengan `managed = False` en la clase Meta para evitar que Django gestione las tablas.
- Los scripts SQL para la base de datos están en la carpeta `sql`.
- La documentación generada del proyecto se encuentra en la carpeta `docs`.
- El proyecto utiliza Bootstrap 5 y Bootstrap Icons para la interfaz.

---

## Estructura y uso de la plantilla base (`base.html`)

El archivo `base.html` define la estructura principal de la interfaz. Incluye una barra lateral con enlaces de navegación a las diferentes apps del sistema:

```html
<div class="sidebar d-flex flex-column justify-content-between">
    <div class="menu-items">
        <h3>PERFUMERIA</h3>
        <hr>
        <a href="{% url 'lista_aromas' %}" class="{% if '/aromas' in request.path %}active{% endif %}">
            <i class="bi bi-droplet"></i> Aromas
        </a>
        <a href="{% url 'lista_generos' %}" class="{% if '/generos' in request.path %}active{% endif %}">
            <i class="bi bi-gender-ambiguous"></i> Géneros
        </a>
        <a href="{% url 'lista_marcas' %}" class="{% if '/marcas' in request.path %}active{% endif %}">
            <i class="bi bi-tags"></i> Marcas
        </a>
        <a href="{% url 'lista_perfumes' %}" class="{% if '/perfumes' in request.path %}active{% endif %}">
            <i class="bi bi-box-seam"></i> Perfumes
        </a>
    </div>
    <div class="menu-items">
        <hr>
        <a href="{% url 'logout' %}"><i class="bi bi-box-arrow-right"></i> Cerrar sesión</a>
    </div>
</div>
```

### Redirección a las diferentes apps

Cada enlace utiliza la etiqueta `{% url %}` de Django para redirigir a las vistas principales de cada app.  
Por ejemplo:

- Aromas: `{% url 'lista_aromas' %}`
- Géneros: `{% url 'lista_generos' %}`
- Marcas: `{% url 'lista_marcas' %}`
- Perfumes: `{% url 'lista_perfumes' %}`

Asegúrate de que en tus archivos `urls.py` de cada app existan las rutas con estos nombres para que la navegación funcione correctamente.

---
# 📸 Carga de Imágenes en Django

Paso a paso para habilitar la subida de **imagenes** en tu proyecto Django, y almacenarla la ruta en tu base de datos PostgreSQL.

---

## 🔧 1. Modelo

Asegúrate de que tu modelo incluya el campo `imagen` como un `ImageField`:

```python
imagen = models.ImageField(upload_to='perfumes/', blank=True)
```

Esto guarda las imágenes en la carpeta `media/perfumes/` dentro de tu proyecto.

---

## ⚙️ 2. Configuración en `settings.py`

Agrega estas configuraciones para que Django sepa dónde guardar y servir los archivos de imagen:

```python
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEBUG = True  # Solo en desarrollo
```

> ⚠️ **Nota**: `DEBUG = True` solo debe usarse en desarrollo para servir archivos estáticos y de medios.

---

## 🛣️ 3. URLs del proyecto (`urls.py`)

Agrega esta configuración para servir archivos en modo desarrollo:

```python
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 📝 4. Formulario

Define el formulario incluyendo el campo `imagen`:

```python
from django import forms
from .models import Perfumes

class PerfumesForm(forms.ModelForm):
    class Meta:
        model = Perfumes
        fields = ['nombre', 'id_aroma', 'id_marca', 'id_genero', 'tamanio', 'precio', 'imagen', 'estado']
        ...
```

---

## 🧠 5. Vista de creación

Agrega las vista para manejar el formulario y guardar la imagen:

```python
from django.shortcuts import render, redirect
from .forms import PerfumesForm

def crear_perfume(request):
    aromas = obtener_catalogo_aromas()
    marcas = obtener_catalogo_marcas()
    generos = obtener_catalogo_generos()

    if request.method == 'POST':
        form = PerfumesForm(request.POST, request.FILES)
    ...

def editar_perfume(request, pk):
    perfume = get_object_or_404(Perfumes, pk=pk)
    aromas = obtener_catalogo_aromas()
    marcas = obtener_catalogo_marcas()
    generos = obtener_catalogo_generos()

    if request.method == 'POST':
        form = PerfumesForm(request.POST, request.FILES, instance=perfume)
    ...
```

---

## 📦 6. Instalar Pillow

Django usa Pillow para trabajar con imágenes. Instálalo con:

```bash
python3 -m pip install Pillow
```

---

## 🗂️ 7. Ruta donde se guardan las imágenes

Las imágenes subidas se almacenarán en:

```
/udla-sistema-perfumes/media/perfumes/
```

Para comprobarlo, puedes acceder a ellas desde el navegador (en desarrollo) vía:

```
http://localhost:8000/media/perfumes/nombre_de_la_imagen.jpg
```

---

¡Y listo! 🎉 Ya puedes cargar imágenes en tu app Django de forma sencilla y ordenada.

### Limpieza y migración de base de datos (si el proyecto está en desarrollo)

1. **Eliminar las tablas de la base de datos** (manual desde la herramienta de administración de base de datos).

2. **Verificar el archivo `settings.py`**

   - Configuración mínima en `INSTALLED_APPS`:

     ```python
     INSTALLED_APPS = [
         'django.contrib.admin',
         'django.contrib.auth',
         'django.contrib.contenttypes',
         'django.contrib.sessions',
         'django.contrib.messages',
         'django.contrib.staticfiles',
         'login',
         'aromas',
         'marcas',
         'generos',
         'perfumes'
     ]
     ```

   - Configuración mínima en `MIDDLEWARE`:

     ```python
     MIDDLEWARE = [
         'django.middleware.security.SecurityMiddleware',
         'django.contrib.sessions.middleware.SessionMiddleware',
         'django.middleware.common.CommonMiddleware',
         'django.middleware.csrf.CsrfViewMiddleware',
         'django.contrib.auth.middleware.AuthenticationMiddleware',
         'django.contrib.messages.middleware.MessageMiddleware',
         'django.middleware.clickjacking.XFrameOptionsMiddleware',
     ]
     ```

   - Configuración de `TEMPLATES` para uso de plantilla base:

     ```python
     TEMPLATES = [
         {
             'BACKEND': 'django.template.backends.django.DjangoTemplates',
             'DIRS': [BASE_DIR / "templates"],
             'APP_DIRS': True,
             'OPTIONS': {
                 'context_processors': [
                     'django.template.context_processors.debug',
                     'django.template.context_processors.request',
                     'django.contrib.auth.context_processors.auth',
                     'django.contrib.messages.context_processors.messages',
                 ],
             },
         },
     ]
     ```

3. **Eliminar migraciones y bases de datos parciales si estás en desarrollo**:

   ```bash
   find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
   find . -path "*/migrations/*.pyc"  -delete
   ```

4. **Ejecutar migraciones con `--fake-initial`**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate --fake-initial
   ```

5. **Si ocurre un error porque las tablas ya existen (ejemplo: `aromas`)**:

   ```bash
   python manage.py migrate --fake-initial
   ```