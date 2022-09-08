from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='dashboard'),
    path('mypage/', views.my_page_view, name='my-page'),
    path('myprofile/', views.my_profile_view, name='my-profile'),
    path('home/', views.home, name='home'),
    path('account/expert-registration', views.expert_registration_view, name='expert-registration'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)