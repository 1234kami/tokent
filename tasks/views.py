from django.shortcuts import render
from django.shortcuts import redirect
from tasks.models import Task


def get_list(request):
    if request.method == 'GET':
        tasks = Task.objects.filter(is_active=True).order_by('-id')
        return render(request, 'index.html', {"tasks": tasks})


def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        created_at = request.POST.get('created_at')
        type = request.POST.get('type')
        task = Task.objects.create(title=title, description=description, created_at=created_at, type=type)
        return redirect('index')
    return render(request, 'index.html')


def update_task(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        created_at = request.POST.get('created_at')
        type = request.POST.get('type')
        task = Task.objects.filter(id=id, is_active=True).first()
        task.title = title
        task.description = description
        task.created_at = created_at
        task.type = type
        task.save()
        return redirect('index')
    context = {
        'data': Task.objects.filter(id=id, is_active=True).first()
    }
    return render(request, 'update.html', context)


def delete_task(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id, is_active=True)
        task.is_active = False
        task.save()
        return redirect('index')
    return render(request, 'index.html')

# Create your views here.
