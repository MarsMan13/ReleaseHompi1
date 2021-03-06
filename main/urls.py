from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rsop2018', views.rsop, name='rsop'),
    path('rsop2018/projects/<int:pk>', views.project, name='rsop-projects'),
    path('rsop2018/projects/feedback/<int:pk>', views.project_feedback, name='rsop-project-feedback'),

    #Gun's Doing
    path('wewantU_releaseU', views.recruiting_2018, name='recruiting_2018'),
    #path('wewantU_releaseU_intro', views.recruiting_2018_intro, name='recruiting_2018_intro'),

]
