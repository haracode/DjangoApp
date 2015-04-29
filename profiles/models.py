from django.db import models

# Create your models here.

class Profile(models.Model):
    unique_id =  models.CharField(max_length=120, default='0000')
    first_name = models.CharField(max_length=120, null=False, blank=False) 
    last_name = models.CharField(max_length=120, null=False, blank=False)
    email = models.EmailField(unique=True)#only one profile per email
    ip_address = models.CharField(max_length=120, default='0:0:0')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        #the name of the instance in Admin '__unicode__' has to be added to class ProfileAdmin
        return "%s, %s : %s Created: %s" %(self.last_name, self.first_name, self.email, str(self.timestamp))#timestam needs to be converted to a string

    class Meta:
        unique_together = ("email","unique_id",)

    