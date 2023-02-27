from django.urls import path
from users.views import login, register, EmailVerificationView, dashboard, logout, forgotPassword
app_name='user'
urlpatterns=[
    path('', login, name = 'login'),
    path('register/', register, name = 'register' ),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout, name='logout'),
    path('forgotPassword', forgotPassword, name='forgotPassword'),
]