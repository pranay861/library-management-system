from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='books/', permanent=False)),  # homepage -> book list
    path('authors/', include('authors.urls')),
    path('books/', include('books.urls')),
    path('members/', include('members.urls')),
    path('borrowing/', include('borrowing.urls')),
]
