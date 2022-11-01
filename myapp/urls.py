from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('products/',views.products,name='products'),
    path('addtocart/',views.addtocart,name='addtocart'),
    path('cart/',views.cart,name='cart'),
    #path('checkout/',views.checkout,name='checkout'),
    path('single/<int:pid>',views.single,name='single'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('pay/',views.checkout,name='pay'),
]
