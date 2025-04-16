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
from .models import Position


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
