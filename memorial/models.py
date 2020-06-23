from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify


def pic_person_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'pic/person_{0}/{1}'.format(instance.person.id, filename)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.user.first_name


class Person(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Name'))
    birth = models.DateField(verbose_name=_('Birth'))
    death = models.DateField(verbose_name=_('Death'))
    bio = models.TextField(verbose_name=_('Bio'))
    slug = models.SlugField(editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Host'))

    def __str__(self):
        return self.name

    def save(self):
        if not self.id:
            self.slug = slugify(self.name)

        super(Person, self).save()

class Memory(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name=_('Person'))
    memory = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Host'))

    def __str__(self):
        return self.memory


class Picture(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name=_('Person'))
    image = models.ImageField(upload_to=pic_person_path)
    caption = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Host'))


class Soundtrack(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name=_('Person'))
    url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Host'))
