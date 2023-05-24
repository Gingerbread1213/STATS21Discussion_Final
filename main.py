import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = None
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

if dataframe is not None:

    # Number of rows
    st.write("Number of rows:", len(dataframe))

    # Number of columns
    st.write("Number of columns:", len(dataframe.columns))

    # Print the column names
    st.write("Column names:", dataframe.columns.tolist())

    # Count number of each data type
    data_types = dataframe.dtypes
    st.write("Data types and their frequency:\n", data_types.value_counts())

    # Additional statistics
    st.write("\nAdditional Statistics:")
    st.write("Numeric Variables:")
    st.write(dataframe.select_dtypes(include=[np.number]).describe().transpose())

    st.write("\nCategorical Variables:")
    st.write(dataframe.select_dtypes(include=['object']).describe().transpose())

    option = st.selectbox('Choose a column', dataframe.columns.tolist())
    st.write('You selected:', option)

    # Display the unique values in the selected column
    unique_values = dataframe[option].unique()
    st.write('Unique values in this column:', unique_values)

    selected_column = dataframe[option]

    if np.issubdtype(selected_column.dtype, np.number):
        # If the column is numerical

        # Display the five number summary
        five_num_summary = selected_column.describe()[['min', '25%', '50%', '75%', 'max']]
        st.write("Five-number summary:", five_num_summary)

        # Distribution plot
        plt.figure(figsize=(10, 6))
        sns.histplot(data=selected_column, kde=True, color='darkblue')
        plt.title('Distribution of ' + option)
        st.pyplot(plt.gcf())  # Display the plot in Streamlit

    else:
        # If the column is categorical

        # Display the proportions of each category level
        proportions = selected_column.value_counts(normalize=True)  # Get proportions
        st.write("Proportions of each category level:", proportions)

        # Barplot
        plt.figure(figsize=(10, 6))
        sns.countplot(x=selected_column, palette='viridis')
        plt.title('Barplot of ' + option)
        plt.xticks(rotation=45)
        st.pyplot(plt.gcf())  # Display the plot in Streamlit
