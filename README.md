# Student Performance Predictor

This project is a **Multiple Linear Regression Model** that predicts a student's **Performance Index** based on study habits, sleep hours, extracurricular activities, and previous scores.

🚀 Live Demo: [Student Performance Predictor App](https://student-performance-predictor-project.streamlit.app/)

---

##  Features
- Predicts student performance using study-related inputs  
- Considers factors like hours studied, sleep, previous scores, and practice tests  
- Clean **Streamlit UI** for easy interaction  
- Deployed online for instant access  

---

## Tech Stack
- **Python**
- **Pandas, NumPy, Scikit-learn**
- **Streamlit**
- **Joblib** (for model saving & loading)

---
## Project Structure
.
├── app.py              # Streamlit app  
├── model.pkl           # Saved trained model  
├── requirements.txt    # Dependencies  
├── project.ipynb       # Jupyter Notebook (data analysis & model training)  
└── README.md           # Project description  


## How to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/student-performance-predictor.git
   cd student-performance-predictor

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the Streamlit app:
   ```bash
   streamlit run app.py


## Dataset

The dataset includes:
- Hours Studied  
- Previous Scores  
- Extracurricular Activities (Yes/No)  
- Sleep Hours  
- Sample Question Papers Practiced  
- **Performance Index (Target)**  

---

## Results
- Achieved **R² Score ~ 0.99** → very high predictive accuracy  
- Factors like **Hours Studied** and **Previous Scores** strongly impact performance  
- **Balanced Sleep Hours** also play a significant role  

---

## Author
**Aanchal Pandey**  
Computer Science Graduate  
