# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response

from django.shortcuts import render

from start_page.forms import PointCreate


def post_list(request):
    return render(request, 'start_page/index.html', {})


def getPoints(request, xa, ya, xb, yb):
    starting = 'https://route.api.here.com/routing/7.2/calculateroute.json?app_id=teFX7Xo13b2kOkodOS0E&app_code=gTUGnrxh2I0peZbAHwfe2Q&'
    k = 1
    xa, ya = 52.5, 13.4
    xb, yb = 52.5, 13.45
    starting_point = 'waypoint0=geo!' + str(xa) + "," + str(ya)
    another_points = ""
    ending_point = 'waypoint' + str(k) + '=geo!' + str(xb) + "," + str(yb)
    endinf = 'mode=fastest;car;traffic:disabled'
    response = request.get(starting + starting_point + another_points + ending_point + endinf)
    geodata = response.json()
    points = geodata['maneuver']
    print(points)
    return points


def post_points(request):
    if request.method == 'POST':
        point_form = PointCreate(request.POST)

        if True:
            xa, ya = point_form.cleaned_data['f_lat'], point_form.cleaned_data['f_lon']
            xb, yb = point_form.cleaned_data['s_lat'], point_form.cleaned_data['s_lon']

            return_points = getPoints(request, xa, ya, xb, yb)

            return render_to_response("start_page/points.html.html", {
                'points': return_points
            })
    form = PointCreate()
    return render(request, 'start_page/index.html', {'form': form, 'd':23})
