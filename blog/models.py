import os.path

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    head_image = models.ImageField(upload_to = 'blog/images/%Y/%M/%d/', blank=True)
    file_upload = models.FileField(upload_to = 'blog/files/%Y/%M/%d/', blank=True)



    def __str__(self):
        return f'[{self.pk}]  {self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]