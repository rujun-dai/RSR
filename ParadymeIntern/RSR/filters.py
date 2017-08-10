# this file is for search/export team to create filters
import django_filters
from .models import *
from django import forms
from dal import autocomplete
from django.db.models import Q

WORKAUTHORIZATION_CHOICES = (
        ('Citizenship', 'Citizenship'),
        ('Permanent Resident', 'Permanent Resident'),
        ('Visa', 'Visa')
    )
class PersonFilter(django_filters.FilterSet):
    SchoolAttend = django_filters.ModelChoiceFilter(name='persontoschool__SchoolID', queryset=School.objects.all().order_by('Name'),
                                                    to_field_name='Name')
    GraduateDate = django_filters.ModelChoiceFilter(name='persontoschool__GradDate',
                                                    queryset=PersonToSchool.objects.values_list('GradDate',flat=True).
                                                    distinct().order_by('GradDate'),
                                                    to_field_name='GradDate')
    Major = django_filters.ModelChoiceFilter(name='persontoschool__MajorID', queryset=Major.objects.all().order_by('Name').distinct())
    DegreeLevel = django_filters.ModelChoiceFilter(name='persontoschool__SchoolID__DegreeLevel',
                                                   queryset=School.objects.values_list('DegreeLevel',flat=True).distinct(),
                                                   to_field_name='DegreeLevel')
    GPAlb = django_filters.NumberFilter(name='persontoschool__GPA',lookup_expr='gte')
    GPAub = django_filters.NumberFilter(name='persontoschool__GPA',lookup_expr='lt')
    Coursework = django_filters.ModelMultipleChoiceFilter(name='persontocourse__Desc',
                                                  queryset=PersonToCourse.objects.distinct().order_by('Desc'),
                                                  widget=autocomplete.ModelSelect2Multiple(
                                                  url='RSR:Coursework-autocomplete'),
                                                  conjoined = True)
    Language = django_filters.ModelMultipleChoiceFilter(name='persontolanguage__LangID',
                                                queryset=LanguageSpoken.objects.all(),
                                                widget=autocomplete.ModelSelect2Multiple(url='RSR:LanguageSpoken-autocomplete'),
                                                        conjoined=True)
    Skills = django_filters.ModelMultipleChoiceFilter(name='persontoskills__SkillsID',
                                              queryset=Skills.objects.all().order_by('Name').distinct(),
                                              widget=autocomplete.ModelSelect2Multiple(url='RSR:Skills-autocomplete'),
                                                      conjoined=True)
    YearOfExperienceForSkill = django_filters.ModelChoiceFilter(name='persontoskills__YearsOfExperience',lookup_expr='gte',
                                                                queryset=PersonToSkills.objects.values_list('YearsOfExperience',flat=True).
                                                                order_by('YearsOfExperience').distinct(),to_field_name='YearsOfExperience')
    ProfessionalDevelopment = django_filters.ModelMultipleChoiceFilter(name='persontoprofessionaldevelopment__ProfID',
                                                               queryset=ProfessionalDevelopment.objects.all().order_by('Name'),
                                                               widget=autocomplete.ModelSelect2Multiple(url='RSR:ProfessionalDevelopment-autocomplete'),
                                                                       conjoined=True)
    Award = django_filters.ModelMultipleChoiceFilter(name='persontoawards__AwardID',
                                             queryset=Awards.objects.all().order_by('Name').distinct(),
                                             widget=autocomplete.ModelSelect2Multiple(url='RSR:Awards-autocomplete'), conjoined=True)
    CompanyWorked = django_filters.ModelMultipleChoiceFilter(name='persontocompany__CompanyID',
                                                     queryset=Company.objects.all().order_by('Name').distinct(),
                                                     widget=autocomplete.ModelSelect2Multiple(url='RSR:Company-autocomplete'),
                                                             conjoined=True)
    Title = django_filters.ModelMultipleChoiceFilter(name='persontocompany__Title',
                                             queryset=PersonToCompany.objects.order_by('Title').distinct(),
                                             widget=autocomplete.ModelSelect2Multiple(
                                                 url='RSR:Title-autocomplete'), conjoined=True)
    Volunteering = django_filters.ModelMultipleChoiceFilter(name='persontovolunteering__VolunID',
                                                    queryset=Volunteering.objects.all().distinct().order_by('Name'),
                                                    widget=autocomplete.ModelSelect2Multiple(url='RSR:Volunteering-autocomplete'),
                                                            conjoined=True)
    Club_Hobby = django_filters.ModelChoiceFilter(name='persontoclubshobbies_set__CHID',
                                                  queryset=Clubs_Hobbies.objects.all().distinct().order_by('Name'),
                                                  to_field_name='Name')
    SecurityClearance = django_filters.ModelChoiceFilter(name='persontoclearance__ClearanceLevel',
                                                         queryset=Clearance.objects.all().distinct())
    WorkAuthorization = django_filters.ChoiceFilter(name='WorkAuthorization', choices=WORKAUTHORIZATION_CHOICES)
    Name = django_filters.ModelMultipleChoiceFilter(name='Name', queryset=Person.objects.all(),
                                          widget=autocomplete.ModelSelect2Multiple(url='RSR:SearchBar-autocomplete'))


    class Meta:
        model = Person
        fields = ['SchoolAttend', 'GraduateDate', 'Major', 'DegreeLevel', 'GPAlb', 'GPAub','Language', 'Skills',
                  'YearOfExperienceForSkill', 'ProfessionalDevelopment', 'Award', 'CompanyWorked', 'Title',
                  'SecurityClearance', 'Volunteering', 'Club_Hobby', 'Name','WorkAuthorization', 'Coursework']
