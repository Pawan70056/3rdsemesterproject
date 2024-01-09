# feedback_reviews/forms.py

from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['subject', 'message']  # Define the fields from the Feedback model
        # You can add widgets, labels, or customize form field attributes here if needed
