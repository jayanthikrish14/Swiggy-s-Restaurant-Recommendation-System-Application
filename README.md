# Swiggy’s Restaurant Recommendation System Application

This is a Streamlit application which recommends restaurants to users based on input criteria such as city and cuisine preferences. The recommendations are generated using KMeans clustering and are displayed in the application.

## Installation

To install the project the following packages are needed to be imported(if not already present):

- pandas
- pickle
- sklearn.preprocessing - MultiLabelBinarizer
- sklearn.cluster - KMeans
- streamlit

To install packages run command on Windows: 
python -m pip install <Package Name>

# Execution / Usage

### 1. Data cleaning and Preprocessing:

  #### 1. Clean the data given in the 'swiggy.csv' file by:
  
      Removing duplicate values
      Handling missing/null values
      Removing irrelevant columns
      Then save the cleaned data in a csv file - cleaned_data.csv
    These steps are done in DataCleaning.ipynb file

  #### 2. Preprocess the cleaned data by:
  
      Dropping the columns not required for pre processing
      Convert the non-numeric columns to numeric to encode
      Encode the 'city' column using One-Hot Encoding
      Create pickle file for city encoded data city_encoder.pkl
      Encode the 'cuisine' column MultiLabelBinarizer
      Create pickle file for city encoded data cuisine_encoder.pkl
      Save all the encoded data in a csv file - encoded_data.csv
  
    These steps are done in DataPreprocessing.ipynb file

#### To run the file:
Run the cells one by one in DataCleaning.ipynb and DataPreprocessing.ipynb files

### 2. Swiggy’s Restaurant Recommendation System Streamlit Application:

  This App contains two Criteria:
  
  #### 1. City:
    Lets users to select city criteria that they need and click 'Show Reccomendation' button which will display the 
    top 5 restaurants recommended by the system based on the selected city.
  
  #### 2. Cuisine: 
    Lets users to select cuisine criteria that they need and click 'Show Reccomendation' button which will display the 
    top 5 restaurants recommended by the system based on the selected cuisine.

#### To run the application:
  From windows command prompt run the command: 
  streamlit run <path of the file> RestaurantReccomendationSystem.py
