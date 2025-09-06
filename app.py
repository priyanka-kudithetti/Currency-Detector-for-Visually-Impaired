import os
import cv2
import pyttsx3
import time
import numpy as np

# Set working directory to the folder where this script is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def speak(text):
    print("[Speaking]:", text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def capture_image():
    speak("Opening webcam. Please show the currency note in front of the camera.")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        speak("Failed to open webcam.")
        return False

    speak("Starting image capture in")
    time.sleep(0.5)
    speak("3")
    time.sleep(1)
    speak("2")
    time.sleep(1)
    speak("1")
    time.sleep(1)

    ret, frame = cap.read()
    if ret:
        cv2.imwrite("captured_note.jpg", frame)
        speak("Image captured successfully.")
        cv2.imshow("Captured Image", frame)
        cv2.waitKey(2000)
        cap.release()
        cv2.destroyAllWindows()
        return True
    else:
        speak("Failed to capture image.")
        cap.release()
        cv2.destroyAllWindows()
        return False

def load_reference_images():
    reference_images = {}
    for filename in os.listdir():
        if filename.lower().endswith((".jpg", ".jpeg")) and filename != "captured_note.jpg":
            label = filename.rsplit(".", 1)[0]
            img = cv2.imread(filename)
            if img is not None:
                reference_images[label] = img
    return reference_images

def average_color(image):
    return image.mean(axis=0).mean(axis=0)

def color_distance(c1, c2):
    return np.linalg.norm(c1 - c2)

def detect_note(captured_img, reference_images, orb_threshold=100, color_threshold=250):
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(cv2.cvtColor(captured_img, cv2.COLOR_BGR2GRAY), None)
    avg_color_captured = average_color(captured_img)

    best_match = None
    best_score = 0

    print("\n[DEBUG] Matches and color differences:")

    for label, ref_img in reference_images.items():
        kp2, des2 = orb.detectAndCompute(cv2.cvtColor(ref_img, cv2.COLOR_BGR2GRAY), None)

        if des1 is None or des2 is None:
            continue

        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1, des2)
        matches = sorted(matches, key=lambda x: x.distance)
        good_matches = len(matches)

        avg_color_ref = average_color(ref_img)
        color_diff = color_distance(avg_color_captured, avg_color_ref)

        print(f"{label}: {good_matches} matches | Color diff: {color_diff:.2f}")

        if good_matches >= orb_threshold and color_diff < color_threshold:
            if good_matches > best_score:
                best_score = good_matches
                best_match = label

    return best_match

# ========== MAIN ==========
if capture_image():
    speak("Starting detection. Please wait.")
    captured = cv2.imread("captured_note.jpg")

    if captured is None:
        speak("Could not load captured note image.")
    else:
        reference_images = load_reference_images()
        result = detect_note(captured, reference_images)

        if result:
            denomination = result.split("_")[0]
            speak(f"This is a {denomination} rupee note.")
            print(f"✅ Detected denomination: ₹{denomination}")
        else:
            speak("No currency note detected.")
            print("❌ No match found.")
