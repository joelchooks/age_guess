from rest_framework import serializers

class PersonNameSerializer(serializers.Serializer):
    """
    Serializer for validating the request data to get age.
    """
    name = serializers.CharField(max_length=100, help_text="entered name.")
