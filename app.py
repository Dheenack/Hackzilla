# app.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hackzilla — Anemia Explorer", layout="wide")
st.title("Hackzilla — Anemia Dataset Explorer")

@st.cache_data
def load_data():
    # tries CSV first, then xlsx
    try:
        return pd.read_csv("anemia.csv")
    except Exception:
        return pd.read_excel("Anemia Dataset.xlsx")

df = load_data()
st.subheader("Preview")
st.dataframe(df.head())

st.subheader("Basic stats")
st.write(df.describe(include="all"))

# let user pick a numeric column to plot (safely handle missing)
num_cols = df.select_dtypes(include=["number"]).columns.tolist()
if num_cols:
    col = st.selectbox("Choose numeric column to plot", num_cols)
    st.line_chart(df[col].dropna().reset_index(drop=True))
else:
    st.info("No numeric columns found to plot.")

# file upload (optional)
st.sidebar.header("Upload your own file (optional)")
uploaded = st.sidebar.file_uploader("CSV or XLSX", type=['csv','xlsx'])
if uploaded is not None:
    try:
        if uploaded.name.endswith(".csv"):
            df2 = pd.read_csv(uploaded)
        else:
            df2 = pd.read_excel(uploaded)
        st.sidebar.write(df2.head())
    except Exception as e:
        st.sidebar.error(f"Failed to read uploaded file: {e}")
