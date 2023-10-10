from django.db import models
from django.urls import reverse

class ProfileDate(models.Model):
    full_name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="images/")
    bio=models.TextField()

    def __str__(self):
        return self.full_name
    

class SocialLink(models.Model):
    url=models.CharField(max_length=250)
    name=models.CharField(max_length=250)
    icon=models.CharField(max_length=50)
    order=models.IntegerField(default=1)

    class Meta:
        ordering=('order',)

    def __str__(self):
        return self.name
    

class About(models.Model):
    biografy=models.TextField()
    projects=models.IntegerField(default=1)
    money=models.IntegerField(default=1)
    valunters=models.IntegerField(default=1)

    # def __str__(self):
    #     return self.id
    

class Tools(models.Model):
    title=models.CharField(max_length=100)
    percentage=models.IntegerField(default=1)
    order=models.IntegerField(default=0)

    class Meta:
        ordering=('order',)

    def __str__(self):
        return self.title
    


class Service(models.Model):
    icon=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class Projects(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to="images1/")
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

class PostCategory(models.Model):
    name = models.CharField(max_length=50)

    def str(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def str(self):
        return self.name
    

class Post(models.Model):
    image = models.ImageField(upload_to="posts/")
    name = models.CharField(max_length=50)
    category = models.ForeignKey(PostCategory, on_delete=models.PROTECT)  # PROTECT- saqlash
    tags = models.ManyToManyField(Tag) 
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    
    short_description = models.CharField(max_length=255)

    def str(self):
        return self.name 

    def get_absolute_url(self):
        return reverse("blog_detail",kwargs={'pk':self.id})