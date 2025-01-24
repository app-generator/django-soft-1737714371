# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    first_name = models.TextField(max_length=255, null=True, blank=True)
    last_name = models.TextField(max_length=255, null=True, blank=True)
    role = models.TextField(max_length=255, null=True, blank=True)
    province = models.TextField(max_length=255, null=True, blank=True)
    city = models.TextField(max_length=255, null=True, blank=True)
    address_1 = models.TextField(max_length=255, null=True, blank=True)
    address_2 = models.TextField(max_length=255, null=True, blank=True)
    national_id = models.IntegerField(null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Question(models.Model):

    #__Question_FIELDS__
    title = models.TextField(max_length=255, null=True, blank=True)
    content = models.TextField(max_length=255, null=True, blank=True)
    sub_content = models.TextField(max_length=255, null=True, blank=True)
    category = models.TextField(max_length=255, null=True, blank=True)

    #__Question_FIELDS__END

    class Meta:
        verbose_name        = _("Question")
        verbose_name_plural = _("Question")


class Feedback(models.Model):

    #__Feedback_FIELDS__
    title = models.TextField(max_length=255, null=True, blank=True)
    message = models.TextField(max_length=255, null=True, blank=True)
    score = models.TextField(max_length=255, null=True, blank=True)
    sentiment_values = models.TextField(max_length=255, null=True, blank=True)

    #__Feedback_FIELDS__END

    class Meta:
        verbose_name        = _("Feedback")
        verbose_name_plural = _("Feedback")


class Category(models.Model):

    #__Category_FIELDS__
    title = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Category_FIELDS__END

    class Meta:
        verbose_name        = _("Category")
        verbose_name_plural = _("Category")


class Service(models.Model):

    #__Service_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Service_FIELDS__END

    class Meta:
        verbose_name        = _("Service")
        verbose_name_plural = _("Service")



#__MODELS__END
