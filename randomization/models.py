import random
from datetime import datetime

from django.db import models
from django.db.models import Max

site_choices = [("amana", "amana"), ("hindu-mandal", "hindu-mandal")]


def get_random_subject_identifier():
    return f"{random.randint(101, 110)}-{random.randint(101, 110)}-0{random.randint(100, 999)}-{random.randint(1, 9)}"


def get_random_site():
    return random.choices([c[0] for c in site_choices])


def get_random_datetime():
    return datetime.utcnow()


def get_next_sid():
    max_sid = Slot.objects.aggregate(Max("sid")).get("sid__max")
    if max_sid:
        return int(max_sid) + 1
    else:
        return 1001


class Slot(models.Model):
    sid = models.CharField(max_length=5, unique=True, default=get_next_sid)
    site = models.CharField(
        max_length=30,
        choices=site_choices,
        default=get_random_site,
    )
    subject_identifier = models.CharField(
        max_length=20, default=get_random_subject_identifier
    )
    allocated_datetime = models.DateTimeField(
        "allocated datetime", default=get_random_datetime
    )

    def __str__(self):
        return self.sid
