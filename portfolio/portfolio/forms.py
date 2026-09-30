from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    # Honeypot: bots ise bharte hain, insaan ko dikhta nahi
    website = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"tabindex": "-1", "autocomplete": "off"}),
    )

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Your email"}),
            "message": forms.Textarea(
                attrs={"placeholder": "Tell me about your project", "rows": 5}
            ),
        }

    def clean_website(self):
        if self.cleaned_data.get("website"):
            raise forms.ValidationError("Spam detected.")
        return ""

    def clean_message(self):
        text = self.cleaned_data["message"].strip()
        if len(text) < 10:
            raise forms.ValidationError("Please write at least 10 characters.")
        return text