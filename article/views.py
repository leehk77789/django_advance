from rest_framework.views import APIView
from rest_framework.response import Response
from article.models import Article
from article.serializers import ArticleSerializer
# Create your views here.

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        article = ArticleSerializer(data=request.data)

        article.is_valid(raise_exception=True)
        article.save(author = request.user)
        
        return Response(article.data)