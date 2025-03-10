"""
URL configuration for WeightLostManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('logout/', views.logout_page, name='logout'),
    path('home/', views.home_page, name='home'),
    path('about/', views.about, name='about'),
    path('adWeight/', views.addWeight, name='adWeight'),
    path('addedWeight/', views.addedWeight, name='addedWeight'),
    path('update/<int:pk>/', views.weight_update, name='update'),
    path('delete/<int:pk>/', views.weight_delete, name='delete'),
    path('weight-list/', views.weight_list, name='weight_list'),
 
    path('weight-loss/', views.weight_loss_calculator, name='weight_loss_calculator'),

]
