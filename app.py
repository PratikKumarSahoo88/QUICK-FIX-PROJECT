import streamlit as st
import random # Imported to generate random Customer IDs

# --- PAGE CONFIGURATION & SESSION STATE ---
st.set_page_config(page_title="QuickFix | Home Services", page_icon="🔧", layout="wide")

# 1. User Login State
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['username'] = ""
    st.session_state['customer_id'] = "" # New state for Customer ID

# 2. Shopping Cart State (List to hold multiple items)
if 'cart' not in st.session_state:
    st.session_state['cart'] = []

# --- MOCK DATA ---
SERVICES = [
    {"name": "AC Repair & Service", "price": "499", "category": "Appliance", "rating": "⭐ 4.8"},
    {"name": "Deep Home Cleaning", "price": "1299", "category": "Cleaning", "rating": "⭐ 4.7"},
    {"name": "Electrician", "price": "199", "category": "Repair", "rating": "⭐ 4.9"},
    {"name": "Plumber", "price": "149", "category": "Repair", "rating": "⭐ 4.6"},
    {"name": "Beauty Salon at Home", "price": "799", "category": "Beauty", "rating": "⭐ 4.8"},
    {"name": "Washing Machine Repair", "price": "349", "category": "Appliance", "rating": "⭐ 4.5"},
    {"name": "Refrigerator Repair", "price": "399", "category": "Appliance", "rating": "⭐ 4.7"},
    {"name": "Geyser Repair", "price": "249", "category": "Repair", "rating": "⭐ 4.6"},
]

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🔧 QuickFix")

cart_count = len(st.session_state['cart'])

if st.session_state['logged_in']:
    st.sidebar.success(f"Welcome, {st.session_state['username']}!")
    pages = ["Home", "Browse Services", f"🛒 Cart & Checkout ({cart_count})", "My Profile", "Become a Partner"]
else:
    st.sidebar.info("You are not logged in.")
    pages = ["Home", "Browse Services", f"🛒 Cart & Checkout ({cart_count})", "Login / Signup", "Become a Partner"]

page = st.sidebar.radio("Navigation", pages)

# Helper function to add to cart
def add_to_cart(service):
    st.session_state['cart'].append(service)
    st.toast(f"Added {service['name']} to cart! 🛒")

# --- PAGE 1: HOME ---
if page == "Home":
    st.title("Book Trusted Home Services at your Doorstep")
    st.subheader("Fast, Reliable & Affordable solutions")
    st.write("---")
    
    search_query = st.text_input("🔍 Search for services (e.g., AC, Cleaning, Electrician)")
    
    st.write("### Explore Categories")
    selected_category = None
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("❄️ Air Conditioner", use_container_width=True): selected_category = "Appliance"
        if st.button("🧹 Cleaning", use_container_width=True): selected_category = "Cleaning"
    with col2:
        if st.button("💅 Beauty Salon", use_container_width=True): selected_category = "Beauty"
        if st.button("🧺 Washing Machine", use_container_width=True): selected_category = "Appliance"
    with col3:
        if st.button("🧊 Refrigerator", use_container_width=True): selected_category = "Appliance"
        if st.button("⚡ Electrician", use_container_width=True): selected_category = "Repair"
    with col4:
        if st.button("🚿 Geyser", use_container_width=True): selected_category = "Repair"
        if st.button("🚰 Plumber", use_container_width=True): selected_category = "Repair"

    active_filter = search_query.lower() if search_query else (selected_category.lower() if selected_category else "")

    if active_filter:
        st.write("---")
        st.write(f"### Results for '{search_query or selected_category}'")
        
        filtered_services = [s for s in SERVICES if active_filter in s['name'].lower() or active_filter in s['category'].lower()]
        
        if filtered_services:
            for service in filtered_services:
                with st.container():
                    c1, c2 = st.columns([3, 1])
                    with c1:
                        st.write(f"#### {service['name']}")
                        st.write(f"**Price:** ₹{service['price']} | {service['rating']}")
                    with c2:
                        if st.button("Add to Cart", key=f"home_add_{service['name']}"):
                            add_to_cart(service)
                    st.write("---")
        else:
            st.warning("No services found.")

# --- PAGE 2: BROWSE SERVICES ---
elif page == "Browse Services":
    st.title("All Available Services")
    
    for service in SERVICES:
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"### {service['name']}")
                st.write(f"**Price:** ₹{service['price']} | {service['rating']}")
                st.write(f"*Category: {service['category']}*")
            with col2:
                if st.button("Add to Cart", key=f"browse_add_{service['name']}"):
                    add_to_cart(service)
            st.write("---")

# --- PAGE 3: CART & CHECKOUT ---
elif page.startswith("🛒 Cart & Checkout"):
    st.title("Your Shopping Cart")
    
    if len(st.session_state['cart']) == 0:
        st.info("Your cart is empty. Go to 'Browse Services' to add some!")
    else:
        total_price = 0
        for i, item in enumerate(st.session_state['cart']):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"**{item['name']}**")
            with col2:
                st.write(f"₹{item['price']}")
                total_price += int(item['price'])
            st.write("---")
            
        st.subheader(f"Total: ₹{total_price}")
        
        st.write("### Checkout Details")
        if not st.session_state['logged_in']:
            st.warning("⚠️ You must be logged in to checkout. Please go to Login / Signup in the sidebar.")
        else:
            with st.form("checkout_form"):
                st.write("Step 1: Address")
                address = st.text_area("Full Delivery Address")
                
                st.write("Step 2: Schedule")
                col1, col2 = st.columns(2)
                date = col1.date_input("Select Date")
                time = col2.selectbox("Select Time Slot", ["09:00 AM - 11:00 AM", "12:00 PM - 02:00 PM", "03:00 PM - 05:00 PM"])
                
                st.write("Step 3: Payment")
                payment = st.radio("Payment Method", ["Cash on Delivery", "Pay Online"])
                
                submitted = st.form_submit_button("Confirm Booking & Pay", type="primary")
                
                if submitted:
                    if address:
                        st.balloons()
                        # Generate a random Order ID for realism
                        order_id = random.randint(100000, 999999)
                        st.success(f"🎉 Booking Confirmed! Order ID: #{order_id}. Your total of ₹{total_price} will be collected via {payment}.")
                        st.session_state['cart'] = []
                    else:
                        st.error("Please provide a delivery address.")

# --- PAGE 4: LOGIN / SIGNUP / PROFILE ---
elif page in ["Login / Signup", "My Profile"]:
    if not st.session_state['logged_in']:
        st.title("Welcome to QuickFix")
        
        auth_mode = st.radio("Choose an option:", ["Login", "Sign Up"], horizontal=True)
        st.write("---")
        
        if auth_mode == "Login":
            st.subheader("Login to your account")
            login_username = st.text_input("Username", key="login_user")
            login_password = st.text_input("Password", type="password", key="login_pass")
            
            if st.button("Login", type="primary"):
                if login_username and login_password:
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = login_username
                    # Assign a mock Customer ID on login
                    st.session_state['customer_id'] = f"QF-{random.randint(10000, 99999)}"
                    st.rerun()
                else:
                    st.error("Please enter your username and password.")
                    
        elif auth_mode == "Sign Up":
            st.subheader("Create a new account")
            new_username = st.text_input("Choose Username", key="signup_user")
            new_password = st.text_input("Choose Password", type="password", key="signup_pass")
            confirm_password = st.text_input("Confirm Password", type="password", key="signup_confirm")
            
            if st.button("Create Account", type="primary"):
                if not new_username or not new_password:
                    st.error("Please fill in all fields.")
                elif new_password != confirm_password:
                    st.error("Passwords do not match!")
                else:
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = new_username
                    # Generate a random Customer ID on sign up
                    st.session_state['customer_id'] = f"QF-{random.randint(10000, 99999)}"
                    st.success("Account created successfully! Logging you in...")
                    st.rerun()
    
    else:
        st.title("My Profile")
        
        # Displaying User Info in a clean format
        with st.container():
            st.info(f"👤 **Customer ID:** `{st.session_state['customer_id']}`")
            st.write(f"**Name:** {st.session_state['username']}")
            st.write("**Status:** Active Customer")
            st.write(f"**Items in Cart:** {len(st.session_state['cart'])}")
        
        st.write("---")
        if st.button("Logout", type="primary"):
            st.session_state['logged_in'] = False
            st.session_state['username'] = ""
            st.session_state['customer_id'] = "" # Reset ID on logout
            st.session_state['cart'] = [] 
            st.rerun()

# --- PAGE 5: BECOME A PARTNER ---
elif page == "Become a Partner":
    st.title("Join QuickFix as a Professional")
    st.write("Fill out the form below to register your skills and start earning.")
    
    with st.form("partner_form"):
        name = st.text_input("Full Name")
        phone = st.text_input("Phone Number")
        skill = st.selectbox("Your Profession", ["Electrician", "Plumber", "Cleaner", "AC Technician", "Beautician"])
        experience = st.slider("Years of Experience", 0, 20, 2)
        city = st.text_input("City")
        
        submit_partner = st.form_submit_button("Submit Application")
        
        if submit_partner:
            partner_id = f"PRT-{random.randint(1000, 9999)}"
            st.success(f"Thank you, {name}! Your partner ID is {partner_id}. Our team will contact you soon.")