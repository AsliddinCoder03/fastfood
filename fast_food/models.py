from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=30)
    type = models.ForeignKey(Type,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    description = models.TextField(default='')
    image = models.ImageField(upload_to='book-images', null=True)
        

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

class About(models.Model):
    name = models.CharField(max_length=20)

    
    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

class BookTable(models.Model):
    name = models.TextField(max_length=20)
    phone_number = models.IntegerField(default=0)
    email = models.CharField(max_length=50)
    person = models.IntegerField(default=0)
    birthday = models.DateField(auto_now_add=True)

    
    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name



