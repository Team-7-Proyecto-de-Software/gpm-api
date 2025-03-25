# GPM-API

Repositorio exploratorio para probar funcionalidades de la libreria [GPM-API](https://gpm-api.readthedocs.io/en/latest/00_introduction.html).

## Instalación

Este proyecto utiliza Python y requiere la creación de un entorno virtual para gestionar sus dependencias.

Sigue estos pasos para instalar y configurar el entorno:

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd gpm-api
```

### 2. Crear un entorno virtual
En Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

En macOS y Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

## Uso

Ejecutar el archivo `config\.config_gpm_api.py` con el siguiente comando:

```bash
python config\.config_gpm_api.py
```

Si obtiene el mensaje:

```Python
The GPM-API config file has been updated successfully!
Configuración guardada correctamente.
```

Significa que sus credenciales son correctas =). En caso contrario corrobore sus credenciales.





