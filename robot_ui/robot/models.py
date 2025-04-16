from django.db import models
from django.shortcuts import reverse


# class Robot(models.Model):
#     pass
#
class Position(models.Model):
    angle0 = models.IntegerField(null=False, blank=False)
    angle1 = models.IntegerField(null=False, blank=False)
    angle2 = models.IntegerField(null=False, blank=False)
    angle3 = models.IntegerField(null=False, blank=False)
    angle4 = models.IntegerField(null=False, blank=False)
    angle5 = models.IntegerField(null=False, blank=False)

    def delete_obj(self):
        return reverse("robot:delete-position", kwargs={"id": self.id})