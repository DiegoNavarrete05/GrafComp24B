import cv2
import os
import numpy as np

def combine_videos_with_black_screen(input_folder, output_file, black_duration=0.5):
    """
    Combina videos en una carpeta en un solo archivo con pantallas negras entre ellos usando OpenCV.
    
    Args:
        input_folder (str): Carpeta con los videos de entrada.
        output_file (str): Ruta del archivo de salida.
        black_duration (float): Duración de la pantalla negra entre videos (en segundos).
    """
    # Obtener la lista de videos en la carpeta
    video_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith(('.mp4', '.avi', '.mkv', '.mov'))]
    video_files.sort()  # Ordenar los videos alfabéticamente

    # Leer el primer video para obtener las propiedades
    cap = cv2.VideoCapture(video_files[0])
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    cap.release()

    # Crear un video writer para el archivo de salida
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    # Crear un frame negro
    black_frame = np.zeros((height, width, 3), dtype=np.uint8)
    black_frames = [black_frame] * int(fps * black_duration)

    # Procesar cada video
    for video_file in video_files:
        cap = cv2.VideoCapture(video_file)
        
        # Leer cada frame del video y escribirlo en el archivo de salida
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)

        # Añadir los frames negros entre videos
        for frame in black_frames:
            out.write(frame)

        cap.release()

    out.release()
    print(f"Video combinado guardado en: {output_file}")


input_folder="C:/Users/Argel/Desktop/Nueva carpeta/6/media/videos/6a_plots_2D/480p15"
output_file = "sies.mp4"


combine_videos_with_black_screen(input_folder, output_file)