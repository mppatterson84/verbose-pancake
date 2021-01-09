from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    HomePageView,
    AboutPageView,
    ProjectsPageView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('projects/', ProjectsPageView.as_view(), name='projects'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
