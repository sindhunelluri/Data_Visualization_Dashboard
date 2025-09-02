import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Data Visualization Dashboard", layout="wide")

# -----------------------------
# Title
# -----------------------------
st.title("📊 Interactive Data Visualization Dashboard")

st.write(
    """
    This dashboard lets you *analyze and visualize datasets* 
    using *Pandas, Matplotlib, and Seaborn*.
    """
)

# -----------------------------
# File Upload
# -----------------------------
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    # Load dataset
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    # Show first rows
    st.subheader("📌 Data Preview")
    st.dataframe(df.head())

    # Show dataset info
    st.subheader("📌 Dataset Summary")
    st.write(df.describe())

    # -----------------------------
    # Column Selection
    # -----------------------------
    st.sidebar.header("Visualization Settings")
    all_columns = df.columns.tolist()

    # Select columns for visualization
    x_axis = st.sidebar.selectbox("Choose X-axis", all_columns)
    y_axis = st.sidebar.selectbox("Choose Y-axis", all_columns)
    chart_type = st.sidebar.radio("Select Chart Type", ["Scatter", "Line", "Bar", "Histogram", "Boxplot", "Heatmap"])

    # -----------------------------
    # Plotting
    # -----------------------------
    st.subheader("📊 Visualization")

    fig, ax = plt.subplots(figsize=(8, 5))

    if chart_type == "Scatter":
        sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax)
    elif chart_type == "Line":
        sns.lineplot(data=df, x=x_axis, y=y_axis, ax=ax)
    elif chart_type == "Bar":
        sns.barplot(data=df, x=x_axis, y=y_axis, ax=ax)
    elif chart_type == "Histogram":
        sns.histplot(df[x_axis], kde=True, ax=ax)
    elif chart_type == "Boxplot":
        sns.boxplot(data=df, x=x_axis, y=y_axis, ax=ax)
    elif chart_type == "Heatmap":
        corr = df.corr(numeric_only=True)
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
        st.write("🔍 Heatmap of correlations between numeric columns")
    st.pyplot(fig)

else:
    st.info("👆 Please upload a CSV file to begin.")