import django_filters
from django import forms
from Helloworld.models import post


class PostFilter(django_filters.rest_framework.FilterSet):
    created_on = django_filters.DateTimeFilter(widget=forms.DateInput(attrs={'type': 'date'}), lookup_expr='date_exact')


    class Meta:
        model = post
        fields = ['created_on']


