from django.shortcuts import render

# Create your views here.
def home(request):
    """# Home view"""
    template = 'frontend/index.html'
    context = {}
    pg_title = 'Inicio'
    context['pg_title'] = pg_title
    return render(request, template, context)
