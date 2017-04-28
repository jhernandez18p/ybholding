from django.conf.urls import url
from django.contrib import admin
from local_apps.frontend import views as frontend
from django.conf.urls import (include, url, handler400, handler403, handler404, handler500)

handler400 = 'local_apps.frontend.views.custom_bad_request_view'
handler403 = 'local_apps.frontend.views.custom_permission_denied_view'
handler404 = 'local_apps.frontend.views.custom_page_not_found_view'
handler500 = 'local_apps.frontend.views.custom_error_view'

urlpatterns = [
    url(r'^$', frontend.home, name='home'),
    url(r'^admin/', admin.site.urls),
]
