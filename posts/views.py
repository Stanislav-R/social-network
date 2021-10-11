from django.http import JsonResponse
from rest_framework import viewsets, permissions, generics, status
from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer


class LikesViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer


class LikeAnalyticsView(generics.GenericAPIView):

    def get(self, request):
        try:
            dates = dict(request.query_params)

            likes_count = Like.objects.filter(
                created__range=[
                    dates['date_from'][0],
                    dates['date_to'][0]]
            ).count()

            return JsonResponse(
                {'status': 'recieved',
                 'like_counts_by_period': f'{likes_count}'},
                status=status.HTTP_200_OK)

        except:
            return JsonResponse(
                {'status': 'Set date range for analytics'},
                status=status.HTTP_400_BAD_REQUEST)
