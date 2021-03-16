from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet


router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet)
router_v1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)
router_v1.register(r'follow', FollowViewSet)
router_v1.register(r'group', GroupViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router_v1.urls)),
]
