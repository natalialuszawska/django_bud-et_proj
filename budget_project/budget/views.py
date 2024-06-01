from django.shortcuts import render, get_object_or_404, redirect
from .models import Income, Expense
from .forms import IncomeForm, ExpenseForm

def index(request):
    incomes = Income.objects.all().order_by('-date')
    expenses = Expense.objects.all().order_by('-date')
    total_income = sum(income.amount for income in incomes)
    total_expense = sum(expense.amount for expense in expenses)
    balance = total_income - total_expense
    return render(request, 'budget/index.html', {
        'incomes': incomes,
        'expenses': expenses,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance
    })

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = IncomeForm()
    return render(request, 'budget/add_income.html', {'form': form})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExpenseForm()
    return render(request, 'budget/add_expense.html', {'form': form})

def delete_income(request, id):
    income = get_object_or_404(Income, id=id)
    if request.method == 'POST':
        income.delete()
        return redirect('index')
    return render(request, 'budget/delete_income.html', {'income': income})

def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == 'POST':
        expense.delete()
        return redirect('index')
    return render(request, 'budget/delete_expense.html', {'expense': expense})
