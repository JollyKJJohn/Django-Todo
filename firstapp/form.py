from.models import tab
from django import  forms
class ToDoform(forms.ModelForm):
    class Meta:
        model=tab
        fields="__all__"  