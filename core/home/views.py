from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject
from .forms import SubjectForm
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.contrib.auth import logout

GRADE_POINTS = {'A': 9, 'S': 10, 'B': 8, 'C': 7, 'D': 6, 'F': 0}
@login_required(login_url='/login/')
def cgpa_calculator(request):
	subjects = Subject.objects.all()
	form = SubjectForm()

	if request.method == 'POST':
		form = SubjectForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('cgpa_calculator')

	total_credits = 0
	total_grade_points = 0

	for subject in subjects:
		total_credits += subject.credit
		total_grade_points += subject.credit * GRADE_POINTS.get(subject.grade, 0)

	if total_credits != 0:
		cgpa = total_grade_points / total_credits
	else:
		cgpa = 0

	context = {
		'subjects': subjects,
		'form': form,
		'cgpa': cgpa,
	}

	return render(request, 'index.html', context)


@login_required(login_url='/login/')
def edit_subject(request, subject_id):
	subject = get_object_or_404(Subject, id=subject_id)

	if request.method == 'POST':
		form = SubjectForm(request.POST, instance=subject)
		if form.is_valid():
			form.save()
			return redirect('cgpa_calculator')
	else:
		form = SubjectForm(instance=subject)

	context = {
		'form': form,
		'subject_id': subject_id,
	}

	return render(request, 'edit_subject.html', context)

@login_required(login_url='/login/')
def delete_subject(request, subject_id):
	subject = get_object_or_404(Subject, id=subject_id)
	subject.delete()
	return redirect('cgpa_calculator')


@login_required(login_url='/login/')
def result(request):
	subjects = Subject.objects.all()
	form = SubjectForm()

	if request.method == 'POST':
		form = SubjectForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('cgpa_calculator')


	total_credits = 0
	total_grade_points = 0

	for subject in subjects:
		total_credits += subject.credit
		total_grade_points += subject.credit * GRADE_POINTS.get(subject.grade, 0)

	if total_credits != 0:
		cgpa = total_grade_points / total_credits
	else:
		cgpa = 0

	context = {
		'subjects': subjects,
		'form': form,
		'cgpa': cgpa,
	}

	return render(request, 'pdf.html', context)



def login_page(request):
	if request.method == "POST":
		try:
			username = request.POST.get('username')
			password = request.POST.get('password')
			user_obj = User.objects.filter(username=username)
			if not user_obj.exists():
				messages.error(request, "Username not found")
				return redirect('/login/')
			user_obj = authenticate(username=username, password=password)
			if user_obj:
				login(request, user_obj)
				return redirect('receipts')
			messages.error(request, "Wrong Password")
			return redirect('/login/')
		except Exception as e:
			messages.error(request, "Something went wrong")
			return redirect('/register/')
	return render(request, "login.html")



def register_page(request):
	if request.method == "POST":
		try:
			username = request.POST.get('username')
			password = request.POST.get('password')
			user_obj = User.objects.filter(username=username)
			if user_obj.exists():
				messages.error(request, "Username is taken")
				return redirect('/register/')
			user_obj = User.objects.create(username=username)
			user_obj.set_password(password)
			user_obj.save()
			messages.success(request, "Account created")
			return redirect('/login')
		except Exception as e:
			messages.error(request, "Something went wrong")
			return redirect('/register')
	return render(request, "register.html")


def custom_logout(request):
	logout(request)
	return redirect('login') 

