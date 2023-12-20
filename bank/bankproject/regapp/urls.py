from . import views
from django.urls import path

from .views import get_branch, dependantfield

urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('reg',views.reg,name='reg'),
    path('form',views.form,name='form'),
    path('dependantfield',views.dependantfield,name='dependantfield'),
    # path('', views.regfListView.as_view(), name='regf_changelist'),
    # path('add/', views.regfCreateView.as_view(), name='regf_add'),
    # path('<int:pk>/', views.regfUpdateView.as_view(), name='regf_change'),

    path('get-branch/', get_branch, name='get_branch'),

]