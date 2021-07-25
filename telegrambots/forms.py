from django import forms
from telegrambots.models import Order


class OrderForm(forms.ModelForm):
    title = forms.CharField(label='Тема', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите тему'
    }))
    text = forms.CharField(label='Описание идеи', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Напишите вашу идею'
    }))

    class Meta:
        model = Order
        fields = ('title', 'text')