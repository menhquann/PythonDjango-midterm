from django.shortcuts import get_object_or_404, redirect, render
from .models import Csvc
from .forms import CsvcForm

# Create your views here.


def create_view(request):
    initial_values = {
        'code': "E101",
        'name': "Phong E101",
        'den':10,
        'ban_ghe':40,
        'may_chieu':1,
        'quat':4,
        'dieu_hoa':2
        
    }
    form = CsvcForm(request.POST or None, initial=initial_values)
    if form.is_valid():
        form.save()
        form = CsvcForm()
        return redirect('/')
    context = {'form': form}
    return render(request, 'create.html', context)

def update_view(request, id):
    student = get_object_or_404(Csvc, id=id)
    form = CsvcForm(request.POST or None, instance=student)
    if request.method == "POST":
        form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'create.html', context)

def delete_view(request, id):
    student = get_object_or_404(Csvc, id=id)
    if request.method == "POST":
        student.delete()
        return redirect('/')
    context = {'student': student}
    return render(request, 'delete.html', context)

def detail_view(request, id):
    student = Csvc.objects.get(id=id)
    # student = get_object_or_404(Csvc, id=id)
    context = {'student': student}
    return render(request, 'detail.html', context) 

def list_view(request):
    keyword = request.GET.get('keyword')
    sort_by="name"
    if keyword:
        queryset = Csvc.objects.filter(code__icontains=keyword) | Csvc.objects.filter(name__icontains=keyword)
    else:
        queryset = Csvc.objects.all()
    context = {
        'students': queryset.order_by(sort_by),
        'keyword':keyword
    }
    return render(request, 'list.html', context) 
