from django.db import models

# Create your models here.

#class Category(models.Model):
#	auct_id = models.IntegerField()
	
#	class Meta:
#		verbose_name_plural = 'Categories'
#		verbose_name = 'Category'
	

#	def __int__(self):
#		return self.auct_id

class deliv_form(models.Model):
#	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	deliv_form_id = models.IntegerField()
	username = models.CharField(max_length=30)
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
	pro_waight = models.CharField(max_length=30)
	pickup_time = models.CharField(max_length=30)
	auction_time = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True,null=True)
	auct_time = models.CharField(max_length=10)
	auct_year = models.IntegerField()
	auct_day = models.CharField(max_length=10)
	auct_month = models.CharField(max_length=10)
	auction_status = models.CharField(max_length=30,default='live',unique=False)
	time_stamp=models.DateTimeField()
	min_bid_amnt=models.IntegerField(default=0,unique=False)
	achived_by=models.CharField(max_length=30,default='None',unique=False)
	#deliv_method = models.CharField(max_length=30)
	def __str__(self):
		return self.auction_status

class bid_table(models.Model):
	username = models.CharField(max_length=30)
	deliv_form_id = models.IntegerField(null=True)
	bid_amount = models.IntegerField()
	time_stamp=models.DateTimeField()

	def __int__(self):
		return self.deliv_form_id