"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from feedback import views as feedback_views
from harmful import views as harmful_views
from pit import views as pit_views
from survey import views as survey_views
from userinfo import views as userinfo_views
from utterance import views as utterance_views
from prefer_character import views as prefer_character_views

from download import views as dlv

urlpatterns = [
    path('', dlv.hello_world),
    path('admin/', admin.site.urls),
    path('feedback/', feedback_views.FeedbackViewSet.as_view()),
    path('harmful/', harmful_views.HarmfulViewSet.as_view()),
    path('pit/', pit_views.PitViewSet.as_view()),
    path('survey/', survey_views.SurveyViewSet.as_view()),
    path('userinfo/', userinfo_views.UserinfoViewSet.as_view()),
    path('utterance/', utterance_views.UtteranceViewSet.as_view()),
    path('download/', dlv.download_file),
    path('prefer_character/', prefer_character_views.PreferCharacterViewSet.as_view())
]
