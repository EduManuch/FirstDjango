from django.shortcuts import render  # , HttpResponse
from django.http import HttpResponseNotFound

author = {
    "name": "Эдуард",
    "surname": "Манучарян",
    "phone": "89007001122",
    "email": "my_email@mail.ru",
}
items = [
   {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
   {"id": 2, "name": "Куртка кожаная", "quantity": 2},
   {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
   {"id": 7, "name": "Картофель фри", "quantity": 0},
   {"id": 8, "name": "Кепка", "quantity": 124},
]


def home(request):
    context = {
        "name": author['name'],
        "surname": author['surname']
    }
    return render(request, 'index.html', context)


def about(request):
    context = {'author': author}
    return render(request, 'about.html', context)


def item_page(request, id):
    for item in items:
        if item['id'] == id:
            context = {'item': item}
            return render(request, 'item-page.html', context)
    return HttpResponseNotFound(f"Товар с id={id} не найден")


def items_list(request):
    context = {'items': items}
    return render(request, 'item-list.html', context)
