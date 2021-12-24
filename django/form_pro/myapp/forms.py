from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *
from django.forms.widgets import Widget
from django.shortcuts import render

class CollegeForm(forms.ModelForm):
    class Meta:
        model= College
        fields= "__all__"

    department = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Enter Department"
            }
        )
    )
    college_name =forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Enter Name"
            }
        )
    )

    course = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Enter Course"
            }
        )
    )
    # image= forms.FileField(
    #     widget=forms.FileInput(
    #         attrs={
               
    #             "accept":"image/*"
    #         }
    #     )
    # )

    def clean_department(self):
        if len(self.cleaned_data.get('department'))<5:
            raise forms.ValidationError('length is less than 5')
        return self.cleaned_data.get('department')


    def clean_college_name(self):
        if len(self.cleaned_data.get('college_name'))<2:
            raise forms.ValidationError('invalid college name')
        return self.cleaned_data.get('college_name')


class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields="__all__"
