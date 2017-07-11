import json
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from .models import User
from .form import PanelForm


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


def panel(request):
    if request.method == "POST":
        form = PanelForm(request.POST)

        if form.is_valid():
            name = request.POST.get("name")
            password = request.POST.get("password")
            user = User.objects.filter(username=name)
            if user and user.verify_password(password):
                return HttpResponseRedirect("/api/home/")
            else:
                data = {
                    "code": 1201,
                    "msg": "账户或密码错误",
                    "data": None
                }
                return HttpResponse(json.dumps(data))
    else:
        form = PanelForm()
        return render(request, "login.html", {"form": form})
