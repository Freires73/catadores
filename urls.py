from django.urls import path
from . import views

urlpatterns = [

    path('add_pontocoleta/', views.add_pontocoleta,name="add_pontocoleta"),
    path('excluir_pontocoleta/<str:id>/',views.excluir_pontocoleta, name="excluir_pontocoleta"),
]