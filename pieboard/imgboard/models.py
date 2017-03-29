from django.db import models


class Image(models.Model):
    md5 = models.CharField(max_length=32)
    rating = models.CharField(max_length=12)
    uploaded_on = models.DateTimeField()
    uploaded_by = models.IntegerField()


class Tag(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=16)


class ImageTags(models.Model):
    image_id = models.ForeignKey(Image)
    tag_id = models.ForeignKey(Tag)
