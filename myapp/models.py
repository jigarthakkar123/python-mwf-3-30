from django.db import models

# Create your models here.
class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	address=models.TextField()
	gender=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	usertype=models.CharField(max_length=100,default="patient")
	profile_picture=models.ImageField(upload_to="profile_picture/")

	def __str__(self):
		return self.fname+" "+self.lname+" - "+self.usertype

class Doctor_Profile(models.Model):
	doctor=models.ForeignKey(User,on_delete=models.CASCADE)
	qualification=models.CharField(max_length=100)
	specialization=models.CharField(max_length=100)
	experience_in_years=models.PositiveIntegerField()
	clinic_address=models.TextField()
	time=models.CharField(max_length=100)

	def __str__(self):
		return self.doctor.fname+" - "+self.specialization

class Appointment(models.Model):
	patient=models.ForeignKey(User,on_delete=models.CASCADE)
	doctor_profile=models.ForeignKey(Doctor_Profile,on_delete=models.CASCADE)
	appointment_date=models.CharField(max_length=100)
	appointment_time=models.CharField(max_length=100)
	appointment_status=models.CharField(max_length=100,default="Pending")

	def __str__(self):
		return "Patient : "+self.patient.fname+" - "+"Doctor : "+self.doctor_profile.specialization

class Attended_Appointment(models.Model):
	appointment=models.ForeignKey(Appointment,on_delete=models.CASCADE)
	problem_dignosed=models.CharField(max_length=100)
	prescription=models.CharField(max_length=100)
	follow_up_date=models.CharField(max_length=100)

	def __str__(self):
		return self.appointment.patient.fname+" - "+self.appointment.doctor_profile.doctor.fname