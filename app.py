import streamlit as st

# Function to check prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Streamlit UI
st.set_page_config(page_title="Prime Number Finder", page_icon="🔢", layout="centered")

# Add a colorful title
st.markdown(
    """
    <h1 style='text-align: center; color: #FF5733;'>🔍 Let's Find Prime Numbers</h1>
    <p style='text-align: center; color: #2980B9;'>Enter a range and I will show you all the prime numbers inside it!</p>
    """,
    unsafe_allow_html=True
)

# User input for range
col1, col2 = st.columns(2)

with col1:
    start = st.number_input("Enter start of range", min_value=0, value=1)

with col2:
    end = st.number_input("Enter end of range", min_value=1, value=50)

# Button
if st.button("Find Prime Numbers 🚀"):
    if start >= end:
        st.error("⚠️ End of range must be greater than start.")
    else:
        primes = [num for num in range(start, end + 1) if is_prime(num)]
        
        if primes:
            st.success(f"✅ Prime numbers between {start} and {end}:")
            st.write(primes)
        else:
            st.warning(f"No prime numbers found between {start} and {end}.")