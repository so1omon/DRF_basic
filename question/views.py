from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from . import models
from . import serializers


class QuestionDetail(APIView):
    def get(self, request, id, format=None):
        question = get_object_or_404(models.Question, pk=id)
        serializer = serializers.QuestionSerializer(question)
        return Response(serializer.data)


class QuestionList(APIView):
    def get(self, request, format=None):
        questions = models.Question.objects.all()
        serializer = serializers.QuestionSerializer(questions, many=True)
        return Response(serializer.data)
