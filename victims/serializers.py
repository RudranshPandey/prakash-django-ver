from rest_framework import serializers
from .models import All_profiles
class All_profilesSerializers(serializers.ModelSerializer):
    class Meta:
        model = All_profiles
        fields = '__all__'