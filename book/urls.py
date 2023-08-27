from django.urls import path, include
from rest_framework import routers

from .views import AuthorViewSet

router = routers.DefaultRouter()
router.register("author", AuthorViewSet, "author")

app_name = "book"

urlpatterns = [
    path('', include(router.urls))
]