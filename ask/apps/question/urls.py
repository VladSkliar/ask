from django.conf.urls import patterns, url
from question import views

urlpatterns = patterns(
  'question.views',
  url(r'^(?P<pk>\d+)/$', views.AnswerListView.as_view(), name='answer_list'),
  url(r'^$', views.QuestionListView.as_view(), name='question_list'),
  url(r'^(?P<pk>\d+)/add_answer/$', views.AddAnswerUpdateView.as_view(),
      name='add_answer'),
  url(r'^(?P<pk>\d+)/add_question/$', views.QuestionCreateView.as_view(),
      name='add_question'),
)
