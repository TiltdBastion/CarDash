from django import forms
from .models import Expense, Mileage, Category

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'category', 'amount']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class MileageForm(forms.ModelForm):
    class Meta:
        model = Mileage
        fields = ['date', 'odometer']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }