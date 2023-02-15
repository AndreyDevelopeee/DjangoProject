from fileinput import FileInput

from .models import Task, Objavlenie
from django.forms import ModelForm, TextInput, ImageField


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title",  "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),

            "task": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })
        }



class ObjavForm(ModelForm):
    class Meta:
        model = Objavlenie
        fields = '__all__'
        '''
        fields = ["adress", "price", "decribe", "count_room", "type_hous", "img"]
        widgets = {
            "adress": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес'
            }),

            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену'
            }),
            "decribe": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),

            "count_room": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите кол-во комнат'
            }),
            "type_hous": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите тип дома'
            }),

            "img": ImageField(attrs={
                'class': 'form-control',
                'id': 'image_field',
                'upload_to': 'images/'

            })
            
        }
'''
