import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("sales_data_with_clusters.csv")
policy = pd.read_csv("cluster_best_discounts.csv")

st.set_page_config(page_title="Sales Optimization", page_icon="🛍", layout="centered")
st.title("🛍 Sales Optimization System")

# Initialize session states
if "customer_status" not in st.session_state:
    st.session_state.customer_status = None
if "discount" not in st.session_state:
    st.session_state.discount = None

# ---- PHONE INPUT ----
phone = st.text_input("Enter Customer Phone Number")

if st.button("Search"):
    if phone.strip() == "":
        st.error("❌ Enter a valid phone number")
    else:
        customer = df[df["Phone_No"] == phone] if "Phone_No" in df.columns else pd.DataFrame()

        if not customer.empty:
            st.session_state.customer_status = "existing"
            cluster_id = int(customer["Cluster_ID"].iloc[0])
            st.session_state.discount = int(policy[policy["Cluster_ID"] == cluster_id]["Best_Discount"].iloc[0])
            st.success(f"✅ Existing Customer Found (Cluster {cluster_id})")
        else:
            st.session_state.customer_status = "new"
            st.session_state.discount = 10
            st.warning("🆕 New Customer! Flat 10% discount applied")

# ---- EXISTING CUSTOMER UI ----
if st.session_state.customer_status == "existing":
    st.subheader("🛒 Purchase Items")
    q1 = st.number_input("Product A (₹500) Quantity", min_value=0, key="ex_q1")
    q2 = st.number_input("Product B (₹800) Quantity", min_value=0, key="ex_q2")

    if st.button("Generate Bill", key="bill_existing"):
        total = q1 * 500 + q2 * 800
        final = total - (total * st.session_state.discount / 100)

        st.success("✅ Bill Generated")
        st.write(f"Total: ₹{total}")
        st.write(f"Discount: {st.session_state.discount}%")
        st.write(f"Final Amount: ₹{final:.2f}")

# ---- NEW CUSTOMER UI ----
elif st.session_state.customer_status == "new":
    name = st.text_input("Customer Name", key="new_name")
    city = st.text_input("City", key="new_city")

    st.subheader("🛒 Purchase Items")
    q1 = st.number_input("Product A (₹500) Quantity", min_value=0, key="new_q1")
    q2 = st.number_input("Product B (₹800) Quantity", min_value=0, key="new_q2")

    if st.button("Generate Bill", key="bill_new"):
        total = q1 * 500 + q2 * 800
        final = total - (total * st.session_state.discount / 100)

        st.success("✅ Bill Generated")
        st.write(f"Customer: {name}")
        st.write(f"City: {city}")
        st.write(f"Total: ₹{total}")
        st.write(f"Discount: {st.session_state.discount}%")
        st.write(f"Final Amount: ₹{final:.2f}")
