from django import forms
from .models import Case


class case_form(forms.ModelForm):
    incident_time=forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model=Case
        fields="__all__"
        exclude = ['cyber_case_categories','userid','approved','updated','timestamp','solved']

    def __init__(self, *args, **kwargs):
        super(case_form, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            "name":"title"})
        self.fields['case_categories'].widget.attrs.update({
            'class': 'form-control',
            "name":"case_categories"})

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            "name":"description"})
        self.fields['reg_from_loc'].widget.attrs.update({
            'class': 'form-control',
            "name":"reg_from_loc"})
        self.fields['ward_id'].widget.attrs.update({
            'class': 'form-control',
            "name":"ward_id"})
        self.fields['incident_time'].widget.attrs.update({
            'class': 'form-control',
            "name":"incident_time"})













    # title = models.CharField(max_length=80, blank=False)
    # case_categories = models.ForeignKey(CaseCategory,null=True,blank=True)
    # cyber_case_categories = models.ForeignKey(CyberCaseCategories,null=True,blank=True)
    # description = models.TextField()
    # reg_from_loc = models.CharField(max_length=255, blank=False)
    # userid = models.ForeignKey(Citizen)
    # ward_id = models.CharField(max_length=255, blank=False)
    # incident_time = models.DateTimeField()
    # approved=models.BooleanField()
    # solved=models.BooleanField()
    
    # timestamp = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)