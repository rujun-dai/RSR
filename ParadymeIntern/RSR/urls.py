"""ParadymeIntern URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
from RSR.views import *

app_name = 'RSR'

urlpatterns = [

    url(r'^uploaddoc/$', views.uploaddoc, name='uploaddoc'),
    url(r'^uploadlist/$', uploadlist, name = 'uploadlist'),
    url(r'^listdelete/$', listdelete, name="listdelete"),
    url(r'^main/$', main, name = 'main'),
    url(r'^ocr/$', ocr, name='ocr'),
    url(r'^parsing/$', parsing, name='parsing'),
    url(r'^search/$', search, name='search'),
    url(r'^user_access/$', user_acc_cont, name='user_access'),
    url(r'^export/$', export, name='export'),
    url(r'^linkanalysis/$', linkanalysis, name='linkanalysis'),

    #Search/Export Team
    url(r'^search/person_detail/(?P<pk>[0-9]+)/$', views.detail, name='detail'),

        #url for autocomplete function for ProfessionalDevelopment class
    url(r'^search/ProfessionalDevelopment-autocomplete/$', ProfessionalDevelopmentAutocomplete.as_view(),
        name='ProfessionalDevelopment-autocomplete',),
        #url for autocomplete function for skills class
    url(r'^search/Skills-autocomplete/$', Skillsutocomplete.as_view(),
        name='Skills-autocomplete',),
        #url for autocomplete function for Volunteering class
    url(r'^search/Volunteering-autocomplete/$', Volunteeringautocomplete.as_view(),
        name='Volunteering-autocomplete',),
        #url for autocomplete function for search bar
    url(r'^search/SearchBar-autocomplete/$', SearchBarautocomplete.as_view(),
        name='SearchBar-autocomplete',),
        #url for autocomplete function for LanguageSpoken class
    url(r'^search/Language-autocomplete/$', Languageautocomplete.as_view(),
        name='LanguageSpoken-autocomplete',),
        #url for autocomplete function for Company class
    url(r'^search/Company-autocomplete/$', Companyautocomplete.as_view(),
        name='Company-autocomplete',),
        #url for autocomplete function for coursework class
    url(r'^search/Coursework-autocomplete/$', Courseworkautocomplete.as_view(),
        name='Coursework-autocomplete',),
        #url for autocomplete function for Awards class
    url(r'^search/Awards-autocomplete/$', Awardsautocomplete.as_view(),
        name='Awards-autocomplete',),
        #url for autocomplete function for Title class
    url(r'^search/Title-autocomplete/$', Titleautocomplete.as_view(),
        name='Title-autocomplete',)

]
