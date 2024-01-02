from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoForm
# Create your views here.


def todo_list(request):

    if request.user.is_authenticated:
        todos = Todo.objects.filter(owner=request.user).order_by('-last_update')
        form = TodoForm()
        context = {'todos': todos, 'form': form}
        return render(request, 'todo/index.html', context=context)
    else:
        return render(request, 'todo/index.html')


def todo_detail(request, pk):

    todo = get_object_or_404(Todo, pk=pk)

    if request.user == todo.owner:

        context = {'todo': todo}

        if request.method == 'POST':
            if request.POST.get('delete') == 'Delete':
                todo.delete()
                context = {'todo': todo}
                messages.success(request, f'Todo "{todo}" Has Been Deleted!')

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
    
    else:
        return redirect('todo:todo-list')


def edit_todo(request, pk):

    todo = get_object_or_404(Todo, pk=pk)

    if request.user == todo.owner:

        if request.method == 'GET':
            context = {'form': TodoForm(instance=todo), 'pk': pk}
            return render(request,'todo/update.html',context)
        
        elif request.method == 'POST':
            if request.POST.get('cancle') == 'Cancle':
                return redirect('todo:todo-list')
            
            else:
                form = TodoForm(request.POST, instance=todo)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'The Todo has been updated successfully.')
                    return redirect('todo:todo-list')
    else:
        return redirect('todo:todo-list')


def create_todo(request):

    if request.user.is_authenticated:

        if request.method == 'GET':
            form = TodoForm()
            context = {'form': form}
            return render(request,'todo/create.html', context)
        
        elif request.method == 'POST':
            if request.POST.get('cancle') == 'Cancle':
                return redirect('todo:todo-list')
            
            else:
                form = TodoForm(request.POST)
                if form.is_valid():
                    user = request.user
                    new_form = form.save(commit=False)
                    new_form.owner = user
                    new_form.save()
                    form = TodoForm()
                    context = {'form': form}
                    messages.success(request, 'The Todo has been Created successfully.')
                    return redirect('todo:todo-list')
    else:
        return redirect('todo:todo-list')