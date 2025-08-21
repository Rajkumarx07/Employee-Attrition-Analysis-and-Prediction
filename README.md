# 📊 Employee Attrition Analysis and Prediction  

## 🔎 Project Overview  
Employee attrition is one of the most critical challenges faced by organizations, leading to **increased costs, reduced productivity, and workforce instability**. This project leverages **HR Analytics** to analyze employee data, identify key drivers of attrition, and build predictive models to help organizations **retain talent and optimize HR strategies**.  

The project includes:  
- **Exploratory Data Analysis (EDA)** to uncover patterns and trends.  
- **Machine Learning models** to predict employee attrition and performance rating.  
- **Interactive Streamlit application** for data visualization and prediction.  

---

## 🏷️ Domain  
**Human Resource (HR) Analytics – Predicting and Preventing Employee Attrition**  

---

## 🎯 Problem Statement  
Employee turnover creates significant challenges such as higher recruitment costs, team disruption, and productivity loss. By identifying the factors driving attrition and predicting employees most at risk, HR teams can take **proactive retention measures**.  

---

## 💡 Business Use Cases  
- **Employee Retention:** Identify at-risk employees and design personalized retention strategies.  
- **Cost Optimization:** Reduce recruitment, onboarding, and training expenses caused by attrition.  
- **Workforce Planning:** Align retention initiatives with organizational goals to improve employee engagement.  

---

## 🛠️ Skills Gained  
- Data Preprocessing & Cleaning  
- Exploratory Data Analysis (EDA)  
- Feature Engineering  
- Machine Learning Model Development (Logistic Regression, Decision Trees, Random Forest)  
- Model Evaluation (Accuracy, Precision, Recall, ROC-AUC)  
- Streamlit Dashboard Development  

---

## 📂 Project Structure  
```
├── Employee.ipynb          # Jupyter Notebook for data preprocessing, EDA, and model training
├── app.py                  # Streamlit app for visualization and prediction
├── attrition_model.pkl     # Trained Logistic Regression model (Attrition Prediction)
├── performance_model.pkl   # Trained Random Forest model (Performance Rating Prediction)
├── Employee-Attrition.csv  # Employee dataset
└── README.md               # Project documentation
```

---

## 📊 Approach  
1. **Data Collection & Preprocessing:**  
   - Loaded and cleaned employee dataset.  
   - Handled missing values, outliers, and categorical variables using encoding.  

2. **Exploratory Data Analysis (EDA):**  
   - Attrition trends by age, salary, and job role.  
   - Performance rating distributions.  
   - Correlation analysis to identify key drivers.  

3. **Feature Engineering:**  
   - Encoded categorical variables like Job Role, Business Travel, and Attrition.  
   - Created features for tenure, job involvement, satisfaction levels, etc.  

4. **Model Development:**  
   - **Attrition Prediction:** Logistic Regression model.  
   - **Performance Rating Prediction:** Random Forest model using multiple features.  

5. **Evaluation:**  
   - Models evaluated on accuracy and other metrics.  
   - Achieved optimal performance threshold (≥85% accuracy).  

6. **Deployment with Streamlit:**  
   - Introduction page.  
   - Dataset & EDA visualization page.  
   - Prediction page (Attrition + Performance Rating).  

---

## 🚀 How to Run the Project  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/employee-attrition.git
   cd employee-attrition
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:  
   ```bash
   streamlit run app.py
   ```

---

## 📌 Results  
- ✅ **Predictive Accuracy:** Models achieved high accuracy (>85%).  
- 🔑 **Key Drivers Identified:** Salary, job satisfaction, work-life balance, and career growth were major attrition factors.  
- 👥 **At-Risk Employees:** Ranked list of employees most likely to leave.  
- 📉 **Impact:** Insights to reduce attrition, optimize costs, and improve retention strategies.  

---

## 📷 Streamlit App Features  
- **Introduction Page** – Project overview.  
- **Dataset & EDA Page** – Data preview, summary statistics, and visualizations (attrition distribution, age distribution, performance rating).  
- **Prediction Page** –  
  - Attrition prediction (Yes/No).  
  - Performance rating prediction (1–4).  

---

## 🛠️ Tech Stack  
- **Python**  
- **Pandas, NumPy, Scikit-learn** – Data preprocessing & ML models  
- **Matplotlib, Seaborn** – Data visualization  
- **Streamlit** – Interactive dashboards  
- **Pickle** – Model saving & loading  

---

## 📢 Conclusion  
This project provides HR professionals with a **data-driven approach to employee retention**. By predicting attrition and identifying the key drivers, organizations can implement **targeted strategies** to improve employee satisfaction, reduce costs, and enhance workforce stability.  
