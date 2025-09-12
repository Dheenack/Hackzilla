import streamlit as st

st.title("🩸 Hackzilla — Anemia Test Data Input")

# Custom CSS for enhanced transparency and rounded inputs
st.markdown("""
<style>
    div.stSelectbox > div[data-baseweb="select"] > div {
        border-radius: 12px !important;
        background-color: #1e1e2f;
        color: white;
    }
    div.stNumberInput > div > input {
        border-radius: 10px !important;
        background-color: #282c48;
        color: #b4b8ff;
        font-weight: 600;
        font-size: 16px;
        padding: 6px 12px;
    }
    div.stButton > button {
        border-radius: 14px;
        background: linear-gradient(90deg, #5e5eff, #88aaff);
        color: white;
        font-weight: bold;
        font-size: 18px;
        padding: 10px 20px;
        margin-top: 8px;
        box-shadow: 0 0 10px #6677ffaa;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #8a8aff, #bbd1ff);
        box-shadow: 0 0 15px #99aaffcc;
    }
    .stRadio > label {
        font-size: 16px;
        color: #aabbee;
        font-weight: 600;
        margin-bottom: 6px;
    }
</style>
""", unsafe_allow_html=True)

with st.form("anemia_form"):
    st.markdown("### Please fill all fields with accurate values:")
    gender = st.radio("Gender", options=["Male", "Female"], horizontal=True)
    hemoglobin = st.number_input("Hemoglobin (g/dL)", min_value=0.0, max_value=30.0, step=0.1, format="%.1f")
    mch = st.number_input("MCH (pg)", min_value=0.0, max_value=40.0, step=0.1, format="%.1f")
    mchc = st.number_input("MCHC (g/dL)", min_value=0.0, max_value=40.0, step=0.1, format="%.1f")
    mcv = st.number_input("MCV (fL)", min_value=0.0, max_value=130.0, step=0.1, format="%.1f")
    submitted = st.form_submit_button("Analyze Data")

    if submitted:
        st.success(f"Submitted data: Gender={gender}, Hemoglobin={hemoglobin}, MCH={mch}, MCHC={mchc}, MCV={mcv}")
