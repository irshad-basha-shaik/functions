from django.shortcuts import render
from app2.models import SettingModel
from app2.forms import SettingsForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

# Create your views here.
def new(request):
    context = {}
    context['form'] = SettingsForm()
    if request.method== 'POST':
       # form = SettingsForm(request.POST or None)
        form = SettingsForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return render(request,"list.html",{'form':form})
    return render(request,"index.html",context)
def list(request):
    list = SettingModel.objects.all()
    return render(request,"list.html",{"list":list})
def edit(request,id):
    obj = get_object_or_404(SettingModel, pk=id)
    context = {}
    form = SettingsForm(instance=obj)
    if request.method== 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            obj = form.save()
            form = SettingsForm(instance=obj)
            return render(request, "list.html", {'form': form})
    context['form'] = form
    return render(request,"index.html",context)
def delete(request,id):
    context = {}
    obj = get_object_or_404(SettingModel, id=id)
    obj.delete()
    return HttpResponseRedirect("/")

