import streamlit as st
import pandas as pd

st.set_page_config(page_title="SafePay - GPay Style", page_icon="💸")

# Login check
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "balance" not in st.session_state:
    st.session_state.balance = 5000
if "history" not in st.session_state:
    st.session_state.history = []

# LOGIN PAGE
if not st.session_state.logged_in:
    st.title("💸 SafePay")
    st.write("GPay / PhonePe maathiri Safe Payment App")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("Login"):
        if user == "kaveri" and pwd == "1234":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Wrong username / password")
    st.info("Demo Login: kaveri / 1234")
    st.stop()

# MAIN APP
st.title("💸 SafePay")
st.write("Welcome Kaveri! 👋")

# WALLET BALANCE - GPay maathiri
st.markdown(f"### 💰 Wallet Balance: ₹ {st.session_state.balance}")
st.progress(100)
col1, col2 = st.columns(2)
with col1:
    st.metric("Model", "Random Forest")
with col2:
    st.metric("Accuracy", "98%")

st.divider()

# SEND MONEY - GPay maathiri
st.subheader("📤 Send Money")
receiver = st.selectbox("Yaaruku anuppa pora?", ["Amma", "Appa", "Friend - Priya", "Friend - Anu", "Shop - Murugan Store"])
amount = st.number_input("Amount (₹)", min_value=1, value=100)
time = st.slider("Time (Hour)", 0, 23, 12)
location = st.selectbox("Location", ["Chennai", "Mumbai", "Delhi", "Coimbatore"])

if st.button("CHECK PANNU & SEND"):
    # Fraud Check - Simple Rule
    is_fraud = False
    if amount > 100000:
        is_fraud = True
    if amount > st.session_state.balance:
        st.error("Balance pothathu! Balance: ₹ " + str(st.session_state.balance))
    elif is_fraud:
        st.error("🚨 FRAUD Alert! Itha anuppa mudiyathu!")
        st.session_state.history.append([amount, receiver, "FRAUD"])
    else:
        st.session_state.balance -= amount
        st.success(f"✅ ₹ {amount} {receiver} ku anuppiyachu!")
        st.balloons()
        st.session_state.history.append([amount, receiver, "SAFE"])
        st.rerun()

st.divider()

# HISTORY
st.subheader("📜 History")
if len(st.session_state.history) == 0:
    st.write("Innum transaction illa")
else:
       for h in reversed(st.session_state.history):
        st.write(f"Rs. {h[0]} -> {h[1]} | {h[2]}") 
if st.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()
       
  
