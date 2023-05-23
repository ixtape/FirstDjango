from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from MainApp.models import Item

#
# items = [
#     {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
#     {"id": 2, "name": "Куртка кожаная", "quantity": 2},
#     {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
#     {"id": 7, "name": "Картофель фри", "quantity": 0},
#     {"id": 8, "name": "Кепка", "quantity": 124},
# ]


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
    for item in items:
        if item["id"] == id:
            #    result = f"""
            #    <h2> Имя: {item['name']}</h2>
            #    <p>Количество: {item['quantity']} </p>
            #    <a href='/items'> Назад </a>
            #    """
            #    return HttpResponse(result)
            context = {"item": item}
            return render(request, "item-page.html", context)
    return HttpResponseNotFound(f"Item with id={id} not found")


# <ol>
#    <li> ... </li>
#    <li> ... </li>
#    <li> ... </li>
#    <li> ... </li>
#    <li> ... </li>
# </ol>
def items_list(request):
    """Функция для отображения"""
    items = Item.objects.all()
    context = {"items": items}
    # Аргументы render :  Запрос(request), Имя файла шаблона, Контекст (чем заполняем)
    return render(request, "items-list.html", context)
