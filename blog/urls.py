from django.urls import path
from django.views.generic import TemplateView
from blog.views import list_post, update_post, delete_post, create_post, HomePageView, \
    MyView, PostList, PostDetail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('', list_post, name='list'),
    path('create/', create_post, name='create'),
    path('update/<int:pk>', update_post, name='update'),
    path('delete/<int:pk>', delete_post, name='delete'),

    # class based views
    path('home/', TemplateView.as_view(template_name='blog/post_list.html'), name='nome'),
    path('home1/', HomePageView.as_view(), name='home1'),
    path('view/', MyView.as_view(), name='view_post'),
    path('list/', PostList.as_view(), name='list_post'),
    path('detail/<int:pk>/', PostDetail.as_view(), name='detail_post'),
    path('post_create/', PostCreate.as_view(), name='create_post'),
    path('post_update/<int:pk>', PostUpdate.as_view(), name='update_post'),
    path('post_delete/<int:pk>', PostDelete.as_view(), name='delete_post')
]

