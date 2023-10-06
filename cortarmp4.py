from moviepy.editor import VideoFileClip

# Función para convertir (min, sec, milisec) a segundos como número de punto flotante
def convert_to_seconds(time_tuple):
    minutes, seconds, milliseconds = time_tuple
    return minutes * 60 + seconds + milliseconds / 1000.0

# Cargar el video
clip = VideoFileClip("tu_video.mp4")

print(f"Duración total del video: {clip.duration} segundos.")

# Tiempos de inicio y fin para el corte (en min, sec, milisec)
start_time_tuple = (0, 0, 0)
end_time_tuple = (0, 6, 30)

# Convertir a segundos
start_time = convert_to_seconds(start_time_tuple)
end_time = convert_to_seconds(end_time_tuple)

# Cortar el video
new_clip = clip.subclip(start_time, end_time)

# Guardar el nuevo video
new_clip.write_videofile("tu_video_cortado.mp4")

