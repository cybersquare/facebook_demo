from rest_framework.decorators import api_view
from rest_framework.response import Response
from . data import *
from . models import *

# @api_view(['GET'])
# def showemp(request):
#     if request.method = 'GET':
#         serialize = serializationclass(results, many =True)
#         return Response(serialize.data)


@api_view(['POST'])
def user_login(request):
    username = request.data['username']
    print(request.data)
    password = request.data['password']
    print(username)
    print(password)
 
    login = Login(username, password)
    result = login_model(login)
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
    regsiter_model(user)
        #add to login table
    login = Login(username,password)
    insertLogin_model(login)
    


    return Response('Successfully registered')

# @api_view(['POST'])
# def user_updatePassword(request):
#     username = request.data['username']
#     old_password = request .data['old_password']
#     new_password = request.data['new_password']
#     login = Login(username, old_password)







  
  









    


    



     