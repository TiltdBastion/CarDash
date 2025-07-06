from django import forms
from .models import Expense, Mileage, Category, Car


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

class VehicleSelectionForm(forms.Form):
    car = forms.ModelChoiceField(queryset=Car.objects.none(), label='Selection du vehicule')

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['car'].queryset = Car.objects.for_user(user)
