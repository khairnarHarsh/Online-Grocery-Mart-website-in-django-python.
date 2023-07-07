from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name ='home'),
    path('home/', views.home, name ='home'),
    path('attacatogary/<int:pid>/', views.user_product, name="user_product"),
    path('logins/', views.logins, name ='login'),
    path('logouts/', views.logouts, name ='logouts'),
    path('cart/', views.cart, name ='cart'),
    path('about/', views.about, name ='about'),
    path('addaddress/', views.addaddress, name ='addaddress'),
    path('signup/', views.signup, name ='signup'),
    path('personalinfo/', views.personalinfo, name ='personalinfo'),
    path('emptycart/', views.emptycart, name ='emptycart'),
    # path('attacatogary/', views.attacatogary, name ='attacatogary'),
    path('add-to-whishlist/<int:pid>/', views.addwhishlist, name ="whishlist"),
    path('product-detail/<int:pid>/', views.product_detail, name="product_detail"),
    path('add-to-cart/<int:pid>/', views.addToCart, name="addToCart"),
    path('incredecre/<int:pid>/', views.incredecre, name="incredecre"),
    path('deletecart/<int:pid>/', views.deletecart, name="deletecart"),
    path('wishdeletecart/<int:pid>/', views.deletecart, name="deletecart"),
    path('booking/', views.booking, name="booking"),
    path('wishlist/', views.wishlist, name ='wishlist'),   
    path('myorderlist/', views.myorderlist, name ='myorderlist'), 
    path('user-order-track/<int:pid>/', views.user_order_track, name="user_order_track"),
    path('change-order-status/<int:pid>/', views.change_order_status, name="change_order_status"),
    path('payment/', views.payment, name="payment"), 
    path('pdf_report_create/<int:pid>/', views.pdf_report_create, name="pdf_report_create"),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)