from question.models import Question
from django.forms import ModelForm


class AddAnswerForm(ModelForm):
    class Meta:
        model = Question
        exclude = ('respondent',)


class AddQuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ('respondent', 'answer',)
