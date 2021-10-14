from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics

from .models import MemberStatus, MemberStatusSpe, Members, SRG_Service, SR_Service
from .serializers import MemberStatusSerializer, MemberStatusSpeSerializer, MembersSerializer, SRGSerializer, \
    SRSerializer


# MemberStatus
class MemberStatusViewSet(viewsets.ModelViewSet):
    queryset = MemberStatus.objects.all()
    serializer_class = MemberStatusSerializer


# MemberStatusSpe
class MemberStatusSpeViewSet(viewsets.ModelViewSet):
    queryset = MemberStatusSpe.objects.all()
    serializer_class = MemberStatusSpeSerializer


# bloc of Member
class MembersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer
    name = 'members-detail'


class MembersListCreate(generics.ListCreateAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer
    name = 'members-list'


# bloc of SRG Service
class SRGDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SRG_Service.objects.all()
    serializer_class = SRGSerializer
    name = 'srg-detail'


class SRGListCreate(generics.ListCreateAPIView):
    queryset = SRG_Service.objects.all()
    serializer_class = SRGSerializer
    name = 'srg-list'


# bloc of SR Service
class SRDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SR_Service.objects.all()
    serializer_class = SRSerializer
    name = 'sr-detail'


class SRListCreate(generics.ListCreateAPIView):
    queryset = SR_Service.objects.all()
    serializer_class = SRSerializer
    name = 'sr-list'
