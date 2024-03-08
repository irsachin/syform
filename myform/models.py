from django.db import models

class MyForm(models.Model):
    formid = models.CharField(max_length=100, primary_key=True)
    form_title = models.CharField(max_length=100)
    form_html = models.JSONField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.form_title

class UserSchema(models.Model):
    form_name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    store_id = models.CharField(max_length=100)
    form_id = models.ForeignKey(MyForm, on_delete=models.CASCADE, related_name='user_schemas')
    form_details = models.JSONField()

    def __str__(self):
        return self.form_name
    
