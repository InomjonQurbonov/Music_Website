from django.urls import path

from .views import (register_view, login_view,
                    logout_view, change_password,
                    user,favorites,history
                        )

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='log_out'),
    path('change_password/', change_password, name='change_password'),
    path('user/', user, name='user'),
    path('favorites/', favorites, name='favorites'),
    path('history/', history, name='history')
]