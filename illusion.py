"""Simple motion-detection demo (original by Abhinav Anil).

This script captures frames from the default camera and detects
motion by comparing each frame to a static background. Detected
movement intervals are saved to `Time_of_movements.csv`.
"""

import cv2
from datetime import datetime
import pandas as pd


def main() -> None:
    static_back = None
    motion_list = [None, None]
    times = []
    df = pd.DataFrame(columns=["Start", "End"])

    video = cv2.VideoCapture(0)
    if not video.isOpened():
        print("Unable to access the camera.")
        return

    while True:
        ok, frame = video.read()
        if not ok:
            break

        motion = 0
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if static_back is None:
            static_back = gray
            continue

        diff_frame = cv2.absdiff(static_back, gray)
        thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
        thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

        cnts, _ = cv2.findContours(
            thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        for contour in cnts:
            if cv2.contourArea(contour) < 10000:
                continue
            motion = 1
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        motion_list.append(motion)
        motion_list = motion_list[-2:]

        if motion_list[-1] == 1 and motion_list[-2] == 0:
            times.append(datetime.now())
        if motion_list[-1] == 0 and motion_list[-2] == 1:
            times.append(datetime.now())

        cv2.imshow("Difference Frame", diff_frame)
        cv2.imshow("Color Frame", frame)

        key = cv2.waitKey(1)
        if key == ord("q"):
            if motion == 1:
                times.append(datetime.now())
            break

    for i in range(0, len(times), 2):
        df = df.append({"Start": times[i], "End": times[i + 1]}, ignore_index=True)

    df.to_csv("Time_of_movements.csv", index=False)
    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
