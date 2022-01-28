from django.db import models

class UserManager(models.Manager):
    def job_validator(self, postData):
        errors={}
        if len(postData['user_name'])<3:
            errors['user_name']='Name must be at least 3 characters long.'
        if len(postData['location'])<5:
            errors['location']='Must be a vaild location.'
        if len(postData['contact'])<10:
            errors['contact']="Must be a vaild contact number."
        if len(postData['job'])<5:
            errors['job']="Must be longer then 5 characters."
        return errors

class Job(models.Model):
    user_name=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    contact=models.CharField(max_length=255)
    job=models.TextField()
    uploaded_by=models.ForeignKey('LNR_app.User', related_name='jobs', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

