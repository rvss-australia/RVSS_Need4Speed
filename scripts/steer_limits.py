MAX_ANGLE_ABS = 0.5
MAX_WHEEL_SPEED = 20


def clamp_angle(angle, max_angle_abs=MAX_ANGLE_ABS):
    if angle < -max_angle_abs:
        return -max_angle_abs
    if angle > max_angle_abs:
        return max_angle_abs
    return angle


def clamp_wheel_speeds(left, right, max_wheel_speed=MAX_WHEEL_SPEED):
    peak = max(abs(left), abs(right))
    if peak > max_wheel_speed:
        scale = max_wheel_speed / peak
        left *= scale
        right *= scale
    return left, right
