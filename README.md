# Recortador de Video usando MoviePy

## Descripción

Este script utiliza la biblioteca MoviePy para recortar una porción específica de un archivo de video MP4. Puedes establecer el tiempo de inicio y de finalización para el segmento de video que deseas conservar.

## Requisitos

- Python 3.x
- MoviePy

## Instalación de Dependencias

Para instalar MoviePy, puedes usar pip:

```
pip install moviepy
```

## Uso

1. Coloca el archivo de video que deseas recortar en la misma carpeta que el script y nómbralo `tu_video.mp4`.
2. Modifica las variables `start_time_tuple` y `end_time_tuple` con el tiempo de inicio y finalización que deseas, respectivamente. El formato es (minutos, segundos, milisegundos).
3. Ejecuta el script.

El video recortado se guardará en la misma carpeta con el nombre `tu_video_cortado.mp4`.

## Funciones

- `convert_to_seconds(time_tuple)`: Convierte una tupla de tiempo (minutos, segundos, milisegundos) a segundos como un número de punto flotante.

## Ejemplo de Uso

```python
# Tiempos de inicio y fin para el corte (en min, sec, milisec)
start_time_tuple = (0, 0, 0)
end_time_tuple = (0, 6, 30)
```

Con este ejemplo, el script recortará el video desde el principio hasta los 6.3 segundos.

## Licencia

Este proyecto está bajo la Licencia MIT - vea el archivo [LICENSE.md](LICENSE.md) para detalles
