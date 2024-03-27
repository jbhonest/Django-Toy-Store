from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Blog categories'


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(
        BlogCategory, on_delete=models.PROTECT, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    publish_date = models.DateTimeField(auto_now_add=True)

    def delete(self):
        # Delete associated Image objects and their image files
        for image in self.images.all():
            image.delete()

        # Call the superclass's delete method
        super().delete()

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_comments')

    is_active = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class BlogImage(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='images')
    caption = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images/')

    def delete(self):
        # Delete the image file from the storage
        storage, path = self.image.storage, self.image.path
        storage.delete(path)

        # Call the parent class's delete method to remove the model instance from the database
        super().delete()

    def __str__(self):
        return self.caption
