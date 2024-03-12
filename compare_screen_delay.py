import tkinter as tk
from screeninfo import get_monitors
import os, json, time


class ScreenWindow(tk.Tk):
    def __init__(
        self,
        screen,
        windows,
        show_ms_array=True,
        time_size=250,
        ms_array_size=20,
        refresh_interval=1,
    ):
        super(ScreenWindow, self).__init__()
        self.geometry(f"{100}x{50}+{screen.x}+{screen.y}")
        self.state("zoomed")

        self.show_ms_array = show_ms_array
        self.refresh_interval = refresh_interval

        self.time = tk.Label(self, font=("TkDefaultFont", time_size, "normal"))
        self.time.pack()
        self.ms_array = tk.Label(self, font=("TkDefaultFont", ms_array_size, "normal"))
        self.ms_array.pack()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.windows = windows

        self.update_time()

    def on_closing(self):
        for window in self.windows:
            window.destroy()

    def update_time(self):
        time_value = str(time.perf_counter())
        time_value = time_value[time_value.index(".") - 1 :].ljust(9)
        self.time.config(text=time_value)
        if self.show_ms_array:
            self.update_ms_array(time_value)
        self.after(self.refresh_interval, self.update_time)

    def update_ms_array(self, time_value):
        ms_count = int(time_value[2:5])
        result = []
        for i in range(20):
            row = [str(i + 1).rjust(5)]
            for j in range(5):
                if ms_count > 0:
                    row.append(
                        f"{j} {'■' * min(10, ms_count)}{'□' * max(0, 10 - ms_count)}"
                    )
                    ms_count -= 10
                else:
                    row.append(f"{j} {'□' * 10}")
            row.append(str(j + 1))
            result.append(" ".join(row))
        self.ms_array.config(text="\n".join(result))


def main():
    windows = []
    config = {}
    if os.path.exists("./config.json"):
        with open("./config.json", "r") as file:
            temp_config = json.load(file)
            for each_key in [
                "show_ms_array",
                "time_size",
                "ms_array_size",
                "refresh_interval",
            ]:
                if each_key in temp_config:
                    config[each_key] = temp_config[each_key]

    for screen in get_monitors():
        window = ScreenWindow(screen, windows, **config)
        windows.append(window)
    tk.mainloop()


if __name__ == "__main__":
    main()