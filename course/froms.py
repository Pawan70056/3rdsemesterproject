# feedback_reviews/forms.py

from django import forms
from .models import Feedback, ImprovementArea

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
