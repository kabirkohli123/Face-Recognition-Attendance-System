# Face-Recognition-Attendance-System

### 📌 Overview  
The **Face Recognition Attendance System** is an AI-powered application that automates attendance tracking using facial recognition. The system captures, stores, and recognizes faces using OpenCV and machine learning techniques, making attendance marking seamless and efficient.

### 🚀 Features  
- **Face Detection & Recognition** using OpenCV and Haar cascades  
- **Automated Attendance Marking**  
- **Database Integration** for storing recognized faces  
- **User-Friendly Interface** with real-time feedback  

### 🛠️ Installation  

#### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/kabirkohli123/Face-Recognition-Attendance-System
cd Face-Recognition-Attendance-System
```

#### 2️⃣ Install Dependencies  
Ensure you have Python installed, then run:  
```bash
pip install -r requirements.txt
```

#### 3️⃣ Run the Application  
- **Add Faces to the System:**  
  ```bash
  python add_faces.py
  ```
  This script captures and stores face data for recognition.  

- **Start the Face Recognition System:**  
  ```bash
  python app.py
  ```
  This script runs the face recognition attendance system.  

- **Test the System (Optional):**  
  ```bash
  python test.py
  ```
  Runs a test to verify the recognition accuracy.  

### 📂 Project Structure  
```
/face-recognition-attendance
│── add_faces.py                  # Script to add new faces  
│── app.py                         # Main application script  
│── test.py                        # Testing script  
│── haarcascade_frontalface_default.xml  # Pre-trained face detection model  
│── faces_data.pkl                 # Stored face embeddings  
│── names.pkl                      # Names associated with stored faces  
│── NewBack2.webp                   # Background image for UI  
│── README.md                       # Project documentation  
│── requirements.txt                # Required Python libraries  
```

### 📌 Technologies Used  
- **Python**  
- **OpenCV** (Face Detection & Recognition)  
- **NumPy** (Data Handling)  
- **Streamlit** (Web Framework)  

### 👨‍💻 Contribution  
Contributions are welcome! Fork the repo, create a feature branch, and submit a pull request.  


