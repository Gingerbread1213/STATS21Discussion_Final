# STATS21Discussion_Final

## The application developed above using Python and Streamlit is essentially a data exploration and visualization tool. Here's a step-by-step summary of its functionalities:

### File Upload: It begins by providing a mechanism for users to upload a CSV file. Streamlit's file_uploader function is used to handle this.
### Data Display: Once a file is uploaded, the CSV file is read into a pandas DataFrame and displayed in the Streamlit application. This allows users to get a preliminary look at their data.
### Data Summary: The application then provides a summary of the uploaded data. It displays the number of rows and columns, the names of columns, and a count of each data type in the DataFrame. It also provides additional statistics for numerical and categorical variables.
### Column Selection: Users can then select a specific column from a dropdown menu, populated with the DataFrame's column names.
### Data Inspection: Upon selection, the unique values in the chosen column are displayed.
### Data Analysis and Visualization: Depending on the data type of the chosen column (numerical or categorical), the application performs different analyses:
### For numerical columns, it provides a five-number summary (minimum, first quartile (25%), median (50%), third quartile (75%), and maximum), and displays a distribution plot of the column data.
### For categorical columns, it displays the proportions of each category level, and displays a bar plot showing the frequency of each category.
### In a nutshell, this Streamlit application serves as a quick, interactive tool for users to load, explore, and visualize their data, facilitating initial data analysis and understanding.
