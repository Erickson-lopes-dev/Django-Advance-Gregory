from django.urls import path
from django.views.generic import TemplateView
from blog.views import list_post, update_post, delete_post, create_post, HomePageView

urlpatterns = [
    path('', list_post, name='list'),
    path('create/', create_post, name='create'),
    path('update/<int:pk>', update_post, name='update'),
    path('delete/<int:pk>', delete_post, name='delete'),
    # enviar somente template
    path('home/', TemplateView.as_view(template_name='blog/home.html'), name='nome'),
    path('home1/', HomePageView.as_view(), name='home1')
]

