from django.urls import path
from . import views

urlpatterns = [
    path('',views.list,name='list'),
    path('new',views.new,name='list'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
]
