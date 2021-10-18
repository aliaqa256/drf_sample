from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model







class ArticleSerializer_others(serializers.ModelSerializer):
   

	def get_us(self, obj):
		
		return {
			"username": obj.author.username,
			"first_name": obj.author.first_name,
			"last_name": obj.author.last_name,
		}

	us = serializers.SerializerMethodField("get_us")
	# def create(self, obj):
	# 	# obj.author = self.context['request'].user.pk
	# 	obj["author"] = get_user_model()
	# 	print(obj)
	# 	return obj
	author = serializers.HiddenField(default=serializers.CurrentUserDefault())



	class Meta:
		model = Article
		fields = "__all__"






class ArticleSerializer_get(serializers.ModelSerializer):
	

	def get_author(self, obj):

		return {
			"username": obj.author.username,
			"first_name": obj.author.first_name,
			"last_name": obj.author.last_name,
		}

	author = serializers.SerializerMethodField("get_author")




	class Meta:
		model = Article
		fields = "__all__"

















class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = "__all__"