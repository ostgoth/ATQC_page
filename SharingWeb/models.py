from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

from SharingWeb import fields


class ItemUser(User):

    avatar = models.ImageField()

    class Meta:
        ordering = ('id',)


class Reference(models.Model):
    """ References for an ItemUser written by other ItemUsers """

    # ToDo: Rename model fields
    UserWriter = models.ForeignKey(ItemUser, related_name="creator")
    UserRecipient = models.ForeignKey(ItemUser, related_name="recipient")
    reference = models.CharField(max_length=300)

    class Meta:
        ordering = ('UserRecipient',)


class Category(models.Model):

    name = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    attr_format = JSONField()


class Item(models.Model):

    name = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category)
    condition = fields.IntegerRangeField(min_value=1, max_value=10)
    price = models.IntegerField()
    attributes = JSONField()

    class Meta:
        ordering = ('category', 'name')

    def __str__(self):
        return self.name

class ItemImage(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField()


class ItemComment(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    author = models.ForeignKey(ItemUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True)
    body = models.CharField(max_length=300)
    stars = fields.IntegerRangeField(min_value=1, max_value=5)
