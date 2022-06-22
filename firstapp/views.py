from django.shortcuts import render,redirect
from firstapp.form import ToDoform
from firstapp.models import tab

# Create your views here.
def home(request):
    form=ToDoform()
    todos=tab.objects.all()
    if request.method=='POST':
        form=ToDoform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'home.html',{'form':form,'todo':todos})

    # update data
def update(request,todo_id):
    todo=tab.objects.get(id=todo_id)
    form=ToDoform(instance=todo)
    if request.method=='POST':
        form=ToDoform(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'update.html',{'form':form})

    # delete data

def delete(request,todo_id):
    todo=tab.objects.get(id=todo_id)
    todo.delete()
    return redirect('/')
    
   