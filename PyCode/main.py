import cv2
import numpy as np
import face_recognition
import csv
from datetime import datetime

# Load known faces and their encodings
def load_known_faces():
    known_face_encodings = []
    known_face_names = []
    
    face_files = {
        "jobs": "/photos/jobs.jpg",
        "tesla": "photos/tesla.jpg"
    }
    
    for name, file in face_files.items():
        image = face_recognition.load_image_file(file)
        encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(encoding)
        known_face_names.append(name)
    
    return known_face_encodings, known_face_names

known_face_encodings, known_face_names = load_known_faces()
students = set(known_face_names)  # Use a set for faster membership testing

# Create a CSV file to store attendance data
attendance_file = 'attendance.csv'
with open(attendance_file, 'a+', newline='') as f:
    csv_writer = csv.writer(f)

    # Start video capture
    video_capture = cv2.VideoCapture(0)

    try:
        while True:
            # Capture a frame from the video stream
            ret, frame = video_capture.read()
            if not ret:
                print("Failed to capture frame. Exiting...")
                break

            # Resize frame to 1/4 size for faster processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Find all faces and face encodings in the current frame
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []

            for face_encoding in face_encodings:
                # See if the face is a match for the known faces
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

                # If a match was found, add the student's name and current time to the CSV file
                if name in known_face_names and name in students:
                    students.remove(name)
                    print(f"{name} marked as present.")
                    current_time = datetime.now().strftime("%H:%M:%S")
                    csv_writer.writerow([name, current_time])

            # Display the results on the screen
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a rectangle around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Display the resulting image
            cv2.imshow('Video', frame)

            # Exit the program if the 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        # Release the video capture and close all windows
        video_capture.release()
        cv2.destroyAllWindows()
