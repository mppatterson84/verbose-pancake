from django.urls import path

from .views import (
    HomePageView,
    AboutPageView,
    PortfolioPageView,
    FrontendPageView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('portfolio/', PortfolioPageView.as_view(), name='portfolio'),
    path('portfolio/frontend-prototypes', FrontendPageView.as_view(), name='frontend'),
]