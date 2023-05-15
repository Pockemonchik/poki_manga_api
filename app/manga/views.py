from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import *
from config.settings import *
from .models import *
from config.settings import *
from core.views import BaseView
from rest_framework.parsers import MultiPartParser
from .tasks import *
from django_celery_results.models import TaskResult


class MangaListView(BaseView, LimitOffsetPagination):
    """Список записей или создание записи"""

    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(responses={200: MangaSerializer}, query_serializer=MangaQuerySerializer)
    def get(self, request):
        """Возвращает список манги"""
        serializer = MangaQuerySerializer(request.query_params)
        queryset = Manga.objects.all()      
        paginate_queryset = self.paginate_queryset(queryset, request, view=self)
        serializer = MangaListSerializer(
            instance=paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    @swagger_auto_schema(responses={200: MangaSerializer}, request_body=MangaSerializer)
    def post(self, request):
        """Создание записи, загрузка аудио на траскрибацию"""
        serializer = MangaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MangaDetailView(BaseView):
    """Получение, удаление, обновление конкретной манги"""
    @swagger_auto_schema(responses={200: MangaSerializer})
    def get(self, request, pk):
        """Возвращает конкретную мангу по PK"""
        queryset = Manga.objects.get(id=pk)
        serializer = MangaSerializer(
            instance=queryset)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: TranscriberPutSerializer}, request_body=TranscriberPutSerializer)
    def put(self, request, pk):
        """Полное изменение манги"""
        record = Manga.objects.get(id=pk)
        print(request)
        record.status = 'ready'
        serializer = TranscriberPutSerializer(
            record, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        """Изменение парметров манги"""

        return Response()

    @swagger_auto_schema(responses={200: MangaSerializer})
    def delete(self, request, pk):
        """Удалениие манги из базы"""
        try:
            record = Manga.objects.get(id=pk)
            record.delete()
            return Response("delete "+str(pk), status=status.HTTP_200_OK)
        except:
            return Response(" cant delete "+str(pk), status=status.HTTP_400_BAD_REQUEST)
