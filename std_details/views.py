from django.shortcuts import render
from django.http import HttpResponse
from std_details.models import Studentmd_details #(model name)
from std_details import forms

# Create your views here.
def home(Request):
    #return HttpResponse('Students details Home Page')

    return render(Request, 'Student_details/home.html')#temp student_detail/home.html


def reg(Request):
    form = forms.Student_forms()
    #return HttpResponse("This is Students Registration page")
    return render(Request, 'Student_details/reg.html', context=dict({'form_d':form}))

def detail(Request):
    #return HttpResponse('This is Student details page')
    student_mdl_details = Studentmd_details.objects.order_by('Std_Id')
    student_details_dict = {'insert_student_details': student_mdl_details}
    return render(Request, 'Student_details/details.html', context=student_details_dict)
