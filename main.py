import os
import pickle
from utils import read_video, save_video
from trackers import Tracker
import cv2
import numpy as np
from team_assigner import TeamAssigner
from player_ball_assigner import PlayerBallAssigner
from camera_movement_estimator import CameraMovementEstimator
from speed_and_distance_estimator import SpeedAndDistance_Estimator
from view_transformer.view_transformer import ViewTransformer


import os
from utils import read_video, save_video
import os
import pickle
import numpy as np
import cv2
from utils import read_video, save_video
from trackers import Tracker
from team_assigner import TeamAssigner
from player_ball_assigner import PlayerBallAssigner
from camera_movement_estimator import CameraMovementEstimator
from speed_and_distance_estimator import SpeedAndDistance_Estimator
from view_transformer.view_transformer import ViewTransformer


def main():
    try:
        # Read videos
        video_frames = read_video('input_videos/08fd33_4.mp4')

        if not video_frames:
            print("Error: Input video file is missing or could not be read.")
            return

        # Initialize tracker
        tracker = Tracker('models/best.pt')

        # Define stub file path
        stub_path = 'stubs/track_stubs.pkl'

        # Check if stub file exists, and use it if available
        if os.path.exists(stub_path):
            print("Loading tracks from stub...")
            tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path=stub_path)
        else:
            print("Performing fresh tracking...")
            tracks = tracker.get_object_tracks(video_frames)

            # Save tracks to the stub for future use
            print("Saving tracks to stub...")
            with open(stub_path, 'wb') as f:
                pickle.dump(tracks, f)

        # save cropped image of a player
        # for track_id,player in tracks['players'][0].items():
        #     bbox = player['bbox']
        #     frame = video_frames[0]

        #     #crop bbox from frame
        #     cropped_image = frame[int(bbox[1]):int(bbox[3]),int(bbox[0]):int(bbox[2])]

        #     #save cropped image
        #     cv2.imwrite(f"output_videos/cropped_image.jpg", cropped_image)
        #     break

        # Get object positions
        tracker.add_position_to_track(tracks)

        # Estimate camera movement
        camera_movement_estimator = CameraMovementEstimator(video_frames[0])
        camera_movement_per_frame = camera_movement_estimator.get_camera_movement(
            video_frames, read_from_stub=True, stub_path=stub_path
        )
        camera_movement_estimator.add_adjust_positions_to_tracks(tracks, camera_movement_per_frame)

        # View transformer
        view_transformer = ViewTransformer()
        view_transformer.add_transformed_position_to_tracks(tracks)

        # Interpolate ball positions
        tracks["ball"] = tracker.interpolate_ball_positions(tracks["ball"])

        # Speed and distance estimation
        speed_and_distance_estimator = SpeedAndDistance_Estimator()
        speed_and_distance_estimator.add_speed_and_distance_to_tracks(tracks)

        # Assign teams to players
        team_assigner = TeamAssigner()
        team_assigner.assign_team_color(video_frames[0], tracks['players'][0])

        for frame_num, player_track in enumerate(tracks['players']):
            for player_id, track in player_track.items():
                team = team_assigner.get_player_team(video_frames[frame_num], track['bbox'], player_id)
                tracks['players'][frame_num][player_id]['team'] = team
                tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]

        # Assign ball to player
        player_assigner = PlayerBallAssigner()
        team_ball_control = []

        for frame_num, player_tracks in enumerate(tracks['players']):
            ball_bbox = tracks['ball'][frame_num][1]['bbox']
            assigned_player = player_assigner.assign_ball_to_player(player_tracks, ball_bbox)

            if assigned_player != -1:
                tracks['players'][frame_num][assigned_player]['has_ball'] = True
                team_ball_control.append(tracks['players'][frame_num][assigned_player]['team'])
            else:
                if team_ball_control:
                    team_ball_control.append(team_ball_control[-1])
                else:
                    team_ball_control.append(-1)

        team_ball_control = np.array(team_ball_control)

        # Draw object tracks
        output_video_frames = tracker.draw_annotations(video_frames, tracks, team_ball_control)

        # Debug camera movement
        print(f"Camera movement per frame: {camera_movement_per_frame}")
        print(f"Number of frames in video: {len(output_video_frames)}")

        # Draw camera movement
        output_video_frames = camera_movement_estimator.draw_camera_movement(output_video_frames, camera_movement_per_frame)

        # Draw speed and distance
        speed_and_distance_estimator.draw_speed_and_distance(output_video_frames, tracks)

        # Ensure output directory exists
        os.makedirs('output_videos', exist_ok=True)

        # Save the processed video
        save_video(output_video_frames, 'output_videos/08fd33_4_output_video.avi')

        print("Finished processing video.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()



