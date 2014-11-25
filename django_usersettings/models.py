from django.db import models
from django.conf import settings


class ArbitrarySetting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    key = models.CharField(max_length=32)
    value = models.CharField(max_length=128)

    def __str__(self):
        return "'%s': '%s' for user %s" % (
            self.key,
            self.value,
            self.user,
        )
        

