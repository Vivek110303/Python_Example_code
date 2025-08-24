from rest_framework import serializers
from Helloworld.models import post

class PostSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source= "created_by.username", read_only=True)
    class Meta:
        model = post
        fields = '__all__'
        read_only_fields = ('created_by',)

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return post.objects.create(**validated_data)
