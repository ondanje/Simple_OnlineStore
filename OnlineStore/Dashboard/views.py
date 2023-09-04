from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from Item.models import Item

# Create your views here.

@login_required
def index(request):
        items = Item.objects.filter(created_by=request.user)

        return render(request, 'Dashboard/index.html',{
		'items': items,
	})

