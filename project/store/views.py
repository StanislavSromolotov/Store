from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.response import TemplateResponse


# Create your views here.
# def is_my_store(request, my_store):
#     if my_store.startswith('my_store'):
#         return HttpResponse("Hello, world. You're at the polls index.")
#     else:
#         return HttpResponseNotFound(f'Ошибка - {my_store}', status=404)

# def post_list(request):
#     return render(request, '//templates//store//post_list.html', {})


def store(request):
    return TemplateResponse(request, "store/mystore.html")


def cases(request):
    return TemplateResponse(request, "store/cases.html")


def phones(request):
    return TemplateResponse(request, "store/phones.html")
