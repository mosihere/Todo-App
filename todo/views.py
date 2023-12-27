from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.


def todo_list(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            todos = Todo.objects.filter(owner=request.user)
            form = TodoForm()
            context = {'todos': todos, 'form': form}
            return render(request, 'todo/index.html', context=context)
        else:
            return render(request, 'todo/index.html')

    elif request.method == 'POST':
        form = TodoForm(request.POST)
        todos = Todo.objects.filter(owner=request.user)

        if form.is_valid():
            user = request.user
            new_form = form.save(commit=False)
            new_form.owner = user
            new_form.save()
            form = TodoForm()
            context = {'todos': todos, 'form': form}
            return render(request, 'todo/index.html', context=context)


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    context = {'todo': todo}

    if request.method == 'POST':
        if request.POST.get('delete') == 'Delete':
            todo.delete()
            context = {'todo': todo}
            return redirect('todo:todo-list')
        elif request.POST.get('in progress') == 'In Progress':
            todo.status = 'I'
            todo.save()
        elif request.POST.get('pending') == 'Pending':
            todo.status = 'P'
            todo.save()
        elif request.POST.get('done') == 'Done':
            todo.status = 'D'
            todo.save()
        else:
            pass

    return render(request, 'todo/detail.html', context=context)
    
        

