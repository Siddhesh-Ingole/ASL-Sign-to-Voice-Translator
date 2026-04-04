# 🚀 Real-Time ASL Sign-to-Voice Translator

## 📌 Description  
This project is a real-time hand gesture recognition system that translates American Sign Language (ASL) into text and voice output.  

It enables seamless communication by converting hand gestures into readable text 📝 and audible speech 🔊 using computer vision and machine learning.

---

## 🌟 Key Highlights  
- ⚡ Real-time gesture recognition  
- ✋ Accurate hand tracking using MediaPipe  
- 🧠 Machine learning-based gesture classification  
- 📝 Text output with confidence score  
- 🔊 Voice output for each detected gesture  
- 📊 Stable predictions using smoothing technique  

---

## 🚀 Technologies Used  
- 🐍 Python  
- 📷 OpenCV – Real-time video processing  
- ✋ MediaPipe – Hand landmark detection  
- 🤖 Scikit-learn – Machine learning model  
- 📊 Pandas – Data handling  
- 💾 Joblib – Model saving/loading  
- 🔊 pyttsx3 – Text-to-speech conversion  

---

## ⚙️ Functionality  
- 🎥 Captures live video from webcam  
- ✋ Detects hand and extracts landmark points  
- 🧠 Predicts ASL gesture using trained ML model  
- 📝 Converts gesture into meaningful text  
- 🔊 Speaks the detected output  
- 📊 Displays confidence percentage for each prediction  
- 🔁 Ensures stable output using prediction buffering  

---

## 📊 Model Details  
- 🧠 Algorithm: Random Forest Classifier  
- 📌 Type: Multi-class Classification  
- 📥 Input: Hand landmark coordinates (normalized)  
- 📤 Output: Gesture label with confidence score  

---

## 🧠 How It Works  

1. 🎥 Webcam captures real-time video  
2. ✋ MediaPipe detects hand landmarks  
3. 📍 Landmark coordinates are extracted and normalized  
4. 🤖 Data is passed to trained ML model  
5. 📊 Model predicts gesture with confidence  
6. 📝 Output is displayed as text  
7. 🔊 Voice output is generated for the detected gesture  

---

## 🖼️ Output Screenshots  


![WhatsApp Image 2026-04-04 at 11 35 35 PM](https://github.com/user-attachments/assets/a9343acb-02f3-4b3a-b353-b308a576a611)


---

## 🎥 Demo Video  



https://github.com/user-attachments/assets/dde8afea-393e-43e1-af14-1d0e2622a713

---

## 📂 Project Structure  

ASL-Sign-to-Voice-Translator/
│── main.py
│── train_model.py
│── gesture_model.pkl
│── requirements.txt
│── README.md

---

## ▶️ How to Run  

### 1️⃣ Install dependencies  

pip install -r requirements.txt

### 2️⃣ Run the project  

python main.py

---

## 🎯 Supported Gestures  

- 👋 HELLO → Hello  
- ❤️ ILOVEYOU → I Love You  
- 🆘 HELP → I Need Help  
- 👍 YES → Yes  
- 👎 NO → No  
- 🙏 PLEASE → Please  
- 🙌 THANKYOU → Thank You  

---

## 🎯 Learning Outcomes  
- 👁️ Implemented real-time computer vision system  
- 🤖 Applied machine learning for gesture classification  
- ✋ Learned hand tracking using MediaPipe  
- 🔊 Integrated text-to-speech functionality  
- ⚡ Improved system stability using prediction smoothing  

---

## 🔗 Project Status  
✔️ Completed and working successfully  

---

## 🔮 Future Improvements  
- ➕ Add more ASL gestures  
- 📈 Improve model accuracy  
- 🧠 Add sentence formation  
- 🌐 Deploy as web application  
- 📱 Develop mobile version  

---

## 👨‍💻 Developer 
Siddhesh Ingole 

---

## 📜 License  
This project is licensed under the MIT License.
