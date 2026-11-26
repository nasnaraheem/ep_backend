from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework import authentication,permissions
from assessment.models import Assessment
from assessment.serializers import AssesmentSerializer
from rest_framework.response import Response
from accounts.permission import IsOwner
from datetime import datetime,timedelta,time

# Create your views here.
class AssessmentListCreateView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):

        qs=Assessment.objects.filter(trainer=request.user)
        serializer_instance=AssesmentSerializer(qs,many=True)
        return Response(serializer_instance.data)

    def post(self,request):

        form_data=request.data
        serilaizer_instance=AssesmentSerializer(data=form_data)
        if serilaizer_instance.is_valid():

            cleaned_data=serilaizer_instance.validated_data
            exam_date=cleaned_data.get("exam_date")
            start_time=cleaned_data.get("start_time")
            duration=cleaned_data.get("duration")



            end_date_time=datetime.combine(exam_date,start_time)+timedelta(hours=duration)
            end_time=end_date_time.time()



            serilaizer_instance.save(trainer=request.user,end_time=end_time)
            return Response(serilaizer_instance.data)
        else:
            return Response(serilaizer_instance.errors)
        



class AssessmentRetriveUpdateDeleteView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsOwner]

    def get(self,request,pk=None):

        qs=get_object_or_404(Assessment,id=pk)
        serializer_instance=AssesmentSerializer(qs)
        return Response(serializer_instance.data)

    def put(self,request,pk=None):

        form_data=request.data
        instance=get_object_or_404(Assessment,id=pk)
        serializer_instance=AssesmentSerializer(data=form_data,instance=instance)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

    def delete(self,request,pk=None):

        instance=get_object_or_404(Assessment,id=pk)
        instance.delete()
        return Response({"message" : "deleted"})

    

   
   


  


  


