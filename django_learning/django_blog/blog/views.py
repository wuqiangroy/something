import json
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    res = {
        "name": "Roy",
        "age": 23,
        "university": "Southwest JiaoTong University",
        "dream": "work in XiaoMi"
    }
    return HttpResponse(json.dumps(res))


def get_data(request):

    name = request.GET.get("name", "")
    idCard = request.GET.get("idCard", "")
    res = {
        "name": name,
        "idCard": idCard
    }
    return HttpResponse(json.dumps(res))
