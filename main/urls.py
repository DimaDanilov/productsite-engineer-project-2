from django.urls import path, include
from . import views
from .views import ProductsView


app_name = "products"

urlpatterns = [
    path('', views.index, name=app_name),
    path('register', views.register, name='register'),
    path('products', views.ProductsView.as_view()),
    path('accounts/', include('django.contrib.auth.urls'))
]