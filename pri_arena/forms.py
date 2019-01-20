from django.forms import forms

from pri_arena.models import Arena


class ArenaForm(forms.Form):
    class Meta:
        model = Arena
        fields = ['image_path', 'tags']
