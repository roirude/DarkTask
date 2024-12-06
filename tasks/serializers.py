from rest_framework import serializers

from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        exclude = ['created_at', 'updated_at']
        

class TaskStatusUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['status']
        
    def validate(self, attrs):
        if len(attrs) != 1 or 'status' not in attrs:
            raise serializers.ValidationError("Only the 'status' field can be updated.")
        