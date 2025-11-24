from django.urls import path


from myapp import views
urlpatterns = [
    path('', views.home, name='index'),
    path('',views.four, name='four'),
    path( '',views.portfolio, name='portfolio'),
    path( '',views.sarter, name='sarter'),
    path( '',views.service, name='service'),

]