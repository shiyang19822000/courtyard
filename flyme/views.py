# --coding=utf-8

from django.shortcuts import render
from rest_framework import serializers
from rest_framework.pagination import LimitOffsetPagination
from flyme.models import Recall, Profile, WordsWall
from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.
def index(request):
    return render(request, 'index.html')


class RecallSerializer(serializers.ModelSerializer):

    def create(self, validate_data):
        return Recall.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.title = validate_data.get('title', instance.title)
        instance.desc = validate_data.get('desc', instance.desc)
        instance.thumb = validate_data.get('thumb', instance.thumb)
        instance.full = validate_data.get('full', instance.full)
        instance.save()
        return instance

    class Meta:
        model = Recall
        fields = '__all__'


class RecallPagination(LimitOffsetPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10000


class RecallViewSet(viewsets.ModelViewSet):
    queryset = Recall.objects.all()
    serializer_class = RecallSerializer
    pagination_class = RecallPagination


class WordsWallSerializer(serializers.ModelSerializer):

    def create(self, validate_date):
        return WordsWall.objects.create(**validate_date)

    def update(self, instance, validate_data):
        instance.recall_id = validate_data.get('recall_id', instance.recall_id)
        instance.words = validate_data.get('words', instance.words)

    class Meta:
        model = WordsWall
        fields = '__all__'
        ordering = ['-created']


class WordsWallPagination(LimitOffsetPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class WordsWallFilter(filters.FilterSet):
    recall_id = filters.NumberFilter(name='recall_id', method='filter_recall_id')

    def filter_recall_id(self, queryset, name, value):
        return queryset.filter(recall_id=value)

    class Meta:
        model = WordsWall
        fields = ('recall_id', )


class WordsWallViewSet(viewsets.ModelViewSet):
    queryset = WordsWall.objects.filter()
    serializer_class = WordsWallSerializer
    pagination_class = WordsWallPagination
    filter_class = WordsWallFilter
    # filter_backends = (filters.DjangoFilterBackend, )
    # filter_fields = ('recall_id', )

    def list(self, request):
        """查询留言
        * recall -- 照片编号
        """
        queryset = self.filter_queryset(self.get_queryset()).order_by('-created')
        page = self.paginate_queryset(queryset)
        if page is not None:
            seri = self.get_serializer(page, many=True)
        else:
            seri = self.get_serializer(queryset, many=True)
        if page is not None:
            return self.get_paginated_response(seri.data)
        return Response(data=seri.data, status=status.HTTP_200_OK)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
