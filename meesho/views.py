from django.shortcuts import render
def books(request):
    return render(request,'books.html')
def python_book(request):
    return render(request,'python_book.html')

# Create your views here.
