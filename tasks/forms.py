from django.forms import ModelForm, CheckboxSelectMultiple, BooleanField
from .models import Task, Label


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'labels'
        ]
        widgets = {
            'labels': CheckboxSelectMultiple
        }

    def __init__(self, user=None, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        if user:
            self.instance.owner = user
        if self.instance.pk:
            initial_completion_status = self.instance.completion_status
            self.fields['completion_status'] = BooleanField(
                label='Completed?', required=False,
                initial=initial_completion_status
                )
