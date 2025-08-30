# api/serializers.py
from rest_framework import serializers
from .models import User, Patient, Appointment

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['phone', 'date_of_birth', 'emergency_contact']

class UserSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(required=True)  # Make it required
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'patient']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        # Extract patient data before creating user
        patient_data = validated_data.pop('patient')
        
        # Create user
        user = User.objects.create_user(
            username=validated_data['email'],  # Use email as username
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        
        # Create patient record
        Patient.objects.create(user=user, **patient_data)
        
        return user

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['doctor_name', 'appointment_date', 'reason']