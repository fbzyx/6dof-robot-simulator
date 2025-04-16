from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_htmx.http import trigger_client_event
from .forms import PositionForm, RobotForm
from .models import Position, Robot
from .utils.jacobi import forward_kinematics
import json


def main_view(request):
    objs = Position.objects.all()
    params = Robot.objects.all().first()
    context = {"form": PositionForm(), "form_params": RobotForm(instance=params), "objs": objs, "params":params}
    return render(request, "index.html", context=context)


def robot_parameters(request):
    if request.POST:
        form = RobotForm(data=request.POST)
        if form.is_valid():
            Robot.objects.all().delete()
            obj = form.save(commit=False)
            obj.save()

            return redirect("robot:main-view")

        objs = Position.objects.all()
        context = {"form": PositionForm(), "form_params": form, "objs": objs}

        return render(request, "index.html", context=context)



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
def jacobi_api(request):
    if request.method == "POST":
        data = json.loads(request.POST["data"])
        joint_angles = data.get("joint_angles", [])
        j = forward_kinematics(joint_angles)
        return JsonResponse({"matrix": j.tolist()})
