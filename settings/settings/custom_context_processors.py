import datetime

def menu(request):
    """# Menu Preprocessor"""
    print(request)
    context = {}
    site_name = 'YB Holding Panamá Inc.'
    context['site_name'] = site_name
    return context


def cookies(request):
    """# Cookies Preprocessors"""
    print(request)
    context = {}
    now = datetime.timedelta()
    context['now'] = now
    return context
