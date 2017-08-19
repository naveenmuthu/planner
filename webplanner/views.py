from django.shortcuts import render, render_to_response
from models import todo
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _

class ArticleForm(ModelForm):
    class Meta:
        model = todo
        fields = ['title','priority','time_estimated', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'size': 80}),
            'time_estimated': forms.TextInput(attrs={'size': 3}),
        }
        help_texts = {
            'time_estimated': _('mins'),
        }

# Create your views here.
def index(request):

    items = todo.objects.filter(completed='False')

    return render_to_response('index.html', {'items': items})

def addtask(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ArticleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            new_todo = form.save()
            return HttpResponseRedirect('/')

    else:
        form = ArticleForm()

    return render(request, 'addtask.html', {'form': form})

def edittask(request, taskid):
    instance = todo.objects.get(pk=taskid)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ArticleForm(request.POST, instance=instance)
        # check whether it's valid:
        if form.is_valid():
            edited_todo = form.save()
            return HttpResponseRedirect('/')

    else:
        form = ArticleForm(instance=instance)

    return render(request, 'edittask.html', {'form': form, 'taskid': taskid})