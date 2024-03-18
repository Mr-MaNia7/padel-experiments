from moviepy.video.io.VideoFileClip import VideoFileClip


def trim_video(input_video, output_video, start_time, end_time):
    """
    Trim a video from start_time to end_time and save the result to output_video.

    Args:
    input_video (str): Path to the input video file.
    output_video (str): Path to save the trimmed video file.
    start_time (float): Start time of the trimmed segment in seconds.
    end_time (float): End time of the trimmed segment in seconds.
    """
    # Load the video clip
    video_clip = VideoFileClip(input_video)

    # Trim the clip
    trimmed_clip = video_clip.subclip(start_time, end_time)

    # Write the trimmed clip to a new file
    trimmed_clip.write_videofile(
        output_video, codec="libx264", audio_codec="aac")

    # Close the video file
    video_clip.close()


if __name__ == "__main__":
    # input_video = "input_videos/sample-full-match.mp4"
    # for i in range(0, 4):
    #     output_video = "input_videos/sample-video" + str(i) + ".mp4"
    #     # 30 seconds each
    #     start_time = i * 30
    #     end_time = (i + 1) * 30
    #     trim_video(input_video, output_video, start_time, end_time)
    trim_video("input_videos/sample-full-match.mp4",
               "input_videos/shortest.mp4", 0, 5)
