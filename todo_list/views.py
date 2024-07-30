from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import TodoList, Category


def redirect_view(request):
    return redirect(reverse('Category'))


def todo(request):
    todos = TodoList.objects.all()
    categories = Category.objects.all()

    if request.method == "POST":
        if "Add" in request.POST:
            title = request.POST["description"]
            date = str(request.POST["date"])
            category = request.POST["category_select"]
            content = '--'.join([title, date, category])
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save()
            return redirect(reverse('TodoList'))
        if "Delete" in request.POST:
            checkedlist = request.POST.getlist('checkbox')
            for i in range(len(checkedlist)):
                todo = TodoList.objects.filter(id__in=[int(_id) for _id in checkedlist])
                todo.delete()
    return render(request, "todo.html", context={"todos": todos, "categories": categories})


def category(request):
    categories = Category.objects.all()
    if request.method == "POST":
        if "Add" in request.POST:
            name = request.POST["name"]
            category = Category(name=name)
            category.save()
            return redirect(reverse('Category'))
        if "Delete" in request.POST:
            check = request.POST.getlist('check')
            for i in range(len(check)):
                try:
                    categ = Category.objects.filter(id__in=[int(_id) for _id in check])
                    categ.delete()
                except BaseException:
                    return HttpResponse('<h1>Сначала удалите карточки с этими категориями</h1>')
    return render(request, "category.html", context={"categories": categories})
























