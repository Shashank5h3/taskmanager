from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from .forms import RegisterForm
from django.utils.timezone import now
from .models import User
from .forms import ProjectForm
from .models import Project
from django.contrib.auth.decorators import login_required

def register_view(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # 🔥 IMPORTANT: manually assign role
            user.role = form.cleaned_data['role']

            user.save()
            login(request, user)

            if user.role == 'admin':
                return redirect('admin_dashboard')
            else:
                return redirect('member_dashboard')

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            if user.role == 'admin':
                return redirect('admin_dashboard')
            else:
                return redirect('member_dashboard')

    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def admin_dashboard(request):
    if request.user.role != 'admin':
        return redirect('member_dashboard')

    tasks = Task.objects.all()

    total = tasks.count()
    completed = tasks.filter(status='completed').count()
    pending = tasks.filter(status='pending').count()
    overdue = tasks.filter(deadline__lt=now(), status__in=['pending','in_progress']).count()

    context = {
        'total': total,
        'completed': completed,
        'pending': pending,
        'overdue': overdue,
        'tasks': tasks
    }
    context['now'] = now()

    return render(request, 'admin_dashboard.html', context)


@login_required
def member_dashboard(request):
    if request.user.role != 'member':
        return redirect('admin_dashboard')

    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'member_dashboard.html', {
    'tasks': tasks,
    'now': now()
})

@login_required
def create_task(request):
    if request.user.role != 'admin':
        return redirect('member_dashboard')

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')

    return render(request, 'create_task.html', {'form': form})


@login_required
def update_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.user != task.assigned_to:
        return redirect('member_dashboard')

    if request.method == 'POST':
        status = request.POST.get('status')
        task.status = status
        task.save()
        return redirect('member_dashboard')

    return render(request, 'update_task.html', {'task': task})

@login_required
def create_project(request):
    if request.user.role != 'admin':
        return redirect('member_dashboard')

    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            return redirect('admin_dashboard')

    return render(request, 'create_project.html', {'form': form})

@login_required
def project_list(request):
    if request.user.role != 'admin':
        return redirect('member_dashboard')

    projects = Project.objects.all()

    return render(request, 'project_list.html', {
        'projects': projects
    })

@login_required
def profile_view(request):
    user = request.user

    if request.method == 'POST':
        user.email = request.POST.get('email')
        user.bio = request.POST.get('bio')

        if request.FILES.get('profile_pic'):
            user.profile_pic = request.FILES.get('profile_pic')

        user.save()

    return render(request, 'profile.html', {'user': user})