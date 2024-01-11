# feedback_reviews/forms.py

# forms.py
from django import forms

from .models import ContactMessage, Feedback, ImprovementArea


class FeedbackForm(forms.ModelForm):
    improvement_areas = forms.ModelMultipleChoiceField(
        queryset=ImprovementArea.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'age', 'employment_status', 'experience_level', 'course_rating',
                  'materials_rating', 'recommend_course', 'improvement_areas', 'comments']




class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

        widgets = {
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message'}),
        }
