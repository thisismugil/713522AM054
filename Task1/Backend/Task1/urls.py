from django.urls import path
from .views import user, get_user, get_user_posts, get_post_comments

urlpatterns = [
    path('register-user/', user, name='send-user'),
    path('retrieve-users/', get_user, name='get-users'),
    path('users/<int:user_id>/posts/', get_user_posts, name='get-user-posts'),
    path('users/<int:user_id>/posts/<int:post_id>/comments/', get_post_comments, name='get-post-comments'),
]
