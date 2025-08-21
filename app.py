import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

CSV = r"D:\GUVI\Employee Project\Employee-Attrition - Employee-Attrition.csv"
ATTRITION_PKL = r"C:\Users\Rajkumar\Guvi\Projects\Project_3\attrition_model.pkl"
PERFORMANCE_PKL = r"C:\Users\Rajkumar\Guvi\Projects\Project_3\performance_model.pkl"

selected_features = [
    "MonthlyIncome", "JobRole", "TotalWorkingYears", "HourlyRate", 
    "YearsAtCompany", "TrainingTimesLastYear", "MonthlyRate", "BusinessTravel", 
    "JobInvolvement", "WorkLifeBalance", "RelationshipSatisfaction", "Attrition", 
    "EnvironmentSatisfaction", "JobSatisfaction", "StockOptionLevel", 
    "YearsSinceLastPromotion", "YearsWithCurrManager"
]

df = pd.read_csv(CSV)

le_jobrole = LabelEncoder()
df["JobRole_encoded"] = le_jobrole.fit_transform(df["JobRole"])


with open(ATTRITION_PKL, "rb") as f:
    attrition_model = pickle.load(f)

with open(PERFORMANCE_PKL, "rb") as f:
    performance_model = pickle.load(f)


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Introduction", "Dataset & EDA", "Prediction"])


if page == "Introduction":
    st.title("Project Introduction: Employee Attrition Analysis and Prediction")
    st.write("""
    Employee attrition is one of the most pressing challenges faced by organizations today.
    High turnover not only increases hiring and training costs but also disrupts productivity,
    team morale, and long-term business growth.
    This project, Employee Attrition Analysis and Prediction, focuses on leveraging HR Analytics to understand the key
    factors driving employee turnover and predict which employees are at risk of leaving. By applying data preprocessing,
    exploratory data analysis (EDA), feature engineering, and machine learning models, the project provides valuable
    insights into workforce dynamics and empowers HR teams to take proactive measures.
    Through interactive Streamlit dashboards, this project highlights:
    🔎 Attrition Trends Patterns and correlations across demographics, roles, and performance.

    🧠 Key Drivers Identifying factors such as job satisfaction, compensation, career growth, and work-life balance
    that influence attrition.

    🤖 Predictive Models Logistic Regression, Decision Trees, and Random Forests used to predict employee attrition
    with high accuracy.

    📊 Actionable Insights Highlighting at-risk employees and suggesting data-driven retention strategies to reduce turnover.

    Ultimately, the goal is to support HR leaders in improving employee retention, optimizing costs, and enhancing
    workforce satisfaction by transforming raw employee data into meaningful insights and predictive intelligence. 
    """)


elif page == "Dataset & EDA":
    st.title("Dataset Overview")

    st.write("Preview of dataset:")
    st.dataframe(df.head())

    st.write("Summary statistics:")
    st.write(df.describe())

    st.header("Simple Plots")

    # Attrition distribution
    st.subheader("Attrition Distribution")
    if "Attrition" in df.columns:
        fig, ax = plt.subplots()
        sns.countplot(x="Attrition", data=df, ax=ax)
        st.pyplot(fig)

    # Age distribution
    st.subheader("Age Distribution")
    if "Age" in df.columns:
        fig, ax = plt.subplots()
        sns.histplot(df["Age"], kde=True, ax=ax)
        st.pyplot(fig)

    # Performance Rating distribution
    st.subheader("Performance Rating Distribution")
    if "PerformanceRating" in df.columns:
        fig, ax = plt.subplots()
        sns.countplot(x="PerformanceRating", data=df, ax=ax)
        st.pyplot(fig)


elif page == "Prediction":
    st.title("Make Predictions")


    st.header("Attrition Prediction (Logistic Regression)")
    age = st.number_input("Age", min_value=18, max_value=60, value=30, key="attr_age")
    income = st.number_input("Monthly Income", min_value=1000, max_value=50000, value=5000, key="attr_income")
    years = st.number_input("Years at Company", min_value=0, max_value=40, value=5, key="attr_years")

    if st.button("Predict Attrition"):
        sample = pd.DataFrame([[age, income, years]], 
                              columns=["Age", "MonthlyIncome", "YearsAtCompany"])
        pred = attrition_model.predict(sample)[0]
        st.success(f"Attrition Prediction: {'Yes' if pred == 1 else 'No'}")

    st.markdown("---")

    st.header("Performance Rating Prediction (Random Forest)")

    monthly_income = st.number_input("Monthly Income", min_value=1000, max_value=50000, value=5000, key="perf_income")
    jobrole = st.selectbox("Job Role", df["JobRole"].unique(), key="perf_jobrole")
    total_years = st.number_input("Total Working Years", min_value=0, max_value=40, value=10, key="perf_totalyears")
    hourly_rate = st.number_input("Hourly Rate", min_value=10, max_value=100, value=50, key="perf_hourly")
    years_company = st.number_input("Years at Company", min_value=0, max_value=40, value=5, key="perf_yearscompany")
    training_times = st.slider("Training Times Last Year", 0, 10, 3, key="perf_training")
    monthly_rate = st.number_input("Monthly Rate", min_value=1000, max_value=100000, value=20000, key="perf_monthlyrate")
    business_travel = st.selectbox("Business Travel", df["BusinessTravel"].unique(), key="perf_bt")
    job_involvement = st.slider("Job Involvement (1-4)", 1, 4, 3, key="perf_involvement")
    work_life = st.slider("Work Life Balance (1-4)", 1, 4, 3, key="perf_worklife")
    relationship_satisfaction = st.slider("Relationship Satisfaction (1-4)", 1, 4, 3, key="perf_relationship")
    attrition = st.selectbox("Attrition", ["Yes", "No"], key="perf_attrition")
    env_satisfaction = st.slider("Environment Satisfaction (1-4)", 1, 4, 3, key="perf_envsat")
    job_satisfaction = st.slider("Job Satisfaction (1-4)", 1, 4, 3, key="perf_jobsat")
    stock_option = st.slider("Stock Option Level", 0, 3, 1, key="perf_stock")
    years_promo = st.number_input("Years Since Last Promotion", min_value=0, max_value=20, value=1, key="perf_promo")
    years_manager = st.number_input("Years With Current Manager", min_value=0, max_value=20, value=3, key="perf_manager")

    if st.button("Predict Performance Rating"):

        jobrole_encoded = le_jobrole.transform([jobrole])[0]
        bt_encoded = pd.factorize(df["BusinessTravel"])[0][list(df["BusinessTravel"].unique()).index(business_travel)]
        attrition_encoded = 1 if attrition == "Yes" else 0


        sample = pd.DataFrame([[monthly_income, jobrole_encoded, total_years, hourly_rate,
                                years_company, training_times, monthly_rate, bt_encoded,
                                job_involvement, work_life, relationship_satisfaction, attrition_encoded,
                                env_satisfaction, job_satisfaction, stock_option, years_promo, years_manager]],
                                columns=selected_features)

        pred = performance_model.predict(sample)[0]
        st.success(f"Predicted Performance Rating: {pred}")

