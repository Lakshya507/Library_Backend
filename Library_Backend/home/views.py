from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import ShelfToken
import random

NUMBER_OF_SHELVES = 100

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("index") if not user.is_staff else redirect("admin_shelves")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "login.html")
    return render(request, "login.html")


@login_required(login_url='/')
def index_view(request):
    shelf_token = ShelfToken.objects.filter(user=request.user).exclude(status='collected').order_by('-id').first()
    
    if request.method == "POST":
        if shelf_token and shelf_token.status in ['requested', 'assigned', 'retrieval_requested']:
            messages.error(request, "You have an active request or assignment. Please wait for admin confirmation.")
        else:
            assigned_shelves = ShelfToken.objects.filter(status__in=['requested','assigned','retrieval_requested']).values_list('shelf_number', flat=True)
            available_shelves = [i for i in range(1, NUMBER_OF_SHELVES+1) if i not in assigned_shelves]
            if not available_shelves:
                messages.error(request, "No shelves available.")
            else:
                shelf_number = random.choice(available_shelves)
                while True:
                    token = ''.join(random.choices('0123456789', k=4))
                    if not ShelfToken.objects.filter(token=token).exists():
                        break
                ShelfToken.objects.create(user=request.user, shelf_number=shelf_number, token=token, status='requested')
                messages.info(request, f"Shelf requested. Your Shelf Number: {shelf_number} and Token: {token}. Share shelf number with admin for approval.")
                return redirect('index')

    return render(request, "index.html", {
        'shelf_token': shelf_token,
    })


@login_required(login_url='/')
def request_retrieval(request):
    shelf_token = ShelfToken.objects.filter(user=request.user, status='assigned').order_by('-id').first()
    if shelf_token:
        shelf_token.status = 'retrieval_requested'
        shelf_token.save()
        messages.info(request, f"Retrieval requested. Please provide Shelf Number and Token ({shelf_token.token}) to admin for confirmation.")
    else:
        messages.error(request, "No assigned shelf found to retrieve.")
    return redirect('index')


def is_admin(user):
    return user.is_staff


@user_passes_test(is_admin, login_url='/')
def admin_shelves(request):
    pending_requests = ShelfToken.objects.filter(status='requested')
    assigned = ShelfToken.objects.filter(status='assigned')
    retrieval_requests = ShelfToken.objects.filter(status='retrieval_requested')
    collected = ShelfToken.objects.filter(status='collected')

    return render(request, "admin_shelves.html", {
        'pending_requests': pending_requests,
        'assigned': assigned,
        'retrieval_requests': retrieval_requests,
        'collected': collected,
    })


@user_passes_test(is_admin, login_url='/')
def approve_assignment(request):
    if request.method == "POST":
        shelf_number = request.POST.get('shelf_number')
        try:
            shelf_token = ShelfToken.objects.get(shelf_number=shelf_number, status='requested')
            shelf_token.status = 'assigned'
            shelf_token.save()
            messages.success(request, f"Assignment approved for shelf {shelf_number} (User: {shelf_token.user.username}).")
        except ShelfToken.DoesNotExist:
            messages.error(request, "Invalid shelf number or shelf already assigned.")
    return redirect('admin_shelves')


@user_passes_test(is_admin, login_url='/')
def confirm_retrieval(request):
    if request.method == "POST":
        shelf_number = request.POST.get('shelf_number')
        token = request.POST.get('token')
        try:
            shelf_token = ShelfToken.objects.get(shelf_number=shelf_number, token=token, status='retrieval_requested')
            shelf_token.status = 'collected'
            shelf_token.save()
            messages.success(request, f"Shelf {shelf_number} retrieval confirmed for user {shelf_token.user.username}. Shelf is now free.")
        except ShelfToken.DoesNotExist:
            messages.error(request, "Invalid shelf number or token, or retrieval not requested.")
    return redirect('admin_shelves')
