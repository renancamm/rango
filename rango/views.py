from django.shortcuts import render
from rango.models import Category, Page


def index(request):
    # Query database and pass to context
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    # Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)


def about(request):
    context_dict = {'name': "Beik!"}
    return render(request, 'rango/about.html', context=context_dict)


# def show_category(request, category_name_url):
