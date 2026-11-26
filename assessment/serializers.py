from rest_framework import serializers
from assessment.models import Assessment
from questions.models import Questions

class AssesmentSerializer(serializers.ModelSerializer):

    class Meta:

        model=Assessment
        fields="__all__"
        read_only_fields=["id","trainer","created_at","updated_at"]

    def get_question_count(self,obj):
        return Questions.objects.filter(assesment=obj).count()
