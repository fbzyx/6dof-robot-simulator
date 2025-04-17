from django.urls import path
from .views import (
    main_view,
    dh_matrix_api,
    create_position,
    delete_position,
    list_positions,
    robot_parameters,
    get_matrix_path,
    robot_model,
)

app_name = "robot"

urlpatterns = [
    # SERVICES
    path("", main_view, name="main-view"),
    path("list-positions/", list_positions, name="list-positions"),
    path("create-position/", create_position, name="create-position"),
    path("robot-parameters/", robot_parameters, name="robot-parameters"),
    path("delete-position/<int:id>/", delete_position, name="delete-position"),
    path("api/dhmatrix/", dh_matrix_api, name="dh_matrix_api"),
    path("get-matrix-path/", get_matrix_path, name="get-matrix-path"),
    path("api/dhmatrix/", dh_matrix_api, name="dh_matrix_api"),
    # test
    path("robotmodel/", robot_model, name="robot-model"),

]
