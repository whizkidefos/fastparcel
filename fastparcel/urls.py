from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from core import views

from core.customer import  views as customer_views
from core.courier import  views as courier_views

customer_urlpatterns = [
    path('', customer_views.home, name='home'),
    path('profile/', customer_views.profile_page, name="profile"),
]

courier_urlpatterns = [
    path('', courier_views.home, name='home'),

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('', include('social_django.urls', namespace='social')),

    path("sign-in/", auth_views.LoginView.as_view(template_name="signin.html"), name="sign-in"),
    path("sign-out/", auth_views.LogoutView.as_view(next_page="/"), name="sign-out"),
    path('sign-up/', views.signup, name="sign-up"),

    path('customer/', include((customer_urlpatterns, 'customer'))),
    path('courier/', include((courier_urlpatterns, 'courier'))),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
