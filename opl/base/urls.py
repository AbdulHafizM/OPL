from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('calendar/', views.events, name='events'),
    path('login/', views.login_staff, name='login'),
    path('logout/', views.logout_staff, name="logout"),
    path('register/', views.register, name='register'),
    path('addcalendar/', views.addcalendar, name='addcalendar'),
    path('delete-calendar/<str:pk>', views.delete_calendar, name='delete-calendar'),
    path('dash/', views.dash, name='dash'),
    path('blog-feed/', views.blog_feed, name='blog-feed'),
    path('blog/<str:pk>', views.blog, name='blog'),
    path('create-blog', views.create_blog, name='create-blog'),
    path('delete-blog/<str:pk>', views.delete_blog, name='delete-blog'),
    path('admission/', views.admission, name='admission'),
    path('enrollment', views.see_enrollment, name='enrollment-list')
]
