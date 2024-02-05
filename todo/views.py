from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoForm
from .tasks import send_email_todos
import os
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from django.template.loader import render_to_string



def todo_list(request):

    if request.user.is_authenticated:
        todos = Todo.objects.filter(owner=request.user).order_by('-last_update')
        context = {'todos': todos}
        return render(request, 'todo/index.html', context=context)
    else:
        return redirect('home:home')


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
                form = TodoForm(request.POST, request.FILES, instance=todo)
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
                form = TodoForm(request.POST, request.FILES)
                if form.is_valid():
                    user = request.user
                    new_form = form.save(commit=False)
                    new_form.owner = user
                    new_form.save()
                    messages.success(request, 'The Todo has been Created successfully.')
                    return redirect('todo:todo-list')
    else:
        return redirect('todo:todo-list')
    

def send_user_todo_by_email(request):

    if request.user.is_authenticated:
        user = request.user
        user_email = request.user.email
        user_todos = Todo.objects.filter(owner=user)
        serialized_data = serialize("json", user_todos)
        serialized_data = json.loads(serialized_data)

        send_email_todos.delay(
            user_email,
            render_to_string('todo/todo_mail_template.html', {'todos': user_todos}),
            os.environ.get('GMAIL', '')
        )

        return render(request, 'todo/email_success.html')
    
    else:
        return redirect('todo:todo-list')