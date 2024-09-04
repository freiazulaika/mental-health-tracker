from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306152254',
        'name': 'Freia Arianti Zulaika',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)