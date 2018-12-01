from django import forms
from django.views.generic import CreateView

# from .models import Point
from start_page.models import Point


class PointCreate(CreateView):
    model = Point
    fields = ('latitude', 'longitude')

    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user
    #     return super(self).form_valid(form)
