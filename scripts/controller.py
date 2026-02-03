#!/usr/bin/env python3
from steer_labels import LABEL_TO_ANGLE
from steer_limits import MAX_ANGLE_ABS, MAX_WHEEL_SPEED, clamp_angle, clamp_wheel_speeds
class Controller:
    def __init__(
        self,
        base_speed=20,
        turn_gain=20,
        angle_smoothing=0.2,
        max_angle_abs=MAX_ANGLE_ABS,
        max_wheel_speed=MAX_WHEEL_SPEED,
        label_to_angle=None,
    ):
        self.base_speed = base_speed
        self.turn_gain = turn_gain
        self.angle_smoothing = angle_smoothing
        self.max_angle_abs = max_angle_abs
        self.max_wheel_speed = max_wheel_speed
        self.angle = 0.0
        self.stop = False
        if label_to_angle is None:
            self.label_to_angle = LABEL_TO_ANGLE
        else:
            self.label_to_angle = label_to_angle

    def stop(self):
        self.angle = 0.0
        self.stop = True

    def start(self):
        self.angle = 0.0
        self.stop = False

    def toggle_stop(self):
        if self.stop:
            self.start()
        else:
            self.stop()

    def _angle_from_label(self, label):
        if isinstance(label, (int, float)):
            return self.label_to_angle.get(int(label), 0.0)
        return self.label_to_angle.get(label, 0.0)

    def __call__(self, label, left_enc=None, right_enc=None):
        if self.stop:
            return 0, 0

        target_angle = self._angle_from_label(label)
        self.angle += self.angle_smoothing * (target_angle - self.angle)
        self.angle = clamp_angle(self.angle, self.max_angle_abs)
        base = self.base_speed
        steer = self.turn_gain * self.angle
        left = base + steer
        right = base - steer
        left, right = clamp_wheel_speeds(left, right, self.max_wheel_speed)
        left = int(left)
        right = int(right)
        return left, right