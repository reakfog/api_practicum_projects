from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, permissions
from . import serializers
from .models import User, Post, Comment, Follow, Group
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    '''
    This class is needed to manipulate posts.
    Available methods: GET, POST, PUT, PATCH, DELETE.
    '''
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    filterset_fields = ['group']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    '''
    This class is needed to manipulate comments.
    Available methods: GET, POST, PUT, PATCH, DELETE.
    '''
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        author = self.request.user
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=author, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    '''
    This class is needed to manipulate follows.
    Available methods: GET, POST.
    '''
    queryset = Follow.objects.all()
    serializer_class = serializers.FollowSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'following__username']
    http_method_names = ('get', 'post')

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Follow.objects.filter(following=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    '''
    This class is needed to manipulate groups.
    Available methods: GET, POST.
    '''
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ('get', 'post')
