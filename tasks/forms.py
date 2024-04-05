from django.forms import ModelForm, CheckboxSelectMultiple, BooleanField
from .models import Task, Label


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'labels',
            'completion_status'
        ]
        widgets = {
            'labels': CheckboxSelectMultiple
        }

    def __init__(self, user=None, *args, **kwargs):
        task_instance = kwargs.get('instance')
        super(TaskForm, self).__init__(*args, **kwargs)
        if user:
            self.instance.owner = user
        if task_instance:
            self.fields['completion_status'].label = 'Completed?'
            self.fields['completion_status'].required = False

            # Pre-populate title and description fields
            self.initial['title'] = task_instance.title
            self.initial['description'] = task_instance.description

            # Pre-select labels associated with the task
            self.initial['labels'] = task_instance.labels.values_list(
                'pk', flat=True
                )


class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = [
            'name'
        ]

    def __init__(self, user=None, *args, **kwargs):
        super(LabelForm, self).__init__(*args, **kwargs)
        if user:
            self.instance.owner = user
