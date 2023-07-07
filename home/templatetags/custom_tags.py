from django import template
from home.models import *
register = template.Library()

@register.filter()
def applydiscount(pid):
    data = Product.objects.get(id=pid)
    price = float(data.price) * (100 - int(data.discount))/100
    return price


@register.filter()
def productimage(pid):
    data = Product.objects.get(id=pid)
    return data.image.url

@register.filter()
def productname(pid):
    data = Product.objects.get(id=pid)
    return data.name

@register.filter()
def productprice(pid):
    data = Product.objects.get(id=pid)
    return data.price

@register.filter()
def productquan(pid):
    data = Product.objects.get(id=pid)
    return data.quantity

@register.simple_tag()
def producttotalprice(data, qty):
    product = Product.objects.get(id=data)
    price = int(product.price) * (100 - int(product.discount)) / 100
    return int(int(qty) * price)