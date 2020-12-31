from django.db import models

# Create your models here.

class Homecontent(models.Model):
    bg_img_1026x660 = models.ImageField(upload_to='pics')
    offers = models.CharField(max_length=15)
    pd_title = models.CharField(max_length=20)
    pd_name = models.TextField()
    pd_disc = models.TextField()
    pd_img_330x260 = models.ImageField(upload_to='pics')

class Addproduct(models.Model):
    pd_catogory = models.CharField(max_length=20)
    pd_detail = models.TextField()
    pd_img_1_220x245 = models.ImageField(upload_to='pics')
    pd_name1 = models.CharField(max_length=20)
    pd_img_2_220x245 = models.ImageField(upload_to='pics')
    pd_name2 = models.CharField(max_length=20)
    pd_img_3_220x245 = models.ImageField(upload_to='pics')
    pd_name3 = models.CharField(max_length=20)
