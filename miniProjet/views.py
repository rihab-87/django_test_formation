from django.http import HttpResponse
from formation.models import Formation,Chapitre
from formation.forms import AddChap, AddForm
from django.shortcuts import render

def home(request,add="",edit=""):
    formF=AddForm()
    formC=AddChap()
    if(edit):
        chap_à_editer=Chapitre.objects.get(pk=edit)
        formC=AddChap(instance=chap_à_editer)
    formation=Formation.objects.all
    chapitre=Chapitre.objects.all
    context={'formF':formF,'formation':formation,'formC':formC,'chapitre':chapitre,'add':add,'edit':edit,}
    return render(request,"home.html",context)