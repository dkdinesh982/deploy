from django import forms
class FeedbackForm(forms.Form):
    name=forms.CharField(
        label="Enter Your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Name'
            }
        )
    )
    rating=forms.IntegerField(
        label="Enter Your Rating Beteween 1 and 5: ",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'rating'
            }
        )
    )
    feedback=forms.CharField(
        label="Enter Your Feedback",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'FeedBack'
            }
        )
    )