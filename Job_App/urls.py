from django.urls import path
from .views import EmailAPIView, get_firestore_data, add_user_view

urlpatterns = [
    path('emails/', EmailAPIView.as_view(), name='email-api'),
    path('firestore/get-users/', get_firestore_data, name='get-firestore-data'),
    path('firestore/add-user/', add_user_view, name='add-user-view'),
]
