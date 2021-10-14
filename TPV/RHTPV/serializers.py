from rest_framework import  serializers
from .models import MemberStatus, MemberStatusSpe, Members, SRG_Service, SR_Service, SRTask


class MemberStatusSerializer(serializers.ModelSerializer):
    """ status serializer"""
    class Meta:
        model = MemberStatus
        fields = ('id', 'designation', 'description')


class MemberStatusSpeSerializer(serializers.ModelSerializer):
    """ specific status serializer"""
    class Meta:
        model = MemberStatusSpe
        fields = ('id', 'designation', 'description')


class MembersSerializer(serializers.ModelSerializer):
    """ member serializer"""
    member_status = MemberStatusSerializer(required=True)
    member_status_spe = MemberStatusSpeSerializer(required=True)

    class Meta:
        model = Members
        fields = ('id', 'last_name', 'first_name', 'phone', 'whatsapp', 'email', 'member_status', 'member_status_spe')


class SRGSerializer(serializers.ModelSerializer):
    """ SRG serializer"""

    class Meta:
        model = SRG_Service
        fields = ('id', 'designation', 'description', 'member_status', 'member')


class SRSerializer(serializers.ModelSerializer):
    """ SR serializer"""

    class Meta:
        model = SR_Service
        fields = ('id', 'designation', 'description', 'srg_Service', 'member')
