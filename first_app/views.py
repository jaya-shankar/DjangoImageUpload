from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from .forms import ImageForm
from .models import ImageUpload

# Create your views here.

def index_view(request):
    newForm= ImageForm()
    context={"form" : newForm ,}
    return render(request,"index.html",context)
   


def addImage_view(request):
    
    form=ImageForm(request.POST,request.FILES)
    print(request.FILES)
    if(form.is_valid()):
        form.save()
    else:
        print("bad request")
    return HttpResponse("success")

def getImages_view(request):
    images=ImageUpload.objects.all()
    image_urls=[]
    for image in images:
        image_urls.append("media/"+str(image.image_file))
    response={"image_urls" : image_urls}
        
    return JsonResponse(response)