"""Bounding-box demo with a simple Bokeh timeline export.

This script detects motion and draws bounding boxes around moving
objects. It also exports a small CSV of motion intervals and a
simple Bokeh HTML timeline.
"""

import datetime
import cv2
import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource


def main() -> None:
    first_frame = None
    status_list = [None, None]
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

        status = 0
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if first_frame is None:
            first_frame = gray
            continue

        delta_frame = cv2.absdiff(first_frame, gray)
        th_delta = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
        th_delta = cv2.dilate(th_delta, None, iterations=0)
        cnts, _ = cv2.findContours(
            th_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        for contour in cnts:
            if cv2.contourArea(contour) < 10000:
                continue
            status = 1
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        status_list.append(status)
        status_list = status_list[-2:]
        if status_list[-1] == 1 and status_list[-2] == 0:
            times.append(datetime.datetime.now())
        if status_list[-1] == 0 and status_list[-2] == 1:
            times.append(datetime.datetime.now())

        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    for i in range(0, len(times), 2):
        df = df.append({"Start": times[i], "End": times[i + 1]}, ignore_index=True)

    ts = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    csv_name = f"Times_{ts}.csv"
    df.to_csv(csv_name, index=False)
    video.release()
    cv2.destroyAllWindows()

    # Code to Generate Graph using Bokeh
    df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
    df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

    cds = ColumnDataSource(df)

    p = figure(x_axis_type="datetime", height=100, width=500, title="Motion Graph")
    p.yaxis.minor_tick_line_color = None
    p.ygrid[0].ticker.desired_num_ticks = 1

    hover = HoverTool(tooltips=[("Start", "@Start_string"), ("End", "@End_string")])
    p.add_tools(hover)

    p.quad(left="Start", right="End", bottom=0, top=1, color="red", source=cds)
    output_file(f"Graph_{ts}.html")
    show(p)


if __name__ == "__main__":
    main()
