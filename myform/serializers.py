from rest_framework import serializers
from .models import MyForm, UserSchema

class MyFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyForm
        fields = ['formid', 'form_title', 'form_html', 'is_published']

class UserSchemaSerializer(serializers.ModelSerializer):
    from_id = MyFormSerializer()  # Serialize the related MyForm instance

    class Meta:
        model = UserSchema
        fields = ['form_name','store_id', 'form_id', 'form_details']
