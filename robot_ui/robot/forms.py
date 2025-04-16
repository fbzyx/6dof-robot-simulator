from django.core.exceptions import ValidationError
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
        # min_value=-180,
        # max_value=180,
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

        params = Robot.objects.all().first()
        # self.fields["angle0"].widget["attrs"]["min_value"] = params.angle0_min
        self.fields["angle0"].widget.attrs["value"] = params.angle0
        self.fields["angle0"].widget.attrs["min"] = params.angle0_min
        self.fields["angle0"].widget.attrs["max"] = params.angle0_max
        self.fields["angle1"].widget.attrs["value"] = params.angle1
        self.fields["angle1"].widget.attrs["min"] = params.angle1_min
        self.fields["angle1"].widget.attrs["max"] = params.angle1_max
        self.fields["angle2"].widget.attrs["value"] = params.angle2
        self.fields["angle2"].widget.attrs["min"] = params.angle2_min
        self.fields["angle2"].widget.attrs["max"] = params.angle2_max
        self.fields["angle3"].widget.attrs["value"] = params.angle3
        self.fields["angle3"].widget.attrs["min"] = params.angle3_min
        self.fields["angle3"].widget.attrs["max"] = params.angle3_max
        self.fields["angle4"].widget.attrs["value"] = params.angle4
        self.fields["angle4"].widget.attrs["min"] = params.angle4_min
        self.fields["angle4"].widget.attrs["max"] = params.angle4_max
        self.fields["angle5"].widget.attrs["value"] = params.angle5
        self.fields["angle5"].widget.attrs["min"] = params.angle5_min
        self.fields["angle5"].widget.attrs["max"] = params.angle5_max

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
            "hx-swap": "outerHTML",
            "hx-trigger": "submit",
            "hx-post": "robot-parameters/",
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

    def clean(self):
        super().clean()
        angle0 = self.cleaned_data.get("angle0")
        angle0_min = self.cleaned_data.get("angle0_min")
        angle0_max = self.cleaned_data.get("angle0_max")

        if not angle0_min <= angle0 <= angle0_max:
            raise ValidationError("Values out of range (Angle0)")

        angle1 = self.cleaned_data.get("angle1")
        angle1_min = self.cleaned_data.get("angle1_min")
        angle1_max = self.cleaned_data.get("angle1_max")

        if not angle1_min <= angle1 <= angle1_max:
            raise ValidationError("Values out of range (Angle1)")

        angle2 = self.cleaned_data.get("angle2")
        angle2_min = self.cleaned_data.get("angle2_min")
        angle2_max = self.cleaned_data.get("angle2_max")

        if not angle2_min <= angle2 <= angle2_max:
            raise ValidationError("Values out of range (Angle2)")

        angle3 = self.cleaned_data.get("angle3")
        angle3_min = self.cleaned_data.get("angle3_min")
        angle3_max = self.cleaned_data.get("angle3_max")

        if not angle3_min <= angle3 <= angle3_max:
            raise ValidationError("Values out of range (Angle3)")

        angle4 = self.cleaned_data.get("angle4")
        angle4_min = self.cleaned_data.get("angle0_min")
        angle4_max = self.cleaned_data.get("angle0_max")

        if not angle4_min <= angle4 <= angle4_max:
            raise ValidationError("Values out of range (Angle4)")
        angle5 = self.cleaned_data.get("angle5")
        angle5_min = self.cleaned_data.get("angle5_min")
        angle5_max = self.cleaned_data.get("angle5_max")

        if not angle5_min <= angle5 <= angle5_max:
            raise ValidationError("Values out of range (Angle5)")
