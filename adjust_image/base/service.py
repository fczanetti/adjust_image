from PIL import Image, ImageOps
from io import BytesIO
from rembg import remove
from django.core.files.uploadedfile import InMemoryUploadedFile


def ajustar_imagem(imagem):
    size = (840, 520)

    with Image.open(imagem) as img:
        img = ImageOps.contain(img, size)

        img = remove(img)
        img = img.convert('RGB')

        img_io = BytesIO()
        img.save(img_io, format='JPEG')
        tamanho_imagem = img_io.tell()

        img_io.seek(0)
        imagem_nome = f"nova_imagem_produto.jpg"
        imagem_nova = InMemoryUploadedFile(img_io, None, imagem_nome, 'image/jpeg', tamanho_imagem, None)
    
    return imagem_nova
