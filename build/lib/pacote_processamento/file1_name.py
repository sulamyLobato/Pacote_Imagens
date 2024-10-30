from PIL import Image

def resize_image(image_path, output_path, size):
    """Redimensiona a imagem para o tamanho especificado."""
    with Image.open(image_path) as img:
        img = img.resize(size)
        img.save(output_path)

def crop_image(image_path, output_path, crop_area):
    """Corta a imagem com a área especificada."""
    with Image.open(image_path) as img:
        img_cropped = img.crop(crop_area)
        img_cropped.save(output_path)

