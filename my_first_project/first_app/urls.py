from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('add_musician/', views.add_musician, name='add_musician'),
    path('add_album/', views.add_album, name='add_album'),
    path('album_list/<int:musician_id>/', views.album_list, name='album_list'),
    path('edit_musician/<int:musician_id>/', views.edit_musician, name='edit_musician'),
    path('edit_album/<int:album_id>/', views.edit_alum, name='edit_album'),
    path('delete_album/<int:album_id>/', views.delete_album, name='delete_album'),
    path('delete_musician/<int:musician_id>/', views.delete_musician, name='delete_musician'),
]
