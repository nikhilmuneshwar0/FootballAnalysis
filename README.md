# ⚽ Football Analysis with Computer Vision

An AI-powered football video analysis system that uses YOLO object detection and computer vision techniques to track players, referees, and the ball, analyze team formations, calculate player speeds and distances, and provide comprehensive match insights.

## 🎯 Features

- **Object Detection & Tracking**: Automatically detects and tracks players, referees, and the football using YOLOv8
- **Team Assignment**: Identifies and assigns players to teams based on jersey colors using K-means clustering
- **Ball Possession Analysis**: Determines which player has control of the ball at any given moment
- **Camera Movement Compensation**: Accounts for camera panning and movement to provide accurate position tracking
- **Perspective Transformation**: Converts pixel coordinates to real-world field coordinates
- **Speed & Distance Metrics**: Calculates player speeds (km/h) and distances covered during the match
- **Ball Trajectory Interpolation**: Smooths ball tracking by interpolating positions when detection is lost
- **Visual Annotations**: Overlays tracking information, team colors, and statistics on output video

## 🏗️ Project Structure

```
FootballAnalysis/
├── main.py                              # Main execution script
├── tracker.py                           # YOLO-based object detection and tracking
├── team_assigner.py                     # Team identification using color clustering
├── player_ball_assigner.py              # Ball possession assignment logic
├── camera_movement_estimator.py         # Camera motion compensation
├── speed_and_distance_estimator.py      # Speed and distance calculations
├── view_transformer.py                  # Perspective transformation utilities
├── bbox_utils.py                        # Bounding box utility functions
├── video_utils.py                       # Video I/O operations
├── color_assignment.ipynb               # Color clustering experiments
├── football_training.ipynb              # Model training notebook
├── input_videos/                        # Input video directory
├── output_videos/                       # Processed video output
├── models/                              # Trained YOLO models (best.pt)
└── stubs/                               # Cached tracking data
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- CUDA-compatible GPU (recommended for faster processing)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/nikhilmuneshwar0/FootballAnalysis.git
cd FootballAnalysis
```

2. Install required dependencies:
```bash
pip install ultralytics opencv-python numpy pandas supervision
```

### Dependencies

The project relies on the following key libraries:

- **ultralytics**: YOLOv11 implementation for object detection
- **supervision**: Object tracking utilities (ByteTrack)
- **opencv-python (cv2)**: Video processing and computer vision operations
- **numpy**: Numerical computations
- **pandas**: Data manipulation and interpolation
- **pickle**: Caching tracking results

### Usage

1. Place your football match video in the `input_videos/` directory

2. Update the video path in `main.py`:
```python
video_frames = read_video('input_videos/your_video.mp4')
```

3. Ensure you have a trained YOLO model at `models/best.pt`

4. Run the analysis:
```bash
python main.py
```

The processed video with annotations will be saved to `output_videos/`

### Performance Optimization

The system uses caching to speed up repeated runs:
- Object tracking results are cached in `stubs/track_stubs.pkl`
- Camera movement data is also cached
- Delete stub files to force fresh processing

## 🧠 How It Works

### 1. Object Detection & Tracking
The system uses a fine-tuned YOLOv8 model to detect:
- Players (including goalkeepers)
- Referees
- Football

ByteTrack algorithm maintains consistent IDs across frames.

### 2. Team Assignment
- Extracts player jersey colors from bounding boxes
- Uses K-means clustering (k=2) to identify two dominant team colors
- Assigns each player to a team based on color similarity

### 3. Camera Movement Compensation
- Tracks feature points across frames using optical flow
- Calculates camera translation and adjusts player positions
- Ensures accurate distance and speed measurements

### 4. Position Transformation
- Converts pixel coordinates to real-world field positions
- Uses perspective transformation based on field markings
- Enables accurate distance calculations in meters

### 5. Speed & Distance Calculation
- Tracks player movement across frames
- Adjusts for camera motion
- Calculates instantaneous speed (km/h) and cumulative distance

### 6. Ball Possession
- Calculates distance between ball and all players
- Assigns possession to the nearest player within a threshold
- Tracks possession statistics per player

## 📊 Output

The system generates an annotated video showing:
- Bounding boxes around all detected objects
- Player IDs with team color indicators
- Current ball possessor highlighted
- Real-time speed and distance statistics
- Ball trajectory

## 🎓 Training Custom Models

The repository includes `football_training.ipynb` for training custom YOLO models on football-specific datasets. This allows you to:
- Fine-tune detection for specific match conditions
- Improve goalkeeper recognition
- Optimize for different camera angles

## 🐛 Known Issues

- Ball detection can be inconsistent in crowded scenes (addressed via interpolation)
- Team assignment may struggle with similar jersey colors
- Requires consistent lighting conditions for best results

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Nikhil Muneshwar**
- GitHub: [@nikhilmuneshwar0](https://github.com/nikhilmuneshwar0)

## 🙏 Acknowledgments

- Ultralytics for YOLOv11
- Supervision library for tracking utilities
- ByteTrack tracking algorithm

---

⭐ If you find this project useful, please consider giving it a star!
```
