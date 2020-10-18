from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def add_expense(request):
    return render(request, 'add_expense.html')

# Create your views here.
