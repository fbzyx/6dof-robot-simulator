from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.urls import reverse
from robot.models import Position
from robot.models import Robot


class PositionModelTest(TestCase):
    def setUp(self):
        self.valid_angles = {
            "angle0": 0,
            "angle1": 45,
            "angle2": -90,
            "angle3": 180,
            "angle4": -180,
            "angle5": 90,
        }

    def test_create_valid_position(self):
        position = Position.objects.create(**self.valid_angles)
        self.assertEqual(position.angle0, 0)
        self.assertEqual(position.angle3, 180)
        self.assertIsInstance(position, Position)

    def test_angle_out_of_bounds_positive(self):
        invalid_data = self.valid_angles.copy()
        invalid_data["angle2"] = 181  # > 180
        position = Position(**invalid_data)
        with self.assertRaises(ValidationError):
            position.full_clean()

    def test_angle_out_of_bounds_negative(self):
        invalid_data = self.valid_angles.copy()
        invalid_data["angle4"] = -181  # < -180
        position = Position(**invalid_data)
        with self.assertRaises(ValidationError):
            position.full_clean()

    def test_delete_obj_url(self):
        position = Position.objects.create(**self.valid_angles)
        expected_url = reverse(
            "robot:delete-position", kwargs={"id": position.id}
        )
        self.assertEqual(position.delete_obj(), expected_url)


class RobotModelTest(TestCase):
    def setUp(self):
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

    def test_create_valid_robot(self):
        robot = Robot.objects.create(**self.valid_data)
        self.assertEqual(robot.angle0, 0)
        self.assertEqual(robot.len4, 30)
        self.assertIsInstance(robot, Robot)

    def test_invalid_angle_too_large(self):
        data = self.valid_data.copy()
        data["angle2"] = 181
        robot = Robot(**data)
        with self.assertRaises(ValidationError):
            robot.full_clean()

    def test_invalid_angle_too_small(self):
        data = self.valid_data.copy()
        data["angle3"] = -181
        robot = Robot(**data)
        with self.assertRaises(ValidationError):
            robot.full_clean()

    def test_missing_length_field(self):
        data = self.valid_data.copy()
        del data["len5"]  # simulate missing field
        with self.assertRaises(IntegrityError):
            Robot.objects.create(**data)

    def test_angle_within_min_max_range(self):
        data = self.valid_data.copy()
        robot = Robot(**data)
        self.assertTrue(
            robot.angle0 >= robot.angle0_min
            and robot.angle0 <= robot.angle0_max
        )
