from django.contrib.auth.models import User
from django.db import models


class ConfirmCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.IntegerField()

    def __str__(self):
        return self.code
