from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),

    path("sign-in/", auth_views.LoginView.as_view(template_name="signin.html"), name="sign-in"),
    path("sign-out/", auth_views.LogoutView.as_view(next_page="/"), name="sign-out"),
    path('sign-up', views.signup, name="sign-up"),

    path('customer/', views.customer_page),
    path('courier/', views.courier_page)
]
