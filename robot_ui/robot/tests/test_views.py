from django.urls import reverse
from django.test import TestCase, Client
from robot.models import Robot, Position
from robot.forms import PositionForm, RobotForm
from django_htmx.http import HttpResponseClientRefresh


class MainViewTest(TestCase):
    def setUp(self):
        self.robot = Robot.objects.create(
            angle0= 0,
            angle0_min= -90,
            angle0_max= 90,
            len0= 10,
            a0= 10,
            angle1= 45,
            angle1_min= -90,
            angle1_max= 90,
            len1= 15,
            a1= 10,
            angle2= -45,
            angle2_min= -90,
            angle2_max= 90,
            len2= 20,
            a2= 10,
            angle3= 90,
            angle3_min= 0,
            angle3_max= 180,
            len3= 25,
            a3= 10,
            angle4= -90,
            angle4_min= -180,
            angle4_max= 0,
            len4= 30,
            a4= 10,
            angle5= 10,
            angle5_min= -30,
            angle5_max= 30,
            len5= 5,
            a5= 10,
        )

        self.position = Position.objects.create(
            angle0=10, angle1=20, angle2=30, angle3=40, angle4=50, angle5=60
        )

    def test_main_view_status_code(self):
        response = self.client.get(reverse("robot:main-view"))
        self.assertEqual(response.status_code, 200)

    def test_main_view_template_used(self):
        response = self.client.get(reverse("robot:main-view"))
        self.assertTemplateUsed(response, "index.html")

    def test_main_view_context_data(self):
        response = self.client.get(reverse("robot:main-view"))

        self.assertIsInstance(response.context["form"], PositionForm)
        self.assertIsInstance(response.context["form_params"], RobotForm)
        self.assertEqual(
            list(response.context["objs"]), list(Position.objects.all())
        )
        self.assertEqual(response.context["params"], Robot.objects.first())


class RobotParametersViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("robot:robot-parameters")

        self.valid_data = {
            "angle0": 0,
            "angle0_min": -90,
            "angle0_max": 90,
            "len0": 10,
            "a0": 10,
            "angle1": 45,
            "angle1_min": -90,
            "angle1_max": 90,
            "len1": 15,
            "a1": 10,
            "angle2": -45,
            "angle2_min": -90,
            "angle2_max": 90,
            "len2": 20,
            "a2": 10,
            "angle3": 90,
            "angle3_min": 0,
            "angle3_max": 180,
            "len3": 25,
            "a3": 10,
            "angle4": -90,
            "angle4_min": -180,
            "angle4_max": 0,
            "len4": 30,
            "a4": 10,
            "angle5": 10,
            "angle5_min": -30,
            "angle5_max": 30,
            "len5": 5,
            "a5": 10,
        }

    def test_valid_htmx_post(self):
        # create dummy Robot object to test deletion
        Robot.objects.create(**self.valid_data)
        self.assertEqual(Robot.objects.count(), 1)

        response = self.client.post(
            self.url, self.valid_data, HTTP_HX_REQUEST="true"
        )

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, HttpResponseClientRefresh)
        self.assertEqual(Robot.objects.count(), 1)  # Old deleted, one added

    def test_invalid_htmx_post(self):
        invalid_data = self.valid_data.copy()
        invalid_data["angle0"] = 181  # Invalid (>180)

        response = self.client.post(
            self.url, invalid_data, HTTP_HX_REQUEST="true"
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "partials/form_params.html")
        form = response.context["form_params"]
        self.assertFalse(form.is_valid())
        self.assertIn("angle0", form.errors)

    def test_non_htmx_post_ignored(self):
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(response.status_code, 200)


class CreatePositionViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("robot:create-position")

        self.valid_data = {
            "angle0": 0,
            "angle1": 10,
            "angle2": -20,
            "angle3": 30,
            "angle4": -40,
            "angle5": 50,
        }

    def test_valid_htmx_post_creates_position(self):
        response = self.client.post(
            self.url, self.valid_data, HTTP_HX_REQUEST="true"
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "partials/form.html")
        self.assertTrue(Position.objects.exists())

        # Optional: check client event
        self.assertIn("hx-trigger", response.content.decode())

    def test_invalid_htmx_post_does_not_create_position(self):
        invalid_data = self.valid_data.copy()
        invalid_data["angle1"] = 200  # Invalid: over 180

        response = self.client.post(
            self.url, invalid_data, HTTP_HX_REQUEST="true"
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "partials/form.html")
        self.assertFalse(Position.objects.exists())

        # Form errors should be in the response content
        self.assertIn("angle1", response.content.decode())

    def test_non_htmx_request_returns_200_no_action(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"")


class DeletePositionViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.position = Position.objects.create(
            angle0=10, angle1=20, angle2=30, angle3=40, angle4=50, angle5=60
        )
        self.url = reverse(
            "robot:delete-position", kwargs={"id": self.position.id}
        )

    def test_delete_valid_position(self):
        self.assertEqual(Position.objects.count(), 1)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "partials/list.html")
        self.assertEqual(Position.objects.count(), 0)

        # Ensure context contains empty list
        self.assertQuerySetEqual(response.context["objs"], [])

    def test_delete_invalid_position(self):
        invalid_url = reverse("robot:delete-position", kwargs={"id": 9999})

        response = self.client.get(invalid_url)
        self.assertEqual(
            response.status_code, 404
        )  # Default behavior unless caught
