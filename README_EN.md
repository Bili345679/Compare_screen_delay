# Screen Delay Comparison

HOW TO USE | [使用说明](https://github.com/Bili345679/Compare_screen_delay/blob/main/README.md)

This program creates a maximized window on each screen, displaying the time obtained from `time.perf_counter()`, along with a time progress bar based on that time. In the progress bar, `#` represents the milliseconds that have passed in that second, while `.` represents the remaining milliseconds.

## Testing Method

To compare screen delays, you'll need to use a camera with a shutter speed faster than 1/1000. Simultaneously capture all screens using this camera. Some smartphones allow you to adjust the shutter speed in the camera app's professional mode. Set the shutter speed to 1/1000 and take the photos.

## Progress Bar Settings

Since the progress bar may affect the display time and cause inaccuracies in screen delay measurements, you can disable it by adjusting the settings. Similarly, you can modify the time size and progress bar size to fit your window dimensions.

## Configuration

To customize the program, create a `config.json` file in the same directory as the program. Configure it as follows:

```json
{
  "show_ms_array": true,
  "time_size": 250,
  "ms_array_size": 20,
  "refresh_interval": 1
}
```
show_ms_array: Whether to display the progress bar, default is true. If you do not want to display the progress bar, please change it to false.<br>
time_size: Time character size, default is 250.<br>
ms_array_size: Millisecond array character size, default is 20.<br>
refresh_interval: Refresh interval between time characters and millisecond array characters, in milliseconds (ms), default value is 1.<br>