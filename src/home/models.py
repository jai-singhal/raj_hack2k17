from django.contrib.auth.models import User
from django.db import models

def image_upload_location(instance, filename):
    return '%s/%s/%s' % ("abc", 'evidence_images/%Y/%m/%d/', "filename")

def video_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.id, 'evidence_videos/%Y/%m/%d/', filename)

def doc_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.id, 'evidence_docs/%Y/%m/%d/', filename)

def audio_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.id, 'evidence_audios/%Y/%m/%d/', filename)

class AnonymousUser(User):
    pass

    class Meta:
        verbose_name = 'Anonymous User'

    def __str__(self):
        return self.username


class AnonymousTip(models.Model):
    title = models.CharField(max_length=80, blank=False)
    description = models.TextField()
    userid = models.ForeignKey(AnonymousUser,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    incident_time = models.DateField()
    updated = models.DateTimeField(auto_now=True)
    upload_evidence = models.BooleanField(blank = True)

    def __str__(self):
        return self.title



class Evidence(models.Model):
        image1 = models.ImageField(upload_to=image_upload_location, blank = True)
        image2 =  models.ImageField(upload_to=image_upload_location, blank = True)
        doc =  models.FileField(upload_to=doc_upload_location, blank = True)
        video =  models.FileField(upload_to=doc_upload_location, blank = True)
        def __str__(self):
            return str(self.id)
