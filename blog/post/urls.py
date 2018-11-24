from . import views
from django.urls import path
app_name = 'post'
urlpatterns = [
    path('', views.all_posts, name = 'all_posts'),
    path('<int:id>/', views.post, name = 'post'),
    path('create/', views.create_post, name = 'create_post'),
    path('<int:id>/edit_post/', views.edit_post, name = 'edit_post'),
    path('<int:id>/delete_post/', views.delete_post, name = 'delete_post' ),
]
#
