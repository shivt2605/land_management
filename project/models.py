from django.db import models

# Create your models here.
class State(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="state")
    
    class Meta:
        verbose_name_plural='1. State'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.name


class City(models.Model):
    name=models.CharField(max_length=100)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="city")

    class Meta:
        verbose_name_plural='2. City'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.name

class Locality(models.Model):
    name=models.CharField(max_length=100)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="locality")

    class Meta:
        verbose_name_plural='3. Locality'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.name
    

class Project(models.Model):
    name=models.CharField(max_length=100)
    locality=models.ForeignKey(Locality,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="project")

    class Meta:
        verbose_name_plural='4. Project'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.name
    

class Block(models.Model):
    name=models.CharField(max_length=100)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural='5. Block'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.name


class Plat(models.Model):
    block=models.ForeignKey(Block,on_delete=models.CASCADE)
    plat_no=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    price_sq_ft=models.CharField(max_length=100)
    total_price=models.CharField(max_length=100)
    dimension=models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='6. Plat'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.name




