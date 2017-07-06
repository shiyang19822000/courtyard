from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.pagination import LimitOffsetPagination
from flyme.models import Recall, Profile


# Create your views here.
def index(request):
    return render(request, 'index.html')


class RecallSerializer(serializers.ModelSerializer):
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


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
