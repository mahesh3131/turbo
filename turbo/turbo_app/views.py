from django.shortcuts import render
from django.http import HttpResponseRedirect
from turbo_app.models import person, reg, deliv_form
import requests
# Create your views here.
def home(request):
    return render(request,'turbo_app/home.html')


def table(request):
	obj = person.objects.all()
	return render(request,'turbo_app/table.html',{'var1':'ramesh','var2':24,'var3':'ravula','var4':obj[0].user_name,'var5':obj[1].user_name,'var6':obj[0].email_id,'var7':obj[1].email_id,'var8':obj[0].age,'var9':obj[1].age})


def show_data(request):
	person_info = person.objects.all()
	return render(request,'turbo_app/show_data.html',{'person_info':person_info})


def add_info(request):
	return render(request,'turbo_app/add_info.html')	


def save_person(request):
	try:
		p_obj=person.objects.create(
			user_name=request.POST.get('user','NA'),
			age=request.POST.get('age_ui','NA'),
			email_id=request.POST.get('mail_id'))
		p_obj.save()
	except:
		return HttpResponseRedirect('add_info')
	return HttpResponseRedirect('show_data')


def forgot_pass(request):
	return render(request,'turbo_app/forgot_pass.html')


def forgot_p(request):
	trl_obj = reg.objects.all()
	if request.method=="POST":
		name = request.POST['Email']
	for i in trl_obj:
		if str(name)==str(i.email_id):
			import smtplib
			server = smtplib.SMTP("smtp.gmail.com", 587)
			server.starttls()
			def send(FROM,TO,TEXT,SUBJECT,PASS):
				MESSAGE="Subject:{}\n\n{}".format(SUBJECT,TEXT)
				server.login(FROM,PASS)
				server.sendmail(FROM,TO,MESSAGE)
				server.quit()
			send("mahesh.ravula99@gmail.com",name,"' {} '  is your password".format(i.password),"password sent","Next2you")
	return HttpResponseRedirect('register')


def profile(request):
	return render(request,'turbo_app/profile.html')


def add_auction(request):
	return render(request,'turbo_app/add_auction.html')

def auct_form(request):
	reg_obj1 = deliv_form.objects.create(
		sender_name=request.POST.get('s_name'),
		sender_email_id=request.POST.get('s_email'),
		sender_phone_no=request.POST.get('s_Phone_no'),
		sen_d_no=request.POST.get('s_d_no'),
		sen_city=request.POST.get('s_city'),
		sen_state=request.POST.get('s_state'),
		sen_district=request.POST.get('s_district'),
		sen_pincode=request.POST.get('s_pincode'),
		sen_land_mark=request.POST.get('s_land_mark'),
		rec_name=request.POST.get('r_name'),
		rec_email_id=request.POST.get('r_email'),
		rec_phone_no=request.POST.get('r_phone_no'),
		rec_d_no=request.POST.get('r_d_no'),
		rec_city=request.POST.get('r_city'),
		rec_state=request.POST.get('r_state'),
		rec_district=request.POST.get('r_district'),
		rec_pincode=request.POST.get('r_pincode'),
		rec_land_mark=request.POST.get('r_land_mark'),
		about_product=request.POST.get('about_prod'),
		p_waight=request.POST.get('prod_waight'),
		pickup_time=request.POST.get('pick_time'),
		auction_time=request.POST.get('auct_time'),
		deliv_method=request.POST.get('deliv_method'),
		)
	reg_obj1.save()
	return HttpResponseRedirect('register')


def login(request):
	return render(request,'turbo_app/login.html')


def add_login(request):
	trl_obj = reg.objects.all()
	if request.method=="POST":
		name = request.POST['username1']
		pass31 = request.POST['password1']
	for i in trl_obj:
		if str(i) == str(name) and str(pass31)== str(i.password):
			return render(request,'turbo_app/profile.html',{'res1':name,'res2':i.email_id})
	return render(request,'turbo_app/register.html')
		

def register(request):
	return render(request,'turbo_app/register.html')	


def reg_post(request):
	try:
		reg_obj = reg.objects.create(
			user_name=request.POST.get('username','NA'),
			email_id=request.POST.get('email','NA'),
			password=request.POST.get('password','NA'),
			password_2=request.POST.get('password2','NA'),
			)
		reg_obj.save()
	except:
		return HttpResponseRedirect('register')
	return HttpResponseRedirect('login')