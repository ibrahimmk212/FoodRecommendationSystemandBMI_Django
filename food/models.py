import datetime

from django.db import models

# Create your models here.
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from account.models import Account
from django.conf import settings


def upload_location(instance, filename):
    file_path = "food/{date_created}/{title}-{filename}".format(date_created=datetime.datetime.now().month
                                                                             + datetime.datetime.now().month
                                                                             + datetime.datetime.now().day
                                                                             + datetime.datetime.now().minute
                                                                             + datetime.datetime.now().second,
                                                                title=instance.title,
                                                                filename=filename)
    return file_path


class Recommendation(models.Model):
    expert = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=210)
    content = models.TextField()
    mealsToConsume = models.TextField(max_length=5000, verbose_name='Meals to consume')
    mealsToAvoid = models.TextField(max_length=5000, verbose_name='Meals to avoid')
    dietTips = models.TextField(max_length=5000, verbose_name='Diet Tips')
    image = models.ImageField(upload_to=upload_location)
    diseaseTag = models.TextField(verbose_name="disease tag", max_length=200, blank=True, null=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Recommendation)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


def pre_save_recommendation_receiver(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.expert.username + "-" + str(instance.id) + "-" + instance.title)


pre_save.connect(pre_save_recommendation_receiver, sender=Recommendation)


class Food(models.Model):
    title = models.CharField(max_length=210)
    note = models.TextField(max_length=5000)
    image = models.ImageField(upload_to=upload_location)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Added Date', )
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Updated Date', )
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Food)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


def pre_save_food_receiver(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(str(datetime.datetime.now()) + "-food-" + instance.title)


pre_save.connect(pre_save_food_receiver, sender=Food)
