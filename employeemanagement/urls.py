from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    
    path('admin/', admin.site.urls),  # Django admin interface
    path('employees/', include('employees.urls')),  # Include URLs from the employees app
    path('', RedirectView.as_view(url='employees/')),  # Redirect root URL to employees/
]


