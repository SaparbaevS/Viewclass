"""
URL configuration for cbvtest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path



from shop.views import ProductListView, ProductDetailView, AddProductView, StartPageView, FeedbackView, \
    ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StartPageView.as_view(), name='start_page'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('product/', ProductListView.as_view(), name="show_products"),
    path('product/add/', AddProductView.as_view(), name='add_product'),
    path('product/<slug:slug_param>/', ProductDetailView.as_view(), name="product_detail"),
    path('product/<slug:slug_param>/update/', ProductUpdateView.as_view(), name='update_product'),
    path('product/<slug:slug_param>/delete/', ProductDeleteView.as_view(), name='delete_product')
]
