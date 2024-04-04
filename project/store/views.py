# from django.http import HttpResponse, HttpResponseNotFound
# from django.shortcuts import render
from django.template.response import TemplateResponse

# from store.models.customer import Customer
from store.models.orders import Orders
from store.models.phone import Phone
from store.models.phone_case import Phone_case


def store(request):
    context = {
        "title": "My store",
    }
    return TemplateResponse(request, "store/mystore.html", context=context)


def cases(request):
    context = {
        "title": "Cases",
        "cases": Phone_case.objects.all(),
    }
    return TemplateResponse(request, "store/cases.html", context=context)


def phones(request):
    context = {
        "title": "Phones",
        "phones": Phone.objects.all(),
    }
    return TemplateResponse(request, "store/phones.html", context=context)


def basket(request):
    context = {
        "title": "Basket",
        "basket": Orders.objects.all(),
    }
    return TemplateResponse(request, "store/basket.html", context=context)
