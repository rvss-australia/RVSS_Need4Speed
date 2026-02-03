LABELS = [
    "sharp left",
    "left",
    "straight",
    "right",
    "sharp right",
]

LABEL_TO_ANGLE = {
    0: -1.0,
    1: -0.5,
    2: 0.0,
    3: 0.5,
    4: 1.0,
}


def steering_to_class(steering):
    if steering <= -0.5:
        return 0
    if steering < 0:
        return 1
    if steering == 0:
        return 2
    if steering < 0.5:
        return 3
    return 4
