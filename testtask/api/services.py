import requests
from .models import User, Address, Bank
from django.db import transaction


# ===== RandomDataAPI =====
def fetch_users_from_api(size=5):
    """
    Отримати дані з RandomDataAPI
    """
    url = f"https://random-data-api.com/api/v2/users?size={size}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []


@transaction.atomic
def save_users_from_api(data):
    """
    Зберегти отриманих користувачів у БД разом з адресами і банком
    """
    for item in data:
        # Створення банку (якщо є)
        bank = Bank.objects.create(
            name=item.get("bank", {}).get("name", "Default Bank"),
            swift_code=item.get("bank", {}).get("iban", "N/A"),
        )

        # Створення користувача
        user = User.objects.create(
            username=item["username"],
            email=item["email"],
            bank=bank
        )

        # Додавання адрес (може бути кілька)
        addr = item.get("address", {})
        address = Address.objects.create(
            street=addr.get("street_address", "unknown"),
            city=addr.get("city", "unknown"),
            country=addr.get("country", "unknown"),
        )
        user.addresses.add(address)

    return True


# ===== CRUD =====
def get_all_users():
    return User.objects.select_related("bank").prefetch_related("addresses").all()


def get_user_by_id(user_id):
    return User.objects.select_related("bank").prefetch_related("addresses").filter(id=user_id).first()


def update_user(user_id, **kwargs):
    """
    Оновити дані користувача
    """
    user = User.objects.filter(id=user_id).first()
    if user:
        for key, value in kwargs.items():
            setattr(user, key, value)
        user.save()
    return user


def delete_user(user_id):
    """
    Видалити користувача
    """
    user = User.objects.filter(id=user_id).first()
    if user:
        user.delete()
        return True
    return False
