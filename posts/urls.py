from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import PostsViewSet, LikesViewSet, LikeAnalyticsView

router = routers.DefaultRouter()
router.register('posts_list', PostsViewSet)
router.register('likes_list', LikesViewSet)

urlpatterns = [
    path("", include(router.urls)),
    url('analytics', LikeAnalyticsView.as_view())
]
