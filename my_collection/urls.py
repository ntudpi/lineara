from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='collection_index'),
    path('<int:item_id>/', views.detail, name='item_detail'),
    path('search', views.search, name='search')
]