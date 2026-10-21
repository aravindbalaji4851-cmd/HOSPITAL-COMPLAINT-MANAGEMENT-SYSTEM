from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Count

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from complaints.serializers import UserSerializer,ComplaintSerializer
from complaints.models import Complaint
from complaints.permissions import IsUser

class SignUpView(APIView):

    def post(self,request):

        form_data = request.data

        serializer = UserSerializer(data = form_data)

        if serializer.is_valid():

            cleaned_data = serializer.validated_data

            user_object = User.objects.create_user(** cleaned_data)

            instance = UserSerializer(user_object)

            return Response(data = instance.data)

        else: return Response(serializer.errors)


class ComplaintListCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        qs = Complaint.objects.filter(user=request.user)

        serializer = ComplaintSerializer(qs,many=True)

        return Response(data=serializer.data)

    def post(self,request):

        form_data = request.data

        serializer = ComplaintSerializer(data=form_data)

        if serializer.is_valid():

            serializer.save(user=request.user)

            return Response(data=serializer.data)

        else: return Response(data=serializer.errors)


class ComplaintRetrieveUpdateDeleteView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsUser]

    def get(self,request,pk=None):

        instance = get_object_or_404(Complaint,id=pk)

        self.check_object_permissions(request,instance)

        serializer = ComplaintSerializer(instance)

        return Response(data=serializer.data)


    def put(self,request,pk=None):

        instance = get_object_or_404(Complaint,id=pk)

        self.check_object_permissions(request,instance)

        form_data = request.data

        serializer = ComplaintSerializer(data=form_data,instance=instance)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        else: return Response(serializer.errors)

    def delete(self,request,pk=None):

        instance = get_object_or_404(Complaint,id=pk)

        self.check_object_permissions(request,instance)

        instance.delete()

        return Response({"message":"deleted.."})


class UnresolvedComplaintsView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        queryset = Complaint.objects.filter(user=request.user).exclude(status="Resolved")

        serializer = ComplaintSerializer(queryset, many=True)

        return Response(data=serializer.data)

class ComplaintCountView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        total_complaints = Complaint.objects.filter(user=request.user).count()

        response_data = {
            "total_complaints": total_complaints
        }

        return Response(data=response_data)

class ComplaintStatusSummaryView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        queryset = Complaint.objects.filter(user=request.user)

        status_summary = queryset.values("status").annotate(total=Count("id"))

        response_data = {
            "status_summary": status_summary
        }

        return Response(data=response_data)

class HighCriticalComplaintsView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        queryset = Complaint.objects.filter(
            user=request.user,
            priority__in=["High", "Critical"]
        )

        serializer = ComplaintSerializer(queryset, many=True)

        return Response(data=serializer.data)