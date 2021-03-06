from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from {{ cookiecutter.package_name }}.views import HomePageView

urlpatterns = [
    # Examples:
    url(r'^$', HomePageView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),

    {% if cookiecutter.use_rq == "y" -%}
    url(r'^admin/rq/', include('django_rq.urls')),
    {%- endif %}

    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
