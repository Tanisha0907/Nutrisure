from django import forms
from .models import User
from .models import Feedback

class FoodIntakeForm(forms.ModelForm):
    class Meta:
        model = User


    fields = [
        "height",
        "weight",
        "gender",
        "breakfast",
        "lunch",
        "dinner",
    ]

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback


    fields = [
        "fullname",
        "feedback",
    ]



