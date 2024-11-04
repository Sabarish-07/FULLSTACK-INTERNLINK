from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name='home'),
    path('search', search,name='search'),
    path('add', add,name='add'),
    path('view/<str:intern_id>/', view_function,name='view'),
    path('editintern/<str:intern_id>/', editintern,name='editintern'),
    path('deleteintern/<str:intern_id>/', deleteintern,name='deleteintern'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
