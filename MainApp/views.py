from django.shortcuts import render  # , HttpResponse
from django.http import HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

author = {
    "name": "Эдуард",
    "surname": "Манучарян",
    "phone": "89007001122",
    "email": "my_email@mail.ru",
}


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
    try:
        item = Item.objects.get(id=id)
        colors = item.colors.all()
        context = {'item': item,
                   'colors': colors}
        return render(request, 'item-page.html', context)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Товар с id={id} не найден")


def items_list(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'item-list.html', context)
