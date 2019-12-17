from django.db import models


class MailTest(models.Model):
    email = models.EmailField('Email', unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        verbose_name = "Mail Test"
        verbose_name_plural = "Mail Tests"

