from django.shortcuts import render
from adjust_image.base.forms import ImageForm


def imagem(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    return render(request, "base/imagem.html", {"form": form})
