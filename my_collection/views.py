from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import Http404

from my_collection.forms import ItemForm
from .models import Item
from django.http import HttpResponse
from django.db.models import Q

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


def search(request):
    if request.method == 'GET':
        items = ""
        text=""
        query = request.GET.get('query')
        if query:
            items = Item.objects.filter(
                Q(name__contains=query)|
                Q(location__contains=query)|
                Q(material_type__contains=query)|
                Q(description__contains=query)
            )
            if items.count()==0:
                text = "Cannot find result for '" + query + "'"
            else:
                text = "Search result for: '" + query + "'"
            return render(request, 'index.html', {
                'items': items,
                'search_text': text,
            })
        else:
            items = Item.objects.all()
            text = "All items"
            return render(request, 'index.html', {
                'items': items,
                'search_text': text,
            })
    else:
        return HttpResponse(404)



def create(request):
    if request.method == 'GET':
        form = ItemForm()
        return render(request, 'create.html', {'form': form})
    else:
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            form = ItemForm()
            context = {}
            context['form'] = form
            context['edit_status'] = "success"
            return render(
                request,
                'create.html',
                context
            )
        else:
            context = {}
            context['edit_status'] = "error"
            context['msg'] = form.errors
            context['form'] = form
            return render(
                request,
                'create.html',
                context
            )
