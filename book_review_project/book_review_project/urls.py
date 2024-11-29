"""
URL configuration for book_review_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reviews.urls')),  # This will include the API and other app routes
    path('api-auth/', include('rest_framework.urls')),  # For login/logout views in DRF UI
]
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('books/', include('reviews.urls')),  # Include the URLs from the 'reviews' app
# ]