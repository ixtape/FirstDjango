from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from MainApp.models import Item


def home(request):
    context = {"name": "............", "email": "............"}
    return render(request, "index.html")


def about(request):
    author = {
        "name": "Александр",
        "midle": "Павлович",
        "surname": "Табаков",
        "phone": "8-923-600-01-02",
        "email": "vasya@mail.ru",
    }
    result = f"""
        Имя: <b>{author['name']}</b><br>
        Отчество: <b>{author['midle']}</b><br>
        Фамилия: <b>{author['surname']}</b><br>
        телефон: <b>{author['phone']}</b><br>
        email: <b>{author['email']}</b><br>
        <a href='/'> Home </a>
        """

    return HttpResponse(result)


# url /item/1
# url /item/2
def get_item(request, id):
    context = {"item": item}
    return render(request, "item-page.html", context)
    return HttpResponseNotFound(f"Item with id={id} not found")


def items_list(request):
    """Функция для отображения"""
    items = Item.objects.all()
    context = {"items": items}
    # Аргументы render :  Запрос(request), Имя файла шаблона, Контекст (чем заполняем)
    return render(request, "items-list.html", context)
