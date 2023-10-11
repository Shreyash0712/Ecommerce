from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name = 'store'),
    path('cart/', views.cart, name = 'cart'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('contact/', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about'),
    path('signup/', views.signup, name = 'signup'),
    path('signin/', views.signin, name = 'signin'),
    path('signout/', views.signout, name = 'signout'),

]