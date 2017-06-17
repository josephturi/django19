from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
# MVC Model View Controller

class Post(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()
    image = models.FileField(null=True, blank=True)
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