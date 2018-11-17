from django import forms
from .models import Mascota
#clases para agregar loquiear y para las mascotas 
#en ellas les decimos todo los que los usuarios o mascotas deven tener por el cual seran sus partenencias

class AgregarUsuario(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="contraseña")
    correo=forms.EmailField(widget=forms.EmailInput(),label="Correo")
    
class Login(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="contraseña")


#aqui se define estado de la mascota la cual estara en ella si disponible , rescatada o adoptada
estado=(
    ('Rescatado','Rescatado'),
    ('Disponible','Disponible'), 
    ('Adoptado','Adoptado'),
)

 
class Mascotas(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = [
        'mascotaname',
        'raza',
        'generomascota',
        'estado',
        'foto'
    ]

   
    estado=forms.ChoiceField(choices=estado, initial='Rescatado')
  
    widgets ={
        'mascotaname': forms.TextInput(attrs={'class':'form=control'}),
        'raza': forms.TextInput(attrs={'class':'form=control'}),
        'generomascota': forms.TextInput(attrs={'class':'form=control'}),
        
    }
    