from django.contrib import admin
from django.urls import path, include, re_path

from expense_tracker import views
from expense_tracker.views import activate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.sign_up, name='register'),
    re_path('^accounts/activate/(?P<uidb64>[0-9A-Za-z_\\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            activate, name='activate'),
]
