from django.urls import path

from .views import HomePageView, AboutPageView, ProductsPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("products/", ProductsPageView.as_view(), name="products"),
]
