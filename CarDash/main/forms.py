from django import forms
from .models import Expense, Mileage, Category, Car


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'category', 'amount']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-44 rounded-lg border border-gray-600 bg-gray-800 text-gray-100 placeholder-gray-400 focus:border-blue-500 focus:ring focus:ring-blue-500/50 p-2'
            }),
            'category': forms.Select(attrs={
                'class': 'w-44 rounded-lg border border-gray-600 bg-gray-800 text-gray-100 placeholder-gray-400 focus:border-blue-500 focus:ring focus:ring-blue-500/50 p-2'

            }),
            'amount': forms.NumberInput(attrs={
                'class': 'w-44 rounded-lg border border-gray-600 bg-gray-800 text-gray-100 placeholder-gray-400 focus:border-blue-500 focus:ring focus:ring-blue-500/50 p-2'
            })
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class MileageForm(forms.ModelForm):
    class Meta:
        model = Mileage
        fields = ['date', 'odometer']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'rounded-lg border border-gray-600 bg-gray-800 text-gray-100 placeholder-gray-400 focus:border-blue-500 focus:ring focus:ring-blue-500/50 p-2'
            }),
            'odometer': forms.NumberInput(attrs={
                'class': 'rounded-lg border border-gray-600 bg-gray-800 text-gray-100 placeholder-gray-400 focus:border-blue-500 focus:ring focus:ring-blue-500/50 p-2'
            })
        }


class VehicleSelectionForm(forms.Form):
    car = forms.ModelChoiceField(queryset=Car.objects.none(), label='Selection du vehicule')

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['car'].queryset = Car.objects.for_user(user)
