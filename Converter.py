import streamlit as st

# Streamlit page settings (must be first Streamlit command)
st.set_page_config(page_title="🌍 Unit Converter", page_icon="🔄")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f8f9fa;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background: linear-gradient(135deg, #6a11cb, #2575fc);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        color: white;
    }
    h1 {
        text-align: center;
        font-size: 32px;
        color: #ffffff;
    }
    .stSidebar {
        background-color: #2c3e50 !important;
        color: white;
    }
    .stButton>button {
        background-color: #28a745;
        color: white;
        border-radius: 8px;
        font-size: 18px;
        padding: 10px;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #218838;
    }
    .stSuccess {
        background-color: #28a745 !important;
        color: white;
        padding: 10px;
        border-radius: 8px;
    }
    .stError {
        background-color: #dc3545 !important;
        color: white;
        padding: 10px;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Unit conversion functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000,
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28084, 'Inches': 39.3701
    }
    return (value / length_units[from_unit]) * length_units[to_unit] if from_unit and to_unit else None

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilogram': 1, 'Grams': 1000, 'Milligrams': 1000000,
        'Pounds': 2.20462, 'Ounces': 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit] if from_unit and to_unit else None

def temp_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == 'Celsius':
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else None
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else None
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else None
    return None

# App title and description
st.markdown("<h1>🔄 Unit Converter using Python and Streamlit </h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature! 📏⚖️🌡️")

# Sidebar for selecting conversion type
conversion_type = st.sidebar.selectbox("📌 Choose Conversion Type", ["Length", "Weight", "Temperature"])

# Unit lists
length_units = ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"]
weight_units = ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"]
temp_units = ["Celsius", "Fahrenheit", "Kelvin"]

# Initialize unit options based on selection
units = length_units if conversion_type == "Length" else weight_units if conversion_type == "Weight" else temp_units

# Input Fields
value = st.number_input("✏️ Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

# Select "From" and "To" units with valid default indices
with col1:
    from_unit = st.selectbox("🔍 From", units, index=0)
with col2:
    to_unit = st.selectbox("🎯 To", units, index=1)

# Button to perform conversion
if st.button("🤖 Convert"):
    if from_unit and to_unit and value is not None:
        if conversion_type == "Length":
            result = length_converter(value, from_unit, to_unit)
        elif conversion_type == "Weight":
            result = weight_converter(value, from_unit, to_unit)
        elif conversion_type == "Temperature":
            result = temp_converter(value, from_unit, to_unit)
        
        if result is not None:
            st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit} 🎉")
        else:
            st.error("❌ Invalid Conversion")
    else:
        st.warning("⚠️ Please enter a valid value and select units.")

# Footer
st.markdown("<div style='text-align: center;'>🚀 Created with ❤️ by Nazia Siraj</div>", unsafe_allow_html=True)
