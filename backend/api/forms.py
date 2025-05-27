from django import forms
from .models import StampCard

class StampCardForm(forms.ModelForm):
    class Meta:
        model = StampCard
        fields = ['title', 'stamps_needed']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'stamps_needed': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 1,
                },
            ),
        }

        labels = {
            'title': 'Card Title',
            'stamps_needed': 'Number of Stamps Required',
        }
