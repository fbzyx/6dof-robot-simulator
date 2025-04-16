from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_htmx.http import (
    trigger_client_event,
    HttpResponseClientRedirect,
    HttpResponseClientRefresh,
)
from .forms import PositionForm, RobotForm
from .models import Position, Robot
from .utils.dh import forward_kinematics
from .utils.interpolate import get_interpolated_matrix_data
import json


def main_view(request):
    objs = Position.objects.all()
    params = Robot.objects.all().first()
    context = {
        "form": PositionForm(),
        "form_params": RobotForm(instance=params),
        "objs": objs,
        "params": params,
    }
    return render(request, "index.html", context=context)


def robot_parameters(request):
    if request.htmx:
        if request.POST:
            form = RobotForm(data=request.POST)
            if form.is_valid():
                Robot.objects.all().delete()
                obj = form.save(commit=False)
                obj.save()
                return HttpResponseClientRefresh()

            context = {"form_params": form}

            return render(request, "partials/form_params.html", context=context)


def create_position(request):
    if request.htmx:
        if request.POST:
            form = PositionForm(data=request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()

                form = PositionForm(instance=obj)

            context = {"form": form}
            ret = render(request, "partials/form.html", context)

            return trigger_client_event(
                ret,
                "reload_list",
                params={},
                after="settle",
            )


def delete_position(request, id):
    Position.objects.get(id=id).delete()
    objs = Position.objects.all()
    context = {"objs": objs}
    return render(request, "partials/list.html", context)


def list_positions(request):
    objs = Position.objects.all()
    context = {"objs": objs}
    return render(request, "partials/list.html", context)


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
def dh_matrix_api(request):
    if request.method == "POST":
        data = json.loads(request.POST["data"])
        joint_angles = data.get("joint_angles", [])
        j = forward_kinematics(joint_angles)
        return JsonResponse({"matrix": j.tolist()})


@csrf_exempt
def get_matrix_path(request):
    print(request.POST)
    if request.method == "POST":
        data = json.loads(request.POST["data"])
        joint_angles = data.get("joint_angles", [])
        target_pos_id = data.get("target_pos_id", None)

        pos_obj = Position.objects.get(id=target_pos_id)

        target_pos_angles = [
            pos_obj.angle0,
            pos_obj.angle1,
            pos_obj.angle2,
            pos_obj.angle3,
            pos_obj.angle4,
            pos_obj.angle5,
        ]

        path_matrix = get_interpolated_matrix_data(
            joint_angles, target_pos_angles
        )
        return JsonResponse({"path": path_matrix})
    return JsonResponse({})
