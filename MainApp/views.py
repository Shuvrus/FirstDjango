from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

author = {
    "name": "Евгений",
    "surname": "Юрченко",
    "phone": "89007001122",
    "email": "eyurchenko@specialist.ru",
}
items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


# Create your views here.
def home(request):
    context = {
        'name': author['name'],
        'surname': author['surname']
    }
    return render(request, 'index.html', context)


def about(request):
    # text = f"""
    # Имя: <b>{author['name']}</b><br>
    # Фамилия: <b>{author['surname']}</b><br>
    # телефон: <b>{author['phone']}</b><br>
    # email:   <b>{author['email']}</b>
    # """
    # return HttpResponse(text)
    context = {
        'author': author
        }
    return render(request, 'about.html', context)


def item_page(request, id):
    try:
        item = Item.objects.get(id=id)
        colors = item.colors.all()
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Товар с id={id} не найден")
    context = {
        'item': item,
        'colors': colors,
    }
    return render(request, 'item-page.html', context)


def items_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'item-list.html', context)
