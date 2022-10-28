from dataclasses import fields
from rest_framework import serializers
from article.models import Article

class ArticleSerializer(serializers.Serializer):
    class Meta:
        model = Article
        fields = '__all__'