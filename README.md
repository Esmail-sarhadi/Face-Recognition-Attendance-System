
# Face Recognition Attendance System

This project implements a face recognition-based attendance system using a webcam to capture and recognize faces in real-time. The system compares the captured faces with known faces and logs the attendance details (name and timestamp) into a CSV file. It leverages the `face_recognition` library for face detection and recognition and uses OpenCV for video processing.

## Features

- **Real-time Face Detection and Recognition**: Captures video frames from a webcam and identifies faces in real-time.
- **Attendance Logging**: Logs the attendance details (name and timestamp) into a CSV file.
- **Customizable Known Faces**: Easily add and manage known faces for recognition.
- **Visual Feedback**: Displays a rectangle and name label around recognized faces in the video feed.

## Requirements

- Python 3.6+
- OpenCV
- face_recognition
- numpy

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/face-recognition-attendance.git
   cd face-recognition-attendance
   ```

2. **Install the Required Packages**
   ```bash
   pip install opencv-python face_recognition numpy
   ```

3. **Prepare Known Face Images**
   - Place your known face images in the `photos` directory.
   - Ensure the images are named appropriately (e.g., `jobs.jpg`, `leyla.jpg`, `tesla.jpg`).

## Configuration

1. **Update the Face Files Dictionary**
   - Edit the `main.py` file and update the `face_files` dictionary with the paths to your known face images.

   ```python
   face_files = {
       "jobs": "/media/charon/ESMAIL/OLD BOY/D/face_leyla/photos/jobs.jpg",
       "tesla": "/media/charon/ESMAIL/OLD BOY/D/face_leyla/photos/tesla.jpg"
   }
   ```

## Usage

1. **Run the Script**
   ```bash
   python3 main.py
   ```

2. **System Operation**
   - The webcam will start, and the system will begin recognizing faces.
   - Attendance details (name and timestamp) will be logged in `attendance.csv`.
   - Recognized faces will be marked with a rectangle and name label in the video feed.

3. **Exit the Program**
   - Press the 'q' key to exit the video feed and stop the program.

## Project Structure

- `main.py`: The main script for the face recognition attendance system.
- `photos/`: Directory containing known face images.
- `attendance.csv`: CSV file where attendance details are logged.
- `README.md`: This README file.

## Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, please fork the repository and submit a pull request. Ensure your changes are well-documented and tested.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

<h2 id="donation">Donation</h2>

<p>If you find this project helpful, consider making a donation:</p>
<p><a href="https://nowpayments.io/donation?api_key=REWCYVC-A1AMFK3-QNRS663-PKJSBD2&source=lk_donation&medium=referral" target="_blank">
     <img src="https://nowpayments.io/images/embeds/donation-button-black.svg" alt="Crypto donation button by NOWPayments">
</a></p>
