from django.db import models

class user(models.Model):
    unic_user_id=models.CharField(max_length=120)
    username=models.TextField()
    password=models.TextField()
    mail=models.TextField()
    date_of_reg=models.DateTimeField(auto_now_add=True)
    rating_of_user=models.CharField(max_length=120)
    avatarka = models.ImageField(upload_to='image_user/')
    def __str__(self):
        return self.username

class Articles(models.Model):
    title=models.CharField(max_length=120)
    post=models.TextField()
    date=models.DateTimeField()
    rating=models.CharField(max_length=120)
    cover = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title
# class amir(models.Model):
#     title=models.CharField(max_length=120)
#     def __str__(self):
#         return self.title
