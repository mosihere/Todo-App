from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.


def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        form = TodoForm()

        context = {'todos': todos, 'form': form}
        return render(request, 'todo/index.html', context=context)
    
    elif request.method == 'POST':
        todos = Todo.objects.all()
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            form = TodoForm()
            context = {'todos': todos, 'form': form}
            return render(request, 'todo/index.html', context=context)


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    context = {'todo': todo}

    if request.method == 'POST':
        todo.delete()
        context = {'todo': todo}
        return redirect('todo:todo-list')

    return render(request, 'todo/detail.html', context=context)
    
        

