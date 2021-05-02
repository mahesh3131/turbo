from django.db import models

# Create your models here.
class person(models.Model):
	user_name = models.CharField(max_length=30, unique=True)
	age = models.IntegerField()
	email_id = models.EmailField(unique=True)
	def __str__(self):
		return self.user_name
class reg(models.Model):
	user_name = models.CharField(max_length=30,unique=True)
	email_id = models.EmailField(unique=True)
	password = models.CharField(max_length=8)
	password_2 = models.CharField(max_length=8)
	def __str__(self):
		return self.user_name
class deliv_form(models.Model):
	sender_name = models.CharField(max_length=30)
	sender_email_id = models.EmailField()
	sender_phone_no = models.IntegerField()
	sen_d_no = models.IntegerField()
	sen_city = models.CharField(max_length=30)
	sen_state = models.CharField(max_length=30)
	sen_district = models.CharField(max_length=30)
	sen_pincode = models.IntegerField()
	sen_land_mark = models.CharField(max_length=30)
	rec_name = models.CharField(max_length=30)
	rec_email_id= models.EmailField()
	rec_phone_no = models.IntegerField()
	rec_d_no = models.IntegerField()
	rec_city = models.CharField(max_length=30)
	rec_state = models.CharField(max_length=30)
	rec_district = models.CharField(max_length=30)
	rec_pincode = models.IntegerField()
	rec_land_mark = models.CharField(max_length=30)
	about_product = models.CharField(max_length=130)
	p_waight = models.CharField(max_length=30)
	pickup_time = models.CharField(max_length=30)
	auction_time = models.CharField(max_length=30)
	deliv_method = models.CharField(max_length=30)
	def __str__(self):
		return self.sender_name