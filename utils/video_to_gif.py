# A program to convert a video to a gif
# - specify the starting time of the gif
# - specify the duration of the gif
# - specify the playback speed of the gif
import argparse
import ffmpeg
import os


def convert_video_to_gif(input_video_path, output_gif_path, start_time=0, duration=5, playback_speed=1.0, scale_width=1080, fps=10):
    ffmpeg.input(input_video_path, ss=start_time, t=duration).filter("setpts", f"{playback_speed}*PTS").filter("scale", scale_width, -1).filter("fps", fps=fps).output(
        output_gif_path, format="gif"
    ).run(overwrite_output=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Video to GIF Converter")
    parser.add_argument("--input", default="newjeans.mp4", help="Input video file path")
    parser.add_argument("--output", default="newjeans.gif", help="Output GIF file path")
    parser.add_argument("--start-time", type=int, default=0, help="Starting time in seconds (default: 0)")
    parser.add_argument("--duration", type=int, default=5, help="Duration in seconds (default: 5)")
    parser.add_argument("--playback-speed", type=float, default=1.0, help="Playback speed (default: 1.0)")
    parser.add_argument("--scale-width", type=int, default=1080, help="Width of the output GIF (default: 720)")
    parser.add_argument("--fps", type=int, default=10, help="Frames per second for the output GIF (default: 10)")

    args = parser.parse_args()

    input_video_path = args.input
    output_gif_path = args.output
    start_time = args.start_time
    duration = args.duration
    playback_speed = args.playback_speed
    scale_width = args.scale_width
    fps = args.fps

    convert_video_to_gif(input_video_path, output_gif_path, start_time, duration, playback_speed, scale_width, fps)
