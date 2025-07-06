from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Mileage, Expense, Car
from .forms import MileageForm, ExpenseForm, CategoryForm, VehicleSelectionForm
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
import json

from django.contrib.auth import logout

@login_required
def vehicle_selection_view(request):
    form = VehicleSelectionForm(user=request.user)

    if request.method == 'POST':
        form = VehicleSelectionForm(user=request.user, data=request.POST)
        if form.is_valid():
            selected_car = form.cleaned_data['car']
            return redirect('dashboard', selected_car.id)

    return render(request, 'car_selection.html', { 'form' : form})


@login_required
def dashboard_view(request, car_id):
    ordered_mileage = Mileage.objects.for_car_id(car_id).order_by('-date')

    latest_mileage = ordered_mileage.first()
    expenses = Expense.objects.for_car_id(car_id).order_by('-date')[:10]
    
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
def config_view(request, car_id):
    expense_form = ExpenseForm(request.POST or None, prefix='expense')
    mileage_form = MileageForm(request.POST or None, prefix='mileage')
    category_form = CategoryForm(request.POST or None, prefix='category')

    if request.method == 'POST':
        if 'submit_expense' in request.POST and expense_form.is_valid():
            expense = expense_form.save(commit=False)
            expense.car_id = car_id
            expense.save()
            return redirect('config', car_id)
        if 'submit_mileage' in request.POST and mileage_form.is_valid():
            mileage = mileage_form.save(commit=False)
            mileage.car_id = car_id
            mileage.save()
            return redirect('config', car_id)
        if 'submit_category' in request.POST and category_form.is_valid():
            category = category_form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('config', car_id)

    return render(request, 'configuration.html', {
        'expense_form': expense_form,
        'mileage_form': mileage_form,
        'category_form': category_form,
    })

@login_required
def logout_view(request):
    logout(request)