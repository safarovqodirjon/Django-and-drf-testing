from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .serializers import AuthorSerializer
from .models import Author

class AuthorViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    serializer_class = AuthorSerializer
    http_method_names = ['get', 'patch', 'post', 'delete']
    # filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', ]
    ordering_fields = ['name', ]
    queryset = Author.objects.all()

    def get_serializer_class(self):
        return AuthorSerializer
