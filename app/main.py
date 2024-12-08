import streamlit as st
import pandas as pd

# Set page title and layout
st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

# Title and description
st.title("Solar Data Dashboard")
st.write("Explore solar data trends and insights interactively.")

# Load the solar data
@st.cache_data
def load_data(filepath):
    return pd.read_csv(filepath)

data = load_data(r"C:\Users\lenovo\Desktop\AI\10Academy\week_0\Task_1\data\solar_data.csv")

# Add a slider to filter data by GHI
st.sidebar.header("Filters")
ghi_threshold = st.sidebar.slider(
    "Filter by GHI", 
    min_value=0, 
    max_value=int(data['GHI'].max()), 
    value=100
)

filtered_data = data[data['GHI'] > ghi_threshold]

# Display filtered data
st.subheader("Filtered Solar Data")
st.write(filtered_data)

# Add date range filter
st.sidebar.subheader("Date Range Filter")
date_range = st.sidebar.date_input("Select date range", [])
if date_range:
    start_date, end_date = pd.to_datetime(date_range)
    filtered_data = filtered_data[(
        filtered_data['Date'] >= start_date) & 
        (filtered_data['Date'] <= end_date)
    ]

# Show GHI trends over time
st.subheader("GHI Trends Over Time")
st.line_chart(filtered_data[['Date', 'GHI']].set_index('Date'))

# Add a correlation heatmap
st.subheader("Correlation Heatmap")
if st.checkbox("Show Heatmap"):
    import seaborn as sns
    import matplotlib.pyplot as plt

    st.write("Visualizing correlations between features.")
    # Drop non-numeric columns (e.g., 'Date') before calculating correlations
    numeric_data = filtered_data.select_dtypes(include=['number'])

    corr_matrix = numeric_data.corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# Add radial plot for wind direction and speed
st.subheader("Wind Analysis")
if st.checkbox("Show Wind Radial Plot"):
    import plotly.express as px

    fig = px.scatter_polar(
        filtered_data, 
        r='WS', 
        theta='WD', 
        title="Wind Speed vs. Wind Direction"
    )
    st.plotly_chart(fig)
