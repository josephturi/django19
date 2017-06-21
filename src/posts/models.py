from __future__ import unicode_literals
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save

from django.utils.text import slugify

# Create your models here.
# MVC Model View Controller
def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)
    # filebase, extension=filename.split(".")
    # return "%s/%s.%s" %(instance.id, instance.id, extension)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=140)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True,
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

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    exists = Post.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" %(slug, instance.id)
    instance.slug = slug

pre_save.connect(pre_save_post_receiver, sender=Post)