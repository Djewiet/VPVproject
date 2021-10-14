from django.urls import path, include, re_path
from rest_framework import routers

from .views import (
    MemberStatusSpeViewSet,
    MemberStatusViewSet,
    MembersDetail, MembersListCreate,
    SRGListCreate, SRListCreate,
    SRDetail, SRGDetail,
)

router = routers.DefaultRouter()
router.register(r'status_member', MemberStatusViewSet)  # status member
router.register(r'spe_status_member', MemberStatusSpeViewSet)  # special status member

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'auth/', include('rest_auth.urls')),

    path('members-list/', MembersListCreate.as_view(), name=MembersListCreate.name),
    path('members-detail/<int:pk>/', MembersDetail.as_view(), name=MembersDetail.name),

    path('SRG-list/', SRGListCreate.as_view(), name=SRGListCreate.name),
    path('SRG-detail/<int:pk>/', SRGDetail.as_view(), name=SRGDetail.name),

    path('SR-list/', SRListCreate.as_view(), name=SRListCreate.name),
    path('SR-detail/<int:pk>/', SRDetail.as_view(), name=SRDetail.name),
]
