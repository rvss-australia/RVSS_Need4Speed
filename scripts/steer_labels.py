LABELS = [
    "sharpleft",
    "left",
    "straight",
    "right",
    "sharpright",
]

LABEL_TO_ANGLE = {
    0: -0.5,
    1: -0.2,
    2: 0.0,
    3: 0.2,
    4: 0.5,
}


def steering_to_class(steering):
    if steering <= -0.2:
        return 0
    if steering < 0:
        return 1
    if steering == 0:
        return 2
    if steering < 0.2:
        return 3
    return 4
