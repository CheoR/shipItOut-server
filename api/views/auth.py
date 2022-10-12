import json

from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.authtoken.models import Token

from api.models import AppUser


@csrf_exempt
def login_user(request):
    """
        Handles AppUser authentication.
        Method args:
            request - The full HTTP request object.
    """

    # Load JSON string request body into dict
    req_body = json.loads(request.body.decode())
    # Pull relevant info if request is POST.
    if request.method == 'POST':
        username = req_body['username']
        password = req_body['password']
        authenticated_user = authenticate(username=username, password=password)

    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        data = json.dumps({"valid": True, "token": token.key})
        return HttpResponse(data, content_type='applicatoin/json')

    else:
        data = json.dumps({"valid": False})
        return HttpResponse(data, content_type='application/json', status=status.HTTP_401_UNAUTHORIZED)


@csrf_exempt
def register_user(request):
    """
        Create new AppUser for authentication.
        Method args:
            request - The full HTTP request object.
    """

    # Load JSON string request body into dict
    req_body = json.loads(request.body.decode())

    # number of form fields
    # TODO: replace with form validator
    if len(req_body) != 9:
        data = json.dumps({"valid:": False, "reason": "missing fields"})
        return HttpResponse(data, content_type='application/json', status=status.HTTP_400_BAD_REQUEST)

    # Create a new user with Django's built-in User.create_user method
    new_user = User.objects.create_user(
        username=req_body['username'],
        email=req_body['email'],
        password=req_body['password'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name'],
    )

    # If you extend the User model to include extra fields, this is
    # where you would add the extra fields. E.g AppUser extends User
    # Note that User uses create_user method while AppUser uses create
    # method.
    # Also note how AppUser is linked 1-to-1 with User object.
    appuser = AppUser.objects.create(
        company=req_body['company'],
        role=req_body['role'],
        phone=req_body['phone'],
        account_type=req_body['account_type'],
        user=new_user,
    )

    # This is redundanta has the create method above also saves.
    # appuser.save()

    # Get new token for the new user with REST Framework's token
    # generator.
    # Note user=new_user can also be replaced by user=AppUser.user
    token = Token.objects.create(user=new_user)

    # Return token to client.
    data = json.dumps({"token": token.key, "valid": True})

    return HttpResponse(data, content_type='application/json', status=status.HTTP_201_CREATED)
