from django.urls import path, include

from knox import views as knoxViews

from .views import Register, Login, User

urlpatterns = [
    path('api/auth/', include('knox.urls')),
    path('api/auth/register/', Register.as_view()),
    path('api/auth/login/', Login.as_view()),
    path('api/auth/user/', User.as_view()),
    path('api/auth/logut/', knoxViews.LogoutView.as_view(), name='knox_logout')
]
