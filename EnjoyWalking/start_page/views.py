# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import urllib2
from django.shortcuts import render, render_to_response

from django.shortcuts import render

from start_page.forms import PointForm, AddPointForm
from start_page.models import Point


def post_list(request):
    return render(request, 'start_page/index1.html', {})


def getPoints(xa, ya, xb, yb):
    points = Point.objects.all().order_by('latitude')
    answ = list()
    answ.append((0, (xa, ya)))
    for i, point in enumerate(points):
        answ.append((i + 1, (point.latitude, point.longtitude)))
    answ.append((len(points) + 1, (xb, yb)))
    print(answ)
    return answ


# starting = 'https://route.api.here.com/routing/7.2/calculateroute.json?app_id=teFX7Xo13b2kOkodOS0E&app_code=gTUGnrxh2I0peZbAHwfe2Q&'
#  k = 1
#  xa, ya = 52.5, 13.4
#  xb, yb = 52.5, 13.45
#  starting_point = 'waypoint0=geo!' + str(xa) + "," + str(ya)
#  another_points = ""
#  ending_point = 'waypoint' + str(k) + '=geo!' + str(xb) + "," + str(yb)
#  endinf = 'mode=fastest;car;traffic:disabled'
# # serialized_data = urllib2.urlopen(starting + starting_point + another_points + ending_point + endinf).read()
#  url = "https://route.api.here.com/routing/7.2/calculateroute.json?app_id=teFX7Xo13b2kOkodOS0E&app_code=gTUGnrxh2I0peZbAHwfe2Q&waypoint0=geo!52.5,13.4&waypoint1=geo!58.5,13.4&waypoint2=geo!52.5,13.45&mode=fastest;car;traffic:disabled"
#  serialized_data = urllib2.urlopen(url).read()
#  data = json.loads(serialized_data)
#
#  #response = request.get()
#  #geodata = response.json()
#  geodata = data["response"]["route"][0]
# # points = geodata['maneuver']
#  print(geodata)
#  return geodata


def post_points(request):
    if request.method == 'POST':
        point_form = PointForm(request.POST)

        if True:
            xa, ya = point_form['latitude_a'].value(), point_form['longtitude_a'].value()
            xb, yb = point_form['latitude_b'].value(), point_form['longtitude_b'].value()
            return_points = getPoints(xa, ya, xb, yb)

            return render_to_response("start_page/points.html", {
                'points': return_points
            })
    form = PointForm()
    return render(request, 'start_page/index.html', {'form': form})


def add_point(request):
        add_point_form = AddPointForm()
        if request.method == "POST":
            add_point_form = AddPointForm(request.POST)
            if add_point_form.is_valid():
                point = add_point_form.save(commit=False)
                point.save()
                return render(request, 'start_page/add_point.html', {'form': add_point_form})
        return render(request, 'start_page/add_point.html', {'form': add_point_form})
