from django.shortcuts import redirect, render
from django.urls import reverse
from miniProjet.views import home
from formation.models import Chapitre, Formation
from . forms import AddForm,AddChap

def addFormation(request):
    if request.method =='POST':
        print(request.POST)
        form=AddForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

def addChapitre(request,id):
        add = id
        return home(request,add=add,edit="")
        
        
def add_nouveau_Chapitre(request,id):
    add=False
    if request.method=='POST':
        form=AddChap(request.POST)
        formation=Formation.objects.filter(pk=id)
        if form.is_valid():
            Chap=Chapitre.objects.create(nom_chapitre=request.POST['nom_chapitre'],formation=formation[0])
            Chap.save()
        return redirect('home')

def editChapitre(request,id):
        edit = id
        return home(request,add="",edit=edit)

def edit_Chapitre(request,id):
    if request.method=='POST':
        chap_à_editer=Chapitre.objects.get(pk=id)
        form=AddChap(request.POST,instance=chap_à_editer)
        if form.is_valid():
            form.save()
        return redirect('home')

def supChapitre(request,id):
    chap_à_supp=Chapitre.objects.get(pk=id)   
    chap_à_supp.delete()
    return redirect('home')       

def supFormation(request,id):
    formation_à_supp=Formation.objects.get(pk=id)   
    formation_à_supp.delete()  
    return redirect('home')  