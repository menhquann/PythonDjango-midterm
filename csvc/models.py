from django.urls import reverse
from django.db import models
# Register your models here.
class Department(models.Model):
    name = models.TextField(max_length=256)

    def __str__(self):
        return f"{self.name}"
class Csvc(models.Model):
    code = models.TextField(max_length=10)
    name = models.TextField(max_length=255)
    den = models.IntegerField(default=10)
    ban_ghe = models.IntegerField(default=40)
    may_chieu = models.IntegerField(default=1)
    quat = models.IntegerField(default=4)
    dieu_hoa = models.IntegerField(default=2)
    department = models.ForeignKey(Department,
                                   on_delete=models.CASCADE,
                                   blank=False,
                                   null=True)
    
    def __str__(self):
        return f"{self.code}-{self.name}({self.id})"
    def get_absolute_url(self):
        # return f"/students/{self.id}"
        return reverse ("update", kwargs={"id":self.id} )