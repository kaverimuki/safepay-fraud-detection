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
# USERS LIST - Yellarum Sign Up pannalam
if "users" not in st.session_state:
    st.session_state.users = {"kaveri": "1234"}

# LOGIN / SIGNUP PAGE
if not st.session_state.logged_in:
    st.title("💸 SafePay")
    st.write(" WELCOM Mam/Sir")
    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    with tab1:
        user = st.text_input("Username", key="login_user")
        pwd = st.text_input("Password", type="password", key="login_pwd")
        if st.button("Login"):
            if user in st.session_state.users and st.session_state.users[user] == pwd:
                st.session_state.logged_in = True
                st.session_state.current_user = user
                st.rerun()
            else:
                st.error("Wrong username / password. Illana Sign Up pannu!")

    with tab2:
        new_user = st.text_input("Pudhu Username", key="new_user")
        new_pwd = st.text_input("Pudhu Password", type="password", key="new_pwd")
        if st.button("Account Create Pannu"):
            if new_user == "" or new_pwd == "":
                st.warning("Username & Password type pannu!")
            elif new_user in st.session_state.users:
                st.error("Intha username already iruku! Vera name vaithu paaru")
            else:
                st.session_state.users[new_user] = new_pwd
                st.success(f"Super! {new_user} account create aayiduchu! Ippo Login pannu!")
    st.stop()

# MAIN APP
st.title("💸 SafePay")
st.write(f"Welcome {st.session_state.get('current_user', 'Kaveri')}! 👋")
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

# QR CODE - GPay maathiri
st.subheader("📷 My QR Code")
st.image("https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=kaveri@okSafePay", width=200)
st.write("UPI ID: kaveri@okSafePay")
st.write("Itha scan panni yaarum unaku kaasu anuppalalam!")

st.subheader("📱 Scan & Pay")
upi_id = st.text_input("UPI ID / QR la irukura peru", placeholder="ex: priya@okHDFC")
qr_amount = st.number_input("QR Amount (Rs.)", min_value=1, value=50, key="qr_amt")

if st.button("QR vazhiya Pay pannu"):
    if upi_id == "":
        st.warning("UPI ID ah type pannu Kaveri!")
    elif qr_amount > st.session_state.balance:
        st.error("Balance pothathu!")
    elif qr_amount > 100000:
        st.error("🚨 FRAUD Alert! Itha anuppa mudiyathu!")
    else:
        st.session_state.balance -= qr_amount
        st.success(f"✅ Rs. {qr_amount} {upi_id} ku QR vazhiya anuppiyachu!")
        st.balloons()
        st.session_state.history.append([qr_amount, upi_id, "SAFE - QR"])
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
       
  
