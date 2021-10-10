from rest_framework import routers
from .views import PostsViewSet, LikesViewSet

router = routers.DefaultRouter()
router.register('posts_list', PostsViewSet)
router.register('likes_list', LikesViewSet)

urlpatterns = router.urls
