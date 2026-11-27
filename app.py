import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="SafePay - Fraud Detection", page_icon="🛡️")

# --- MODEL LOAD ---
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# --- LOGIN PAGE ---
if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.markdown("<h1 style='text-align:center'>🛡️ SafePay</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center'>Kaveri oda Final Year Project</p>", unsafe_allow_html=True)
    st.write("")
    user = st.text_input("Username")
    passw = st.text_input("Password", type="password")
    if st.button("Login", use_container_width=True):
        if user == "kaveri" and passw == "1234":
            st.session_state.login = True
            st.rerun()
        else:
            st.error("Username / Password thappu!")
    st.info("Demo Login: Username = kaveri, Password = 1234")
    st.stop()

# --- MAIN APP ---
st.title("🛡️ SafePay Dashboard")
st.write("Welcome Kaveri! 👋")

if "history" not in st.session_state:
    st.session_state.history = []

col1, col2 = st.columns(2)
with col1:
    amount = st.number_input("💰 Amount", min_value=0.0, value=100.0)
    location = st.selectbox("📍 Location", ["Chennai", "Delhi", "Mumbai", "Foreign Country"])
with col2:
    time = st.slider("🕒 Time", 0, 24, 12)
    st.write("Model: Random Forest")
    st.write("Accuracy: 98%")

if st.button("🔍 CHECK PANNU", use_container_width=True):
    is_foreign = 1 if location == "Foreign Country" else 0
    result = model.predict([[amount, time, is_foreign]])[0]
    status = "FRAUD" if result == 1 else "SAFE"
    st.session_state.history.append({"Amount": amount, "Location": location, "Time": time, "Result": status})
    if result == 1:
        st.error("### ⚠️ FRAUD DETECTED!")
    else:
        st.success("### ✅ SAFE TRANSACTION")
        st.balloons()

# --- DASHBOARD ---
st.write("---")
st.subheader("📊 Dashboard")
if len(st.session_state.history) > 0:
    df = pd.DataFrame(st.session_state.history)
    c1, c2, c3 = st.columns(3)
    c1.metric("Total", len(df))
    c2.metric("Safe", len(df[df.Result=="SAFE"]))
    c3.metric("Fraud", len(df[df.Result=="FRAUD"]))
    st.bar_chart(df["Result"].value_counts())
    st.subheader("📜 History")
    st.dataframe(df, use_container_width=True)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Report Download Pannu", csv, "SafePay_Report.csv", "text/csv", use_container_width=True)
else:
    st.write("Innum ethuvum check pannala. Mela poi check pannu.")
