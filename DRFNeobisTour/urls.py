"""
URL configuration for DRFNeobisTour project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from myapp.views import TourListCreateAPIView, TourCategoryListCreateAPIView, ReviewListCreateAPIView, BookingListCreateAPIView, UserViewSet, TourDetailAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('', include("myapp.urls")),
    path('api/tours/<int:pk>/', TourDetailAPIView.as_view(), name='tour-detail'),
    path("api/schema/", SpectacularAPIView.as_view(), name='schema'),  # Moved this line up
    path("api/docs/", SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),  # Moved this line up
    path('api/tours/', TourListCreateAPIView.as_view(), name='tour-list-create'),
    path('api/categories/', TourCategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('api/reviews/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('api/bookings/', BookingListCreateAPIView.as_view(), name='booking-list-create'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),  # Moved this line down
]


