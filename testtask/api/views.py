from rest_framework import viewsets
from .models import User, Address, Bank
from rest_framework.response import Response
from .serializers import UserSerializer, AddressSerializer, BankSerializer
from rest_framework.decorators import api_view
from .services import fetch_users_from_api, save_users_from_api
from .services import (
    fetch_users_from_api,
    save_users_from_api,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user
)



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer




@api_view(["POST"])
def load_random_users(request):
    data = fetch_users_from_api(size=5)
    save_users_from_api(data)
    return Response({"status": "ok", "inserted": len(data)})


@api_view(["GET"])
def list_users(request):
    users = get_all_users()
    return Response([{"id": u.id, "username": u.username, "email": u.email} for u in users])


@api_view(["PUT"])
def edit_user(request, user_id):
    user = update_user(user_id, **request.data)
    if user:
        return Response({"status": "updated"})
    return Response({"status": "not found"}, status=404)


@api_view(["DELETE"])
def remove_user(request, user_id):
    if delete_user(user_id):
        return Response({"status": "deleted"})
    return Response({"status": "not found"}, status=404)