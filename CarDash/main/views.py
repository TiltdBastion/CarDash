from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Mileage, Expense, Car
from .forms import MileageForm, ExpenseForm, CategoryForm, VehicleSelectionForm
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
import json

from django.contrib.auth import logout


@login_required
def home_view(request):
    car = Car.objects.for_user(request.user).first()
    ordered_mileage = Mileage.objects.for_car(car).order_by('-date')

    latest_mileage = ordered_mileage.first()
    expenses = Expense.objects.filter(car=car).order_by('-date')[:10]
    
    odo_data = ordered_mileage.values('date', 'odometer')
    odo_chart_data = json.dumps(list(odo_data), cls=DjangoJSONEncoder)

    expense_by_category = (
        Expense.objects
        .values('category__name')
        .annotate(total=Sum('amount'))
        .order_by('category__name')
    )

    expenses_chart_data = json.dumps({
        'labels': [item['category__name'] for item in expense_by_category],
        'data': [float(item['total']) for item in expense_by_category]
    }, cls=DjangoJSONEncoder)

    return render(request, 'dashboard.html', {
        'mileage': latest_mileage,
        'expenses': expenses,
        'odo_chart_data': odo_chart_data,
        'expenses_chart_data': expenses_chart_data,
    })

@login_required
def config_view(request):
    expense_form = ExpenseForm(request.POST or None, prefix='expense')
    mileage_form = MileageForm(request.POST or None, prefix='mileage')
    category_form = CategoryForm(request.POST or None, prefix='category')

    if request.method == 'POST':
        if 'submit_expense' in request.POST and expense_form.is_valid():
            expense_form.save()
            return redirect('configuration')
        if 'submit_mileage' in request.POST and mileage_form.is_valid():
            mileage_form.save()
            return redirect('configuration')
        if 'submit_category' in request.POST and category_form.is_valid():
            category_form.save()
            return redirect('configuration')

    return render(request, 'configuration.html', {
        'expense_form': expense_form,
        'mileage_form': mileage_form,
        'category_form': category_form,
    })

@login_required
def logout_view(request):
    logout(request)