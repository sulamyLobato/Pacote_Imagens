from PIL import ImageFilter

def apply_grayscale(image):
    """Converte a imagem para escala de cinza."""
    return image.convert("L")