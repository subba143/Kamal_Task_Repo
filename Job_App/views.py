from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from firebase_admin import firestore
from firebase_config import db
from .services import add_user_to_firestore

class EmailAPIView(APIView):
    def get(self, request):
        return Response({"message": "GET request"})

    def post(self, request):
        return Response({"message": "POST request"})

def get_firestore_data(request):
    # Example of fetching data from Firestore
    users_ref = db.collection('users')
    docs = users_ref.stream()
    users = []
    for doc in docs:
        users.append(doc.to_dict())
    return JsonResponse(users, safe=False)

def add_user_view(request):
    if request.method == 'POST':
        # Example: Extracting data from POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = int(request.POST.get('age'))
        add_user_to_firestore(name, email, age)
        return JsonResponse({'message': 'User added successfully'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
