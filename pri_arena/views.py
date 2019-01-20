
import datetime

from django.shortcuts import render

from pri_arena.forms import ArenaForm
from pri_arena.models import Arena, Tag


def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    arena_list = Arena.objects.all()[:5]
    context = {'arena_list': arena_list}

    return render(request, 'pri_arena/index.html', context)


def post(request):
    tags = Tag.objects.all()
    context = {'tags', tags}
    return render(request, 'pri_arena/post.html', context)


def add(request):
    if request.POST == 'POST':
        form = ArenaForm(request.POST)
        if form.is_valid():
            return render(request, 'pri_arena/form.html')
    else:
        form = ArenaForm()

    return render(request, 'pri_arena/form.html', {'form': form})

# class ArenaCreate(CreateView):
#     model = Arena
#     form_class = ArenaForm
#     template_name = "form.html"
#     success_url = "/"  # 成功時にリダイレクトするURL
