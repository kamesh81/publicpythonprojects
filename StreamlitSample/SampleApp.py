import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("My First Streamlit App")

# Getting user input
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=120, step=1)

# Displaying the input
if name and age:
    st.write(f"Hello, {name}! You are {age} years old.")

# Creating a random data frame
data = pd.DataFrame({
    'Column 1': np.random.randn(1000),
    'Column 2': np.random.randn(1000)
})

# Plotting the data
st.line_chart(data)

# Checkbox to show/hide the data
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data)

# Slider to select a range of values from the data
values = st.slider("Select a range of values", min_value=float(data['Column 1'].min()), max_value=float(data['Column 1'].max()), value=(float(data['Column 1'].min()), float(data['Column 1'].max())))

# Filtered data based on the slider
filtered_data = data[(data['Column 1'] >= values[0]) & (data['Column 1'] <= values[1])]

# Displaying filtered data
st.write(filtered_data)

# Plotting the filtered data
st.line_chart(filtered_data)

# Sidebar section
st.sidebar.header("About")
st.sidebar.write("This is a simple Streamlit app example. You can customize it further to fit your needs!")

# Running the app
if __name__ == "__main__":
    st.write("App is running...")
