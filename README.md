# Currency-Detector-for-Visually-Impaired
Currency Detector for Visually Impaired is a Python-based project that helps identify Indian currency notes using a webcam. It uses ORB feature matching and color histogram verification for accurate detection, and provides audio feedback through text-to-speech, making it accessible and user-friendly.
💵 Currency Detector for Visually Impaired
📌 Project Overview

The Currency Detector for Visually Impaired is a Python-based project designed to help visually impaired individuals identify Indian currency notes using a simple webcam and audio guidance.

The system uses:

ORB (Oriented FAST and Rotated BRIEF) for feature extraction and matching.

Color Histogram Matching (HSV) for secondary verification based on dominant note colors.

pyttsx3 for text-to-speech output, so the detected denomination is spoken aloud.

The application is lightweight, works in real-time, and does not require deep learning models or GPUs, making it suitable for everyday use.

🎯 Features

✔️ Real-time note detection using webcam

✔️ Automated countdown capture (3…2…1)

✔️ ORB-based keypoint and descriptor matching

✔️ Dual verification with color histogram analysis

✔️ Accurate detection of front and back sides

✔️ Voice output using text-to-speech for accessibility

✔️ Works offline without internet dependency

🛠️ Tech Stack

Language: Python 3

Libraries Used:

OpenCV → Image processing, ORB, feature matching

pyttsx3 → Text-to-Speech engine

NumPy → Array and matrix operations

Matplotlib (optional, for debugging/visualizations)

💻 Installation & Setup

Clone the repository

git clone https://github.com/your-username/currency-detector-visually-impaired.git
cd currency-detector-visually-impaired


Install required dependencies

pip install opencv-python pyttsx3 numpy matplotlib


Run the project

python app.py

📂 Dataset

Contains reference images of Indian currency notes (front and back).

Each note has unique features and color profiles used for matching.

Example denominations supported: ₹10, ₹20, ₹50, ₹100, ₹200, ₹500.

📊 Working Process

Image Capture → Webcam automatically captures the note after countdown.

Feature Extraction (ORB) → Keypoints and descriptors are extracted.

Feature Matching → Captured descriptors are matched with dataset reference images using Brute-Force Matcher.

Color Matching → Dominant color histogram is compared in HSV color space.

Final Detection → System declares the denomination and announces via voice output.

📸 Screenshots (add these later)

Webcam detection window

Debug output (matches + color differences)

Voice feedback example

🔮 Future Scope

Add support for all Indian denominations including ₹2000.

Mobile app version for smartphones.

Add fake note detection using watermark and hologram features.

Multi-language speech output (Hindi, Telugu, etc.).
