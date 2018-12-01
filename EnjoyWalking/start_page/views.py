# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import urllib2
from django.shortcuts import render, render_to_response

from django.shortcuts import render

from start_page.forms import PointForm
from start_page.models import Point


def post_list(request):
    return render(request, 'start_page/index.html', {})


def getPoints(xa, ya, xb, yb):
    points = Point.objects.all()
    answ = list()
    answ.append((0, (xa, ya)))
    for i, point in enumerate(points):
        answ.append((i + 1, (point.latitude, point.latitude)))
    answ.append((len(points) + 1, (xb, yb)))
    print(answ)
    return answ



   #starting = 'https://route.api.here.com/routing/7.2/calculateroute.json?app_id=teFX7Xo13b2kOkodOS0E&app_code=gTUGnrxh2I0peZbAHwfe2Q&'
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

        # p = Point()
        # p.latitude='55.7522'
        # p.longtitude='37.6156'
        # p.rating=8
        # p.description='Moscow Arbat'
        # p.save()
        if True:
            xa, ya = point_form['latitude_a'].value(), point_form['longtitude_a'].value()
            xb, yb = point_form['latitude_b'].value(), point_form['longtitude_b'].value()
            xa, ya = 55.7558472, 37.5837
            xb, yb = 55.7559472, 37.5847
            return_points = getPoints(xa, ya, xb, yb)

            return render_to_response("start_page/points.html", {
                'points': return_points
            })
    form = PointForm()
    return render(request, 'start_page/index.html', {'form': form})
