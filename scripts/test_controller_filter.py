#!/usr/bin/env python3
import os
import argparse
import numpy as np
import matplotlib.pyplot as plt

from controller import Controller


def run_filter_response(controller, labels, dt):
    angles = []
    targets = []
    lefts = []
    rights = []
    times = []
    t = 0.0
    for label in labels:
        left, right = controller(label)
        angle = controller.angle
        target = controller._angle_from_label(label)
        angles.append(angle)
        targets.append(target)
        lefts.append(left)
        rights.append(right)
        times.append(t)
        t += dt
    return (
        np.array(times),
        np.array(targets),
        np.array(angles),
        np.array(lefts),
        np.array(rights),
    )


def main():
    parser = argparse.ArgumentParser(description="Controller filter response test")
    parser.add_argument("--steps", type=int, default=120, help="Number of samples")
    parser.add_argument("--dt", type=float, default=0.1, help="Sample time (s)")
    parser.add_argument("--step_at", type=int, default=20, help="Step index")
    parser.add_argument("--from_label", type=int, default=2, help="Initial label")
    parser.add_argument("--to_label", type=int, default=4, help="Step label")
    parser.add_argument("--amplitude", type=float, default=1.0, help="Target amplitude")
    parser.add_argument("--freq_hz", type=float, default=0.5, help="Sinusoid frequency (Hz)")
    parser.add_argument("--tau", type=float, default=2.0, help="Exponential time constant (s)")
    parser.add_argument("--log_scale", type=float, default=3.0, help="Scale for -log(t) target")
    parser.add_argument("--smoothing", type=float, default=0.2, help="Angle smoothing")
    parser.add_argument("--out", type=str, default="controller_filter_response.png", help="Output plot")
    args = parser.parse_args()

    base_map = Controller().label_to_angle
    from_angle = base_map.get(args.from_label, 0.0)
    to_angle = base_map.get(args.to_label, 0.0)

    step_targets = [from_angle] * args.step_at + [to_angle] * (args.steps - args.step_at)

    sin_times = np.arange(args.steps) * args.dt
    sin_targets = list(args.amplitude * np.sin(2.0 * np.pi * args.freq_hz * sin_times))

    exp_times = np.arange(args.steps) * args.dt
    exp_targets = list(args.amplitude * np.exp(-exp_times / args.tau))

    log_times = (np.arange(args.steps) + 1) * args.dt
    log_targets = list(-np.log(log_times) * args.log_scale)

    target_angles = step_targets + sin_targets + exp_targets + log_targets

    label_to_angle = {i: float(target_angles[i]) for i in range(len(target_angles))}
    controller = Controller(angle_smoothing=args.smoothing, label_to_angle=label_to_angle)
    labels = list(range(len(target_angles)))
    times, targets, angles, lefts, rights = run_filter_response(controller, labels, args.dt)

    fig, axes = plt.subplots(3, 1, figsize=(9, 7), sharex=True)
    axes[0].plot(times, targets, label="target angle")
    axes[0].plot(times, angles, label="filtered angle")
    axes[0].axhline(controller.max_angle_abs, color="k", linestyle="--", alpha=0.4, label="+angle limit")
    axes[0].axhline(-controller.max_angle_abs, color="k", linestyle="--", alpha=0.4, label="-angle limit")
    axes[0].set_ylabel("angle")
    axes[0].set_title("Controller filter response (step + sinusoid + exp + -log(t))")
    axes[0].grid(True, alpha=0.3)
    axes[0].legend()

    axes[1].plot(times, lefts, label="left wheel")
    axes[1].axhline(controller.max_wheel_speed, color="k", linestyle="--", alpha=0.4, label="+speed limit")
    axes[1].axhline(-controller.max_wheel_speed, color="k", linestyle="--", alpha=0.4, label="-speed limit")
    axes[1].set_ylabel("left speed")
    axes[1].grid(True, alpha=0.3)
    axes[1].legend()

    axes[2].plot(times, rights, label="right wheel")
    axes[2].axhline(controller.max_wheel_speed, color="k", linestyle="--", alpha=0.4, label="+speed limit")
    axes[2].axhline(-controller.max_wheel_speed, color="k", linestyle="--", alpha=0.4, label="-speed limit")
    axes[2].set_ylabel("right speed")
    axes[2].set_xlabel("time (s)")
    axes[2].grid(True, alpha=0.3)
    axes[2].legend()

    out_path = os.path.abspath(args.out)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    print(f"Saved plot: {out_path}")


if __name__ == "__main__":
    main()
