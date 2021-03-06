from . views import All_questions_View, Query_ques_View, Advance_search_View, Detail_View
from django.conf.urls import include,url
from django.urls import path

urlpatterns = [
    url('questions/$',All_questions_View.as_view(),name='all_ques'),
    # path('queryques/<str:query>/', Query_ques_View.as_view(),name='queryques'),
    # url(r'queryques/(?<query>\w+)/$',Query_ques_View.as_view(),name='queryques'),
    # url(r'queryques/(?<query>\w+)/(?P<page>\w+)/$',Query_ques_View.as_view(),name='queryques'),
    # url(r'queryques/(?P<query>\w+)/(?P<page>\w+)/(?P<sort>\w+)/$',Query_ques_View.as_view(),name='queryques'),

   	url('advsearch/$',Advance_search_View.as_view(),name='advsearch'),
   	url('answerdetails/$',Detail_View.as_view(),name='answerdetails'),
]
