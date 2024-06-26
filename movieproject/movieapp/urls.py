from django.conf.urls.static import static
from movieproject import settings
from . import views
from django.urls import path
app_name = 'movieapp'

urlpatterns = [
    path("",views.index,name='index'),
    path("movie/<int:movie_id>",views.details,name='details'),
    path("add/",views.add_movie,name='add_movie'),
    path("update/<int:id>",views.update,name='update'),
    path("delete/<int:id>",views.delete,name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)