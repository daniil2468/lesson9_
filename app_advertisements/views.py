from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForms

def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements' : advertisements}
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')


def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForms(request.POST , request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url  = reverse('main-page')
            return redirect(url)
        else:
            form=AdvertisementForms()

    form = AdvertisementForms()
    context = {'forms' : form}
    return render(request, 'advertisement-post.html', context)