from django import forms
from adjust_image.base.models import Imagem
from adjust_image.base.service import ajustar_imagem


class ImageForm(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = "__all__"

    def save(self, commit=True):
        instancia = super(ImageForm, self).save(commit=False)
        
        if 'imagem' in self.changed_data:
            imagem = instancia.imagem
            imagem_ajustada = ajustar_imagem(imagem)
            instancia.imagem = imagem_ajustada
            instancia.save()

        return instancia
