from django import forms


from .models import Chapitre, Formation

class AddForm(forms.ModelForm):
    class Meta:
        model=Formation
        
        widgets = {
            'titre': forms.TextInput(attrs={'placeholder': 'titre de formation'}),
            'description': forms.TextInput(
                attrs={'placeholder': 'description'}),
            'durée': forms.TextInput(
                attrs={'placeholder': 'durée du formation'}),
           
        }
        fields=['titre','description','durée']

class AddChap(forms.ModelForm):
    class Meta:
        model=Chapitre
        
        widgets = {
            'nom_chapitre': forms.TextInput(attrs={'placeholder': 'Nom de chapitre '}),
            
           
           
        }
        fields=['nom_chapitre']

              