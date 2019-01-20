from django.http import HttpResponse
import datetime

from django.shortcuts import render

from pri_arena.models import Arena


def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    arena_list = Arena.objects.all()[:5]
    context = {'arena_list': arena_list}

    return render(request, 'pri_arena/index.html', context)
