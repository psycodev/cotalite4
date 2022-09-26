from django import forms
from Transacciones.models import Transaccion

class registrarTransaccion(forms.ModelForm):
    
    class Meta: 
        model= Transaccion
        fields=[
            'id_tr',
            'tipo',
            'fecha_tr',
            'usuario',
            'concepto',   
            'monto',
        ]
        labels ={
            'id_tr':'Id Transaccion',
            'Tipo':'Tipo de transaccion',
            'fecha_tr':'Fecha de transaccion',
            'usuario':'Usuario',
            'concepto':'Concepto',   
            'monto':'Monto',
        }
        Widgets ={
            'id_tr': forms.Select(attrs={"class":"form"}),
            'Tipo': forms.TextInput(attrs={"class":"form"}),
            'fecha_tr': forms.TextInput(attrs={'class':'form-control'}),
            'usuario': forms.TextInput(attrs={'class':'form-control'}),
            'concepto': forms.TextInput(attrs={'class':'form-control'}),   
            'monto': forms.TextInput(attrs={'class':'form-control'}),
        }
