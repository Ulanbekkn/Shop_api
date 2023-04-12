from django.urls import path
from users import views


urlpatterns = [
    path('authentication/', views.authentication_api_view),
    path('registration/', views.registration_api_view),
    path('confirm/', views.confirm_user_views),
]