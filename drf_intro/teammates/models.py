from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.name)
