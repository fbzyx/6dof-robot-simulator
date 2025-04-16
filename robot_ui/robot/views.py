from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils.jacobi import forward_kinematics
import json


def main_view(request):
    return render(request, "index.html")


def main_view2(request):
    return render(request, "index2.html")


def main_view3(request):
    return render(request, "index3.html")


def main_view4(request):
    return render(request, "index4.html")


def move_func(request):
    return JsonResponse({})


def get_matrix(request):
    return JsonResponse({})


@csrf_exempt
def jacobi_api(request):
    if request.method == "POST":

        data = json.loads(request.POST["data"])
        joint_angles = data.get("joint_angles", [])
        j = forward_kinematics(joint_angles)
        return JsonResponse({"jacobi": j.tolist()})
