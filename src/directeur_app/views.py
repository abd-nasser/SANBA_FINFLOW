from django.shortcuts import render

def directeur_view(request):
    return render(request, "terminal/directeur.html")
