Aquí tienes un README basado en el ejemplo proporcionado:

---

# Ethos Persons to CSV

Este proyecto es una aplicación en Python que consume datos del recurso `persons` de la API de Ethos de Ellucian y genera un archivo plano en formato CSV con todos los registros obtenidos.

## Requisitos

- Python 3.x
- Bibliotecas de Python:
  - `requests`
  - `csv`
  - `json`

## Instalación

1. Clona el repositorio en tu máquina local:

   ```sh
   git clone https://github.com/iacosta/ethos-persons-to-csv.git
   cd ethos-persons-to-csv
   ```

2. Crea un entorno virtual e instala las dependencias:

   ```sh
   python3 -m venv ethos_env
   source ethos_env/bin/activate
   pip install requests
   ```

## Uso

1. Asegúrate de tener la clave de la API (`API_KEY`) y la URL de autenticación (`AUTH_URL`) correctamente configuradas en el script `ethos_persons_to_csv.py`.

2. Ejecuta el script para generar el archivo `Persons.csv`:

   ```sh
   python ethos_persons_to_csv.py
   ```

   El script autenticará con la API, obtendrá todos los registros de `persons` manejando la paginación, y generará un archivo CSV con todos los datos.

## Estructura del Proyecto

```plaintext
ethos-persons-to-csv/
│
├── ethos_persons_to_csv.py  # Script principal para obtener datos y generar el archivo CSV
├── README.md                # Este archivo
└── requirements.txt         # Archivo de requisitos para instalar dependencias
```

## Detalles del Código

### Función `get_access_token`

Esta función realiza una solicitud POST a la URL de autenticación para obtener un token de acceso. Usa la clave de la API y especifica el tiempo de expiración del token en el payload. Si la solicitud es exitosa, retorna el token de acceso.

### Función `get_persons_data`

Esta función realiza solicitudes GET a la URL de datos `persons` utilizando el token de acceso. Maneja la paginación con un bucle `while` que incrementa el número de página en cada iteración. Los datos de cada página se agregan a la lista `persons_data`. Si no hay más datos (respuesta vacía), el bucle se rompe.

### Función `write_to_csv`

Esta función escribe los datos obtenidos en un archivo CSV. Primero, recolecta todos los posibles nombres de campos (`keys`) de los elementos de datos. Luego, usa `DictWriter` de la biblioteca `csv` para escribir los datos en el archivo, asegurándose de que todos los campos estén presentes en cada fila, rellenando los campos faltantes con `None`.

### Función `main`

La función `main` orquesta la ejecución del script. Primero obtiene el token de acceso, luego obtiene los datos de `persons`, y finalmente escribe estos datos en un archivo CSV. Maneja las excepciones para capturar y mostrar errores HTTP, errores de decodificación JSON y otros errores generales.

## Contribuciones

Las contribuciones son bienvenidas. Para contribuir, por favor:

1. Bifurca el repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commits (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre una solicitud de extracción (pull request).

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

Este README debería proporcionarte una guía clara sobre cómo usar y contribuir al proyecto. Asegúrate de personalizar cualquier sección adicional que creas necesaria para tu proyecto específico.
