from django.urls import path
from .views import HomeView, SnackListView,SnackDetailsView

urlpatterns = [
 
    path('',HomeView.as_view(), name='home'),
    path('snack/',SnackListView.as_view(), name='snack'),
    path('snack/<pk>/',SnackDetailsView.as_view(), name='snack_detail')
]