from django.db import models
from django.contrib.auth.models import User


def image_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.case.id, 'evidence_images/%Y/%m/%d/', filename)

def video_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.case.id, 'evidence_videos/%Y/%m/%d/', filename)

def doc_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.case.id, 'evidence_docs/%Y/%m/%d/', filename)

def audio_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.case.id, 'evidence_audios/%Y/%m/%d/', filename)


designation_choice = (
    ('DGP', 'Director General of Police'),
    ('ADGP', 'Addl. Director General of Police'),
    ('IGP', 'Inspector General of Police'),
    ('DIGP', 'Deputy Inspector General of Police'),
    ('SPDCP', 'Superintendent of police Deputy Commissioner of Police(Selection Grade)'),
    ('SPDCPJ', 'Superintendent of police Deputy Commissioner of Police(Junior Management Grade)'),
    ('ASPADCP', 'Addl. Superintendent of police Addl.Deputy Commissioner of Police'),
    ('ASP', 'Assistant Superintendent of Police'),
    ('INSP', 'Inspector of Police'),
    ('SUB_INSP', 'Sub Inspector of Police.'),
    ('HVLDRM', 'Asst. Sub. Inspector/Havildar Major'),
    ('HVLDR', 'Havildar.'),
    ('LN', 'Lance Naik.'),
    ('CONS', 'Constable.'),
)


class Police(User):
    police_id = models.CharField(max_length=20)
    designation = models.CharField(max_length=10, choices=designation_choice, null=True)
    ward = models.ForeignKey('Ward', null=True)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Police'

    def __str__(self):
        return self.username


class Ward(models.Model):
    id = models.CharField(max_length=10, primary_key=True)  # eg: RJ01w1,RJ01w2,RJ15w5
    address = models.CharField(max_length=255, blank=False)

    def get_contacts(self):
        contact_list = [i.contact for i in Ward.objects.get(id=self.id).contact_set]
        return contact_list

    def __str__(self):
        return self.id


class Contact(models.Model):
    ward = models.ForeignKey('ward')
    contact = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.ward
