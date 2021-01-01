from django.db import models
from django.contrib.auth.models import User

class investment(models.Model):
    dbinvest=models.CharField(max_length=30)
    dbamount=models.PositiveSmallIntegerField(null=True,blank=True)
    dbplace=models.CharField(max_length=30)
    dbshopname=models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dbdate=models.DateField()
    
    


    def __str__(self):
        return self.dbinvest

