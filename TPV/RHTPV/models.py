from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class MemberStatus(models.Model):
    """ status of member   """

    designation = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.designation


class MemberStatusSpe(models.Model):
    """ specific status for member"""
    designation = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.designation


class Members(models.Model):
    """ members of TPV"""
    last_name = models.CharField(max_length=30, null=False)
    first_name = models.CharField(max_length=30, null=False)
    phone = models.CharField(max_length=15, null=False)
    whatsapp = models.CharField(max_length=15, null=False)
    email = models.EmailField(_("Email address"))
    member_status = models.ForeignKey(MemberStatus, on_delete=models.CASCADE, related_name='member_status')
    member_status_spe = models.ForeignKey(MemberStatusSpe, on_delete=models.CASCADE, related_name='member_status_spe')

    def __str__(self):
        return f'{self.last_name}_{self.first_name}'

# create an endpoint of manager
class SRG_Service(models.Model):
    """ SRG Service """
    designation = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=False)
    member = models.ForeignKey(Members, on_delete=models.CASCADE, related_name='srg_member')

    def __str__(self):
        return f'{self.designation}'


class SR_Service(models.Model):
    """ SR Service """
    designation = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=False)
    srg_Service = models.ForeignKey(SRG_Service, on_delete=models.CASCADE, related_name='sr_srg_Service')
    member = models.ForeignKey(Members, on_delete=models.CASCADE, related_name='sr_member')

    def __str__(self):
        return f'{self.designation}'


class SRTask(models.Model):
    """ main task of SR"""

    designation = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=False)
    sr_Service = models.ForeignKey(SR_Service, on_delete=models.CASCADE, related_name='task_sr_Service')

    def __str__(self):
        return self.designation
