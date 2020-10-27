from django.urls import path
from faceapp import views

app_name = 'faceapp'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('photos_database/', views.photos_database, name='photos_database'),
    path('add_audio/', views.add_audio, name='add_audio'),
    path('audio_track_list/', views.audio_track_list, name='audio_track_list'),
    path('profile/', views.profile, name='profile'),
]