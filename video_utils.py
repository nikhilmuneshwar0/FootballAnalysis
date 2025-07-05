import cv2

# Reading the video frame by frame
def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    
    cap.release()  # Release the video capture object after reading
    return frames

# Saving the video
def save_video(output_video_frames, output_video_path):
    if not output_video_frames:
        print("No frames to save")
        return

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    frame_height, frame_width = output_video_frames[0].shape[:2]
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (frame_width, frame_height))

    for frame in output_video_frames:
        out.write(frame)

    out.release()
