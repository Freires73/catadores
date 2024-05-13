from django import template
from reciclagem.models import Imagem

register = template.Library()

@register.filter(name='get_first_image')
def get_first_image(product):
    imagem = Imagem.objects.filter(produto=product).first()
    if imagem:
        return imagem.imagem.url
    else:
        return False