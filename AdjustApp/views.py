from dataclasses import fields
from itertools import groupby
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.db.models import Sum
import pandas as pd
from AdjustApp.models import Metric
from AdjustApp.serializers import MetricSerializer
import csv
import json
import sqlite3


def mainf_():
    url = 'https://gist.githubusercontent.com/kotik/3baa5f53997cce85cc0336cb1256ba8b/raw/3c2a590b9fb3e9c415a99e56df3ddad5812b292f/dataset.csv'
    df = pd.read_csv(url)

    with open('AdjustApp/data_/dataset.csv') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            Metric.objects.get_or_create(
                date=row[0],
                channel=row[1],
                country=row[2],
                os=row[3],
                impressions=row[4],
                clicks=row[5],
                installs=row[6],
                spend=row[7],
                revenue=row[8],
            )


def execute_query(paramDict_):

    # Group By
    groupby_ = ''
    if paramDict_["groupb"]:
        for item in paramDict_["groupb"]:
            groupby_ = groupby_ + item + ', '
        groupbyC_ = " GROUP BY " + groupby_[0:-2]

    # Conditional query
    whereC_ = ''
    if paramDict_["dateb"]:
        whereC_ = "WHERE date < '" + paramDict_["dateb"] + "'"
    if paramDict_["datea"]:
        whereC_ = "WHERE date > '" + paramDict_["datea"] + "'"
    if paramDict_["datef"] and paramDict_["datet"]:
        whereC_ = "WHERE date BETWEEN '" + \
            paramDict_["datef"] + "' AND '" + paramDict_["datet"] + "'"

    if paramDict_["os"]:
        whereC_ = whereC_ + " AND os = '" + paramDict_["os"] + "'"

    if paramDict_["country"]:
        whereC_ = whereC_ + " AND country = '" + paramDict_["country"] + "'"

<<<<<<< HEAD
    # cpi calculation
=======
    #cpi calculation
>>>>>>> 2058c8b019184318045a783fcc9efb667ccace53
    cpi_ = ''
    if paramDict_["isCpi"]:
        cpi_ = ", spend/installs AS cpi"

    # Aggregate
    aggrC_ = ''
    if paramDict_["sum"]:
        for item in paramDict_["sum"]:
            aggrC_ = aggrC_ + "SUM(" + item + ") AS " + item + ","

    # Select clause
    selectC_ = groupby_ + aggrC_[0:-1] + cpi_

    # Order By
    orderC_ = ''
    if paramDict_["orderb"]:
        orderC_ = " ORDER BY " +paramDict_["orderb"]

    # Is descending
    if paramDict_["desc"]:
        orderC_ = orderC_ + " desc"

    conn = sqlite3.connect('db.sqlite3')
    sql_query = pd.read_sql_query('''
                                SELECT '''
                                  + selectC_ +
                                  ''' FROM AdjustApp_metric '''
                                  + whereC_ 
                                  + groupbyC_
                                  + orderC_
                                  , conn)

    df = pd.DataFrame(sql_query)
    json_list = json.loads(json.dumps(list(df.T.to_dict().values())))
    conn.close()

    return json_list


@csrf_exempt
def root_(request):
    if request.method == 'GET':
        groupb = request.GET.getlist('groupb')
        orderb = request.GET.get('orderb')
        order_isDesc = request.GET.get('desc')
        dateBefore = request.GET.get('dateb')
        dateAfter = request.GET.get('datea')
        dateFrom = request.GET.get('datef')
        dateTo = request.GET.get('datet')
        sum = request.GET.getlist('sum')
        os = request.GET.get('os')
        country = request.GET.get('country')
        isCpi = request.GET.get('isCpi')

        paramDict = {
            "groupb": groupb,
            "orderb": orderb,
            "desc": order_isDesc,
            "dateb": dateBefore,
            "datea": dateAfter,
            "datef": dateFrom,
            "datet": dateTo,
            "sum": sum,
            "os": os,
            "country": country,
            "isCpi": isCpi
        }

        jsonOutput = execute_query(paramDict)

        return JsonResponse(jsonOutput, safe=False)
