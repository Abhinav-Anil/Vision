"""Simple video capture/merge demo.

This script records a short blended video using the first captured
frames as a static background. It is a minimal demo and expects a
webcam available on device index 0.
"""

import time
import cv2
import numpy as np


def main() -> None:
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    output = cv2.VideoWriter("ABHINAV.mp4", fourcc, 20.0, (640, 480))

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Unable to access the camera.")
        return

    # give camera time to warm up
    time.sleep(1)

    # capture a few frames to use as background
    background = None
    for _ in range(10):
        ret, background = cap.read()
        if not ret:
            break

    t0 = time.time()
    while cap.isOpened():
        ret, foreground = cap.read()
        if not ret:
            break

        # combine frames (simple add/blend)
        full = cv2.add(foreground, background)

        output.write(full)
        cv2.imshow("ABHINAV", full)

        if cv2.waitKey(1) & 0xFF == ord("a"):
            break

        if time.time() - t0 > 10:
            break

    cap.release()
    output.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
