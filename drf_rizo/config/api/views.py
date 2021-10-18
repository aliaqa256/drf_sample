from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework import generics
from django.contrib.auth import get_user_model
from blog.models import Article
from .serializers import  ArticleSerializer_others ,ArticleSerializer_get,UserSerializer

from .permissions import (
	IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperUserOrStaffReadOnly
)





class ArticleViewSet_others(ModelViewSet):

	# queryset = 
	def get_queryset(self):
		if self.request.method == 'GET':

			return Article.objects.all()

	# serializer_class = ArticleSerializer_others 
	# custom_serializer_classes = {
    #     'list':  ArticleSerializer_get,
 
    # }	

	def get_serializer_class(self):

		if self.request.method == 'GET':

			return ArticleSerializer_get
		else :
			return ArticleSerializer_others 

	def get_permissions(self):
		if self.action in ['list', 'create']:
			permission_classes = [IsStaffOrReadOnly]
		else:
			permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
		return [permission() for permission in permission_classes]

	filterset_fields = ["status", "author"]
	ordering_fields = ["publish", "status"]
	ordering = ["-publish"]
	search_fields = [
		"title",
		"content",
		"author__username",
		"author__first_name",
		"author__last_name"
	]
class UserViewSet(ModelViewSet):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsSuperUserOrStaffReadOnly,)