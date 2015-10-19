from django.views.generic import ListView, UpdateView, CreateView
from braces.views import LoginRequiredMixin
from question.models import Question
from django.core.urlresolvers import reverse_lazy
from question.forms import AddAnswerForm, AddQuestionForm
from django.contrib.auth.models import User


class AnswerListView(LoginRequiredMixin, ListView):
    model = Question
    template_name = 'question/answer_list.html'

    def get_queryset(self):
        qs = super(AnswerListView, self).get_queryset()
        qs = qs.filter(respondent=self.kwargs['pk']).exclude(answer='')
        return qs

    def get_context_data(self, **kwargs):
        context = super(AnswerListView, self).get_context_data(**kwargs)
        context['respondent_id'] = self.kwargs['pk']
        return context


class QuestionListView(LoginRequiredMixin, ListView):
    model = Question
    template_name = 'question/question_list.html'

    def get_queryset(self):
        qs = super(QuestionListView, self).get_queryset()
        qs = qs.filter(respondent=self.request.user)
        return qs


class AddAnswerUpdateView(LoginRequiredMixin, UpdateView):
    model = Question
    form_class = AddAnswerForm
    template_name = "question/add_answer_form.html"

    def form_valid(self, form):
        form.respondent = self.request.user
        form.save()
        return super(AddAnswerUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('question_list')


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    template_name = 'question/add_question.html'
    form_class = AddQuestionForm

    def form_valid(self, form):
        form.instance.respondent_id = self.kwargs['pk']
        return super(QuestionCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('index')


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'question/user_list.html'
    context_object_name = 'list'

    def get_queryset(self):
        qs = super(UserListView, self).get_queryset()
        qs = qs.order_by('-date_joined')[:5]
        return qs
