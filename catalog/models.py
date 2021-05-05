from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Course(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='courses/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    lectures_amount = models.IntegerField(blank=True)
    start_date = models.DateTimeField(blank=True, null=True)
    finish_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:course_detail',
                       args=[self.id, self.slug])
