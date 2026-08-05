from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import StudentSignUpForm
from .models import Exam, Enrollment


def signup_view(request):
    if request.method == "POST":
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = StudentSignUpForm()
    return render(request, "exams/signup.html", {"form": form})


@login_required
def dashboard_view(request):
    course_ids = Enrollment.objects.filter(student=request.user).values_list("course_id", flat=True)
    exams = Exam.objects.filter(course_id__in=course_ids).select_related("course", "venue")
    return render(request, "exams/dashboard.html", {"exams": exams})
def search_view(request):
    query = request.GET.get("q", "").strip()
    exams = []
    if query:
        exams = Exam.objects.filter(course__code__icontains=query).select_related("course", "venue")
    return render(request, "exams/search.html", {"query": query, "exams": exams})