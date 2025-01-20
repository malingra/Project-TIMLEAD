from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def demand(request):
    return render(request, 'main/demand.html')

def show_geography(request):
    return render(request, 'main/geography.html')

def show_skills(request):
    return render(request, 'main/skills.html')

def show_vacancies(request):
    return render(request, 'main/vacancies.html')
