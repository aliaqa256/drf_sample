
from django.urls import path, include
from .views import ArticleViewSet_others,UserViewSet #,ArticleList
from rest_framework import routers

app_name = "api"

router = routers.SimpleRouter()
router.register('articles', ArticleViewSet_others, basename="articles")

router.register('users', UserViewSet, basename="users")

# urlpatterns = [
# 	path("", include(router.urls)),
# 	path('post',ArticleSerializer_post)
# ]


urlpatterns = [
	
	path("", include(router.urls)),
	# path('my/get/',ArticleList.as_view()),

]