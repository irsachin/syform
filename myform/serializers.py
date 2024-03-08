from rest_framework import serializers
from .models import MyForm, UserSchema

class MyFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyForm
        fields = ['formid', 'form_title', 'form_html', 'is_published']

class UserSchemaSerializer(serializers.ModelSerializer):
    form_id = serializers.PrimaryKeyRelatedField(source='form_id.formid', read_only=True)  # Serialize the formid of the related MyForm instance

    class Meta:
        model = UserSchema
        fields = ['form_name', 'store_id', 'form_id', 'form_details']
