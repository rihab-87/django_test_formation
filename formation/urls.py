from django.urls import path
from . import views
urlpatterns = [
    
    path('addFormation/', views.addFormation, name="addFormation"),
    path('addChapitre/<int:id>', views.addChapitre, name="addChapitre"),
    path('add_nouveau_Chapitre/<int:id>', views.add_nouveau_Chapitre, name="add_nouveau_Chapitre"),
    path('editChapitre/<int:id>', views.editChapitre, name="editChapitre"),
    path('edit_Chapitre/<int:id>', views.edit_Chapitre, name="edit_Chapitre"),
    path('supChapitre/<int:id>', views.supChapitre, name="supChapitre"),
    path('supFormation/<int:id>', views.supFormation, name="supFormation"),
]
