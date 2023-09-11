from requests import request
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from articles import serializers
from articles.models import Article
from articles.serializers import ArticleSerializer
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema


# Create your views here.

# 함수형 뷰
# @api_view(['GET','POST'])
# def articleAPI(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         # sol1)
#         # article = articles[0]
#         # article_data = {        # 원하는 db내용 보냈다. but 귀찮고 반복적이여서 자동화 -> 시리얼라이저 
#         #                         # 이미 models.py에서 선언해줬으니 json 형태의 string으로 만들어주자! 
#         #     "title":article.title,
#         #     "context":article.context,
#         #     "created_at":article.created_at,
#         #     "updated_at":article.updated_at,
#         # }
#         # return Response(article_data)

#         # sol2) 시리얼라이저 이용
#         # article = articles[0]
#         # serializer = ArticleSerializer(article)
#         # return Response(serializer.data)

#         # 여러개 추가 many=True
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             print(serializer.errors)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# CBV(Class-based Views)
class ArticleList(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ArticleSerializer)
    def post(self, request, format=None):
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET','PUT', 'DELETE'])
# def articleDetailAPI(request, article_id):
#     if request.method == 'GET':
#         article = get_object_or_404(Article, id=article_id)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         article = get_object_or_404(Article, id=article_id)
#         serializer = ArticleSerializer(article, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     elif request.method == 'DELETE':
#         article = get_object_or_404(Article, id=article_id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class ArticleDetail(APIView):
    def get(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
