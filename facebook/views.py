from rest_framework.decorators import api_view
from rest_framework.response import Response
from . db import *
from . models import *


@api_view(['GET'])
def index(request):
    message = 'Congratulations, you  have created an API'
    return Response(message)


@api_view(['POST'])
def user_login(request):
    username = request.data['username']
    print(request.data)
    password = request.data['password']
    print(username)
    print(password)
    login = Login(username, password)
    result = login_db(login)
    return Response(result)


@api_view(['POST'])
def user_register(request):
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    gender = request.data['gender']
    dob = request.data['dob']
    email = request.data['email']
    username = request.data['email'] 
    phone = request.data['phone']
    password = request.data['password']

    #add to registered users
    user = User(first_name, last_name, gender, dob, email, phone)
    print(user)
    user_id = regsiter_db(user)
    #add to login table
    login = Login(username,password)
    insertLogin_db(user_id, login)

    return Response('Successfully registered')


@api_view(['POST'])
def user_updatePassword(request):
    username = request.data['username']
    current_password = request .data['current_password']
    new_password = request.data['new_password']
    status = update_password_db(username, current_password, new_password)



# PEP 8 coding standards
# Linting automatic checking
# Deployment, git, ci/cd

# 3 month
# Security - API - JWT authorization
