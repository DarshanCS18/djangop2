from django import forms

class Student_forms(forms.Form):
    Std_Id= forms.IntegerField()
    Name= forms.CharField()
    Age= forms.IntegerField()
    Gender= forms.CharField()
    Phone= forms.IntegerField()
    Email=forms.EmailField()