from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .import views 


urlpatterns = [
    path('',views.index_view,name="home"),
    path('add_image', views.addImage_view , name="add_image") ,
    path('get_images', views.getImages_view , name="get_images")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)