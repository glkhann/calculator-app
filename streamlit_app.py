import streamlit as st
import math

st.set_page_config(page_title="Multi-Input Calculator", layout="centered")

st.title("🧮 Multi-Input Calculator")

# Select number of inputs
num_inputs = st.slider("Select number of inputs:", 1, 10, 2)

# Create input fields dynamically
inputs = []
for i in range(num_inputs):
    val = st.number_input(f"Input {i+1}", key=f"input_{i}")
    inputs.append(val)

# Buttons as columns
col1, col2, col3 = st.columns(3)
col4, col5, _ = st.columns(3)

# Result display
result = None

# Functions for calculations
def add():
    return sum(inputs)

def subtract():
    res = inputs[0]
    for v in inputs[1:]:
        res -= v
    return res

def multiply():
    res = 1
    for v in inputs:
        res *= v
    return res

def divide():
    try:
        res = inputs[0]
        for v in inputs[1:]:
            if v == 0:
                return "❌ Division by zero"
            res /= v
        return res
    except Exception as e:
        return f"Error: {e}"

def sqrt():
    if inputs[0] < 0:
        return "❌ Negative input not allowed for √"
    return math.sqrt(inputs[0])

# Button actions
if col1.button("➕ Add"):
    result = add()

if col2.button("➖ Subtract"):
    result = subtract()

if col3.button("✖️ Multiply"):
    result = multiply()

if col4.button("➗ Divide"):
    result = divide()

if col5.button("√ Square Root (First Only)"):
    result = sqrt()

# Show result
if result is not None:
    st.success(f"Result: {result}")
