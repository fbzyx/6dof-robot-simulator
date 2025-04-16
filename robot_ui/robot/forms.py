from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Row,
    Column,
    Div,
    Fieldset,
    Button,
    HTML,
    Submit,
)

from django import forms
from .models import Position, Robot


class PositionForm(forms.ModelForm):
    angle0 = forms.IntegerField(
        min_value=-180,
        max_value=180,
        widget=forms.NumberInput(
            attrs={
                "type": "range",
                "class": "form-range",
                "onchange": "update_matrix()",
                "id": "range0",
            }
        ),
    )

    angle1 = forms.IntegerField(
        min_value=-180,
        max_value=180,
        widget=forms.NumberInput(
            attrs={
                "type": "range",
                "class": "form-range",
                "onchange": "update_matrix()",
                "id": "range1",
            }
        ),
    )

    angle2 = forms.IntegerField(
        min_value=-180,
        max_value=180,
        widget=forms.NumberInput(
            attrs={
                "type": "range",
                "class": "form-range",
                "onchange": "update_matrix()",
                "id": "range2",
            }
        ),
    )

    angle3 = forms.IntegerField(
        min_value=-180,
        max_value=180,
        widget=forms.NumberInput(
            attrs={
                "type": "range",
                "class": "form-range",
                "onchange": "update_matrix()",
                "id": "range3",
            }
        ),
    )

    angle4 = forms.IntegerField(
        min_value=-180,
        max_value=180,
        widget=forms.NumberInput(
            attrs={
                "type": "range",
                "class": "form-range",
                "onchange": "update_matrix()",
                "id": "range4",
            }
        ),
    )

    angle5 = forms.IntegerField(
        min_value=-180,
        max_value=180,
        widget=forms.NumberInput(
            attrs={
                "type": "range",
                "class": "form-range",
                "onchange": "update_matrix()",
                "id": "range5",
            }
        ),
    )

    class Meta:
        model = Position
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.attrs = {
            "hx-swap": "outerHTML",
            "hx-trigger": "submit",
            "hx-post": "create-position/",
        }
        self.helper.layout = Layout(
            Row(
                Column("angle0", css_class="col-12"),
                Column("angle1", css_class="col-12"),
                Column("angle2", css_class="col-12"),
                Column("angle3", css_class="col-12"),
                Column("angle4", css_class="col-12"),
                Column("angle5", css_class="col-12"),
                css_class="form-row",
            ),
            Submit(
                "submit", "Save position", css_class="btn-success bg-gradient"
            ),
        )


class RobotForm(forms.ModelForm):
    class Meta:
        model = Robot
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.attrs = {
            "action": "robot-parameters/",
        }
        self.helper.layout = Layout(
            Row(
                Column("angle0", css_class="col-md-3"),
                Column("angle0_min", css_class="col-md-3"),
                Column("angle0_max", css_class="col-md-3"),
                Column("len0", css_class="col-md-3"),
                css_class="form-row",
            ),
            Row(
                Column("angle1", css_class="col-md-3"),
                Column("angle1_min", css_class="col-md-3"),
                Column("angle1_max", css_class="col-md-3"),
                Column("len1", css_class="col-md-3"),
                css_class="form-row",
            ),
            Row(
                Column("angle2", css_class="col-md-3"),
                Column("angle2_min", css_class="col-md-3"),
                Column("angle2_max", css_class="col-md-3"),
                Column("len2", css_class="col-md-3"),
                css_class="form-row",
            ),
            Row(
                Column("angle3", css_class="col-md-3"),
                Column("angle3_min", css_class="col-md-3"),
                Column("angle3_max", css_class="col-md-3"),
                Column("len3", css_class="col-md-3"),
                css_class="form-row",
            ),
            Row(
                Column("angle4", css_class="col-md-3"),
                Column("angle4_min", css_class="col-md-3"),
                Column("angle4_max", css_class="col-md-3"),
                Column("len4", css_class="col-md-3"),
                css_class="form-row",
            ),
            Row(
                Column("angle5", css_class="col-md-3"),
                Column("angle5_min", css_class="col-md-3"),
                Column("angle5_max", css_class="col-md-3"),
                Column("len5", css_class="col-md-3"),
                css_class="form-row",
            ),
            Submit(
                "submit", "Save parameters", css_class="btn-success bg-gradient"
            ),
        )
