from django.shortcuts import render

# Create your views here.
def home(request):
    """# Home view"""
    template = 'frontend/index.html'
    context = {}
    pg_title = 'Inicio'
    context['pg_title'] = pg_title
    return render(request, template, context)


# Error views
"""
	custom errors
"""
def my_custom_bad_request_view(request):
    """# Custom http 400 error"""
	# template = 'url_error/frontend/400.html'
    template = 'frontend/index.html'
    context = {
        'pg_title':'Error 400',
        'title':'Error 400',
    }
    return render(request, template, context)


def my_custom_permission_denied_view(request):
    """# Custom http 403 error"""
	# template = 'url_error/frontend/403.html'
    template = 'frontend/index.html'
    context = {
        'pg_title':'Error 403',
        'title':'Error 403',
    }
    return render(request, template, context)


def my_custom_page_not_found_view(request):
    """# Custom http 404 error"""
	# template = 'url_error/frontend/404.html'
    template = 'frontend/index.html'
    context = {
        'pg_title':'Error 404',
        'title':'Error 404',
    }
    return render(request, template, context)


def my_custom_error_view(request):
    """# Custom http 500 error"""
	# template = 'url_error/frontend/500.html'
    template = 'frontend/index.html'
    context = {
        'pg_title':'Error 500',
        'title':'Error 500',
    }
    return render(request, template, context)
