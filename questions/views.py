from django.shortcuts import render,get_object_or_404
from rest_framework.generics import CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import authentication,permissions
from questions.serializers import QuestionSerializer
from assessment.models import Assessment
from questions.models import Questions


# Create your views here.
class QuestionsCreateView(CreateAPIView):

    authentication_classes=[authentication.TokenAuthentication]
    pagination_class=[permissions.IsAuthenticated]
    serializer_class=QuestionSerializer

    def perform_create(self, serializer):
        assesment_id=self.kwargs.get("pk")
        assesment_object=get_object_or_404(Assessment,id=assesment_id)

        return serializer.save(assesment=assesment_object)

class QuestionRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class=QuestionSerializer
    queryset=Questions.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]



    

