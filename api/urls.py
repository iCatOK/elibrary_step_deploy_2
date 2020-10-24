import api.views as views
from django.urls import path, include

app_name = 'api'

user_patterns = [
    path('', views.UserListView.as_view(), name='user-list'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
]

urlpatterns = [
    path('users/', include(user_patterns)),
]