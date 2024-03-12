# MiDex

MiDex es una aplicación web para gestionar una Pokédex personalizada.

## Instalación

Sigue estos pasos para configurar y ejecutar MiDex en tu entorno local:

1. **Clona el repositorio:**
    ```bash
    git clone https://github.com/ByNuxx/Chino-TuPrimeraPagina.git
    ```

2. **Accede al directorio del proyecto:**
    ```bash
    cd MiDex
    ```

3. **Crea y activa un entorno virtual (opcional pero recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

4. **Instala las dependencias del proyecto:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Aplica las migraciones de la base de datos:**
    ```bash
    python manage.py migrate
    ```

6. **Ejecuta el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```

7. **Accede a la aplicación en tu navegador:**
    ```
    http://127.0.0.1:8000/
    ```
