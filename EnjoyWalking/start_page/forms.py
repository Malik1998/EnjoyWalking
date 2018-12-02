from django import forms
from django.views.generic import CreateView

# from .models import Points
from start_page.models import Point, Points


class PointForm(forms.ModelForm):

    class Meta:
        model = Points
        fields = ['latitude_a', 'longtitude_a', 'latitude_b', 'longtitude_b']

    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user
    #     return super(self).form_valid(form)


class AddPointForm(forms.ModelForm):

    class Meta:
        model = Point
        fields = ['latitude', 'longtitude', 'rating', 'description']
