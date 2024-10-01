from django import forms

class TriggerWorkflowForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter name'})
    )
    relation = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter relation'})
    )
    style = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter style'})
    )
    additional_info = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Enter additional information', 'rows': 3})
    )

