from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Item

def index(request):
    latest_item = Item.objects.all()
    return render(request, 'index.html', {
        'items':latest_item,
    })


def detail(request, item_id):
    item =  get_object_or_404(Item, pk=item_id)
    return render(request, 'item_detail.html', {
        'item': item,
    })
