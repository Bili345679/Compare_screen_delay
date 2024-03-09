# Screen Delay Comparison

This program creates a maximized window on each screen, displaying the time obtained from `time.perf_counter()`, along with a time progress bar based on that time. In the progress bar, `#` represents the milliseconds that have passed in that second, while `.` represents the remaining milliseconds.

## Testing Method

To compare screen delays, you'll need to use a camera with a shutter speed faster than 1/1000. Simultaneously capture all screens using this camera. Some smartphones allow you to adjust the shutter speed in the camera app's professional mode. Set the shutter speed to 1/1000 and take the photos.

## Progress Bar Settings

Since the progress bar may affect the display time and cause inaccuracies in screen delay measurements, you can disable it by adjusting the settings. Similarly, you can modify the time size and progress bar size to fit your window dimensions.

## Configuration

To customize the program, create a `config.json` file in the same directory as the program. Configure it as follows:

```json
{
  "time_size": 200,
  "progress_size": 15,
  "show_progress": true
}
```
time_size: Time display size (default: 200).\<br>
progress_size: Progress bar size (default: 15).\<br>
show_progress: Display progress bar (default: true). Set to false if you don’t want to show the progress bar.\<br>
