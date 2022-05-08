from django.urls import path
from .import views

urlpatterns = [
    #function view urls
    path('get', views.get_itinerary, name='get_itinerary'),
    path('post', views.post_itinerary, name='post_itinerary'),
    path('get_by_id/<int:pk>/', views.get_itinerary_by_id, name='get_itinerary_by_id'),
    path('put/<int:pk>/', views.put_itinerary, name='put_itinerary'),
    path('delete/<int:pk>/', views.delete_itinerary, name='delete_itinerary'),
    
]
