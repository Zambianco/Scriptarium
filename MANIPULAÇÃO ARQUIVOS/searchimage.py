'''
DESCRIÇÃO GERAL
Objetivo: O script percorre todas as subpastas da pasta onde está sendo executado, encontra a maior imagem (com base no tamanho em bytes) de cada subpasta e a move para a pasta do script. Se a imagem for .webp, ela é convertida para .jpg. Caso um arquivo com o mesmo nome já exista, o script cria um nome sequencial para evitar substituições.

FLUXO DE FUNCIONAMENTO
Percorre as subpastas com os.walk.
Filtra os arquivos de imagem pelas extensões especificadas.
Encontra a maior imagem com base no tamanho em bytes.
Converte as imagens .webp para .jpg.
Gera um nome único caso o arquivo já exista.
Move a imagem para a pasta onde o script está sendo executado.



'''

import os
import shutil
from PIL import Image  # Certifique-se de ter Pillow instalado: pip install Pillow

def get_new_filename(directory, filename):
    """Gera um nome sequencial se o arquivo já existir."""
    name, ext = os.path.splitext(filename)
    counter = 1
    new_name = f"{name}_{counter}{ext}"

    while os.path.exists(os.path.join(directory, new_name)):
        counter += 1
        new_name = f"{name}_{counter}{ext}"

    return new_name

def get_largest_image_by_size(files, folder):
    """Retorna o caminho do maior arquivo de imagem com base no tamanho em bytes."""
    largest_file = None
    largest_size = 0

    for file in files:
        file_path = os.path.join(folder, file)
        file_size = os.path.getsize(file_path)

        if file_size > largest_size:
            largest_size = file_size
            largest_file = file_path

    return largest_file

def convert_webp_to_jpg(source_path):
    """Converte um arquivo .webp para .jpg e retorna o novo caminho."""
    new_filename = f"{os.path.splitext(source_path)[0]}.jpg"
    new_file_path = os.path.abspath(new_filename)

    with Image.open(source_path) as img:
        img = img.convert("RGB")  # Necessário para converter corretamente
        img.save(new_file_path, "JPEG")
        print(f"Convertido: {source_path} -> {new_file_path}")

    return new_file_path

def move_images_to_current_folder():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    image_extensions = {".png", ".jpg", ".jpeg", ".webp"}

    for root, _, files in os.walk(current_dir):
        # Filtra apenas as imagens
        image_files = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]

        if image_files and root != current_dir:
            largest_image = get_largest_image_by_size(image_files, root)

            if largest_image:
                # Converte .webp para .jpg, se necessário
                if largest_image.lower().endswith(".webp"):
                    new_image_path = convert_webp_to_jpg(largest_image)
                    os.remove(largest_image)  # Exclui o .webp original
                else:
                    new_image_path = largest_image

                # Define o caminho de destino
                destination_path = os.path.join(current_dir, os.path.basename(new_image_path))

                # Gera um nome sequencial se o arquivo já existir
                if os.path.exists(destination_path):
                    destination_path = get_new_filename(current_dir, os.path.basename(new_image_path))

                # Move a imagem
                shutil.move(new_image_path, destination_path)
                print(f"Movido: {new_image_path} -> {destination_path}")

if __name__ == "__main__":
    move_images_to_current_folder()
