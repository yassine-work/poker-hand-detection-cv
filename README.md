# Poker Hand Detection
A computer vision project to detect playing cards via webcam and identify poker hands using a fine-tuned YOLOv8 model.

## Description
This project uses a fine-tuned YOLOv8 model (`playingCards.pt`) to detect playing cards in a webcam feed. It identifies the cards, collects a hand of five unique cards, and determines the poker hand rank (e.g., Royal Flush, Straight) using a custom function. I built this to learn object detection, model fine-tuning, and real-time computer vision as part of my computer vision journey. The model was fine-tuned on a custom dataset to improve accuracy for playing card detection.

## How It Works
- **Detection**: A fine-tuned YOLOv8 model (`playingCards.pt`) detects playing cards in each frame of the webcam feed.
- **Classification**: The model identifies specific cards (e.g., `AH` for Ace of Hearts, `10S` for Ten of Spades) from a set of 52 classes representing a standard deck.
- **Hand Collection**: The script collects up to five unique cards detected with a confidence score above 0.5.
- **Poker Hand Evaluation**: A custom function (`PokerHandFunction.py`) evaluates the hand of five cards and determines the poker hand rank (e.g., Royal Flush, Straight Flush, Four of a Kind).
- **Visualization**: The webcam feed shows:
  - Bounding boxes around detected cards with their class names (e.g., `AH`) and confidence scores.
  - The poker hand rank (e.g., "Your Hand: Royal Flush") displayed on the video when five cards are detected.

## Requirements
- Python 3.x
- Install dependencies: pip install -r requirements.txt
- Key libraries: `ultralytics`, `opencv-python`, `cvzone`, `torch`.
- A webcam (the script uses webcam ID 2 by default; adjust if needed in `PokerHandDetection.py`).
- CUDA-enabled GPU (optional but recommended, as the script uses `model.to('cuda')` for faster inference).

## How to Run
1. Clone this repo
2. Navigate to the folder
3. Install the required dependencies:pip install -r requirements.txt
4. Run the script: python PokerHandDetection.py
- The script uses webcam ID 2 by default (line: `cap = cv2.VideoCapture(2)`). If your webcam has a different ID (e.g., 0 or 1), update this line in `PokerHandDetection.py`.
- Hold up to five playing cards in front of the webcam to detect them and see the poker hand rank.
- Note: This project requires the fine-tuned model `playingCards.pt`, which is not included. You would need access to the model file to run it locally (see Notes).

## Example Output
Watch a demo video of the poker hand detection in action [here](https://drive.google.com/file/d/1V055-70mSxEAEYEmvq9-ou0kDNFt_f5l/view?usp=sharing).

## Notes
- This is a beginner project—expect some rough edges!
- The model (`playingCards.pt`) was fine-tuned on a custom dataset to detect playing cards, enhancing accuracy for this specific use case. However, the model file is not provided in this repository due to its size.
- The script can be modified to use a video file instead of a webcam by uncommenting the video file line (`cap = cv2.VideoCapture("../videos/motorbikes-1.mp4")`) and commenting out the webcam line.
- The poker hand evaluation logic in `PokerHandFunction.py` supports all standard poker hands, from High Card to Royal Flush.
