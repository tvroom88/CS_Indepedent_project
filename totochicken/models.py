from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver


# Create your models here.

def upload_location(instance, filename):
    file_path = 'totochicken/menus/{filename}'.format(filename=filename)
    return file_path


class NewMenu(models.Model):
    Menu  = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    price = models.IntegerField()
    Info  = models.TextField(max_length=500, null=False, blank=False)


    def __str__(self):
            return self.Menu

    def get_profile_picture(self):
        if self.image:
            return NewMenu.image.url
        else:
            return 'your_default_img_url_path'

@property
def image_url(self):
    if self.image:
        return self.image.url
    return '#'

@receiver(post_delete, sender=NewMenu)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

# def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(instance.author.username + "-" + instance.title)
#
# pre_save.connect(pre_save_blog_post_receiver, sender=NewMenu)