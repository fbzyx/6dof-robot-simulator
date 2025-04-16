from django.urls import path
from .views import (
    main_view,
    main_view2,
    main_view3,
    main_view4,
    move_func,
    get_matrix,
    jacobi_api,
    create_position,
    delete_position,
    list_positions,
    robot_parameters,
)

app_name = "robot"

urlpatterns = [
    # SERVICES
    path("", main_view, name="main-view"),
    path("list-positions/", list_positions, name="list-positions"),
    path("create-position/", create_position, name="create-position"),
    path("robot-parameters/", robot_parameters, name="robot-parameters"),
    path("delete-position/<int:id>/", delete_position, name="delete-position"),
    # test
    path("test2/", main_view2, name="main-view2"),
    path("test3/", main_view3, name="main-view3"),
    path("test4/", main_view4, name="main-view4"),
    path("api/move/", move_func, name="move"),
    path("api/matrix/", get_matrix, name="matrix"),
    path("api/jacobian/", jacobi_api, name="jacobi_api"),
]
