from django.contrib.auth.models import User

from rest_framework import serializers

from complaints.models import Complaint

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username","first_name","last_name","email","password"]

        read_only_fields = ["id"]

class ComplaintSerializer(serializers.ModelSerializer):

    class Meta:

        model = Complaint

        fields = "__all__"

        read_only_fields = ["id","reported_date","user"]

    def validate_title(self, validated_data):

        if not validated_data.strip():
            raise serializers.ValidationError("Title cannot be empty.")

        return validated_data

    def validate_description(self, validated_data):

        if not validated_data.strip():
            raise serializers.ValidationError("Description cannot be empty.")

        return validated_data