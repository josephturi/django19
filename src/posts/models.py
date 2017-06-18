from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
# MVC Model View Controller

class Post(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True,
            height_field="height_field",
            width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})
        # return "%s" %(self.id)
        # return "/post/%s/" %(self.id)

    class Meta:
        ordering = ["-timestamp", "-updated"]