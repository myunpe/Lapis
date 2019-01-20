from django.contrib import admin

# Register your models here.
from pri_arena.models import Arena, Tag

admin.site.register(Arena)
admin.site.register(Tag)