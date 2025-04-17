from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django_htmx.http import (
    trigger_client_event,
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

    return HttpResponse(status=200)


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

    return HttpResponse(status=200)


def delete_position(request, id):
    obj = get_object_or_404(Position, id=id)
    obj.delete()
    objs = Position.objects.all()
    context = {"objs": objs}
    return render(request, "partials/list.html", context)


def list_positions(request):
    objs = Position.objects.all()
    context = {"objs": objs}
    return render(request, "partials/list.html", context)


def robot_model(request):
    return render(request, "robot-model.html")


@csrf_exempt
def dh_matrix_api(request):
    if request.method == "POST":
        params = Robot.objects.all().first()
        robot_params_a = [
            params.a0,
            params.a1,
            params.a2,
            params.a3,
            params.a4,
            params.a5,
        ]
        robot_params_d = [
            params.len0,
            params.len1,
            params.len2,
            params.len3,
            params.len4,
            params.len5,
        ]
        data = json.loads(request.POST["data"])
        joint_angles = data.get("joint_angles", [])
        j = forward_kinematics(joint_angles, robot_params_a, robot_params_d)
        return JsonResponse({"matrix": j.tolist()})
    return JsonResponse({})


@csrf_exempt
def get_matrix_path(request):
    if request.method == "POST":
        data = json.loads(request.POST["data"])
        joint_angles = data.get("joint_angles", [])
        target_pos_id = data.get("target_pos_id", None)

        pos_obj = Position.objects.get(id=target_pos_id)
        params = Robot.objects.all().first()

        target_pos_angles = [
            pos_obj.angle0,
            pos_obj.angle1,
            pos_obj.angle2,
            pos_obj.angle3,
            pos_obj.angle4,
            pos_obj.angle5,
        ]

        robot_params_a = [
            params.a0,
            params.a1,
            params.a2,
            params.a3,
            params.a4,
            params.a5,
        ]
        robot_params_d = [
            params.len0,
            params.len1,
            params.len2,
            params.len3,
            params.len4,
            params.len5,
        ]

        path_matrix = get_interpolated_matrix_data(
            joint_angles, target_pos_angles, robot_params_a, robot_params_d
        )
        return JsonResponse({"path": path_matrix})
    return JsonResponse({})
