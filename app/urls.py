from django.contrib import admin
from django.urls import path, include
from . import views
from . import user_login
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
#     path('admin/', admin.site.urls),
    path('',views.index,name="home"),
    path('login/', views.login,name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('social-auth/', include('social_django.urls', namespace="social")),

    path('register/', user_login.register,name="register"),
    path('loginpage/', user_login.loginpage,name="loginpage"),

    path('product/',views.product_view,name="product"),

    path('single_product/<str:id>',views.single_product,name="single_product"),

    path('about/',views.about,name="about"),
    path('services/',views.services,name="services"),
    path('contactus/',views.contact,name="contactus"),
    path('Address/',views.address,name="address"),
    path('profile/',user_login.profile,name="profile"),
    path('profile/update/',user_login.profile_update,name="profile_update"),
    path('test/',views.test,name="test"),
    # path('sliderimage/',views.slider,name="sliderimage")

    #ADD TO CART
     path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
