from django.db import models
from django.shortcuts import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Robot(models.Model):
    angle0 = models.IntegerField(
        null=False,
        blank=False,
        validators=[MaxValueValidator(180), MinValueValidator(-180)],
    )
    angle0_min = models.IntegerField(null=False, blank=False)
    angle0_max = models.IntegerField(null=False, blank=False)
    len0 = models.IntegerField(null=False, blank=False)

    angle1 = models.IntegerField(
        null=False,
        blank=False,
        validators=[MaxValueValidator(180), MinValueValidator(-180)],
    )
    angle1_min = models.IntegerField(null=False, blank=False)
    angle1_max = models.IntegerField(null=False, blank=False)
    len1 = models.IntegerField(null=False, blank=False)

    angle2 = models.IntegerField(
        null=False,
        blank=False,
        validators=[MaxValueValidator(180), MinValueValidator(-180)],
    )
    angle2_min = models.IntegerField(null=False, blank=False)
    angle2_max = models.IntegerField(null=False, blank=False)
    len2 = models.IntegerField(null=False, blank=False)

    angle3 = models.IntegerField(
        null=False,
        blank=False,
        validators=[MaxValueValidator(180), MinValueValidator(-180)],
    )
    angle3_min = models.IntegerField(null=False, blank=False)
    angle3_max = models.IntegerField(null=False, blank=False)
    len3 = models.IntegerField(null=False, blank=False)

    angle4 = models.IntegerField(
        null=False,
        blank=False,
        validators=[MaxValueValidator(180), MinValueValidator(-180)],
    )
    angle4_min = models.IntegerField(null=False, blank=False)
    angle4_max = models.IntegerField(null=False, blank=False)
    len4 = models.IntegerField(null=False, blank=False)

    angle5 = models.IntegerField(
        null=False,
        blank=False,
        validators=[MaxValueValidator(180), MinValueValidator(-180)],
    )
    angle5_min = models.IntegerField(null=False, blank=False)
    angle5_max = models.IntegerField(null=False, blank=False)
    len5 = models.IntegerField(null=False, blank=False)


class Position(models.Model):
    angle0 = models.IntegerField(null=False, blank=False)
    angle1 = models.IntegerField(null=False, blank=False)
    angle2 = models.IntegerField(null=False, blank=False)
    angle3 = models.IntegerField(null=False, blank=False)
    angle4 = models.IntegerField(null=False, blank=False)
    angle5 = models.IntegerField(null=False, blank=False)

    def delete_obj(self):
        return reverse("robot:delete-position", kwargs={"id": self.id})
