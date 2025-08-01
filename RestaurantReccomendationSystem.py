import pandas as pd
import streamlit as st
import pickle
from sklearn.cluster import KMeans

# Load all the data

# Load the cleaned data
cleaned_df = pd.read_csv(r'D:\AIML\Swiggy RRS Project\Data\cleaned_data.csv')

# Load the encoded data
encoded_df = pd.read_csv(r'D:\AIML\Swiggy RRS Project\Data\encoded_data.csv')

# Load the cuisine column list for the selectbox from the pickle file
with open(r'D:\AIML\Swiggy RRS Project\Data\cuisine_encoder.pkl','rb+') as ef:
    cuisine_df = pickle.load(ef)

# Load the city column list for the selectbox from the pickle file
with open(r'D:\AIML\Swiggy RRS Project\Data\city_encoder.pkl','rb+') as ef:
    city_df = pickle.load(ef)



def get_recommended_restaurants(criteria, df, num_recommendations=2):

    """
        This function gets the recommended restaurants based on input criteria(city or cuisine)
        by using K-Means clustering
        Args:
            criteria: The selected city or cuisine
            df: The dataframe based on which recommendations will be calculated
            num_recommendations: The number of recommendations needed
        Returns:
        recommended_restaurants: The recommended number of restaurants based on input criteria
    """
        
    # Apply K-Means clustering
    kmeans = KMeans(n_clusters=2, random_state=0).fit(df)
    df['cluster'] = kmeans.labels_

    # Find the cluster for the given criteria
    target_criteria_cluster = df[df[criteria] == 1]["cluster"].values[0]

    # Find the similar clusters for the given criteria
    same_criteria_clusters = df[df["cluster"] == target_criteria_cluster]

    # Get the index of the recommended clusters
    recommendations_index = same_criteria_clusters[same_criteria_clusters[criteria] == 1].index.tolist()
    
    # Get the recommended data from the cleaned data set
    recommendations_df = cleaned_df.iloc[recommendations_index]
    
    # Sort the recommended data based on rating column
    recommendations_df = recommendations_df.sort_values('rating',ascending=False)

    # Get the top number of recommended data  
    recommended_restaurants = recommendations_df.head(num_recommendations)
    
    return recommended_restaurants


# Streamlit App
def main():

    st.title("Swiggy’s Restaurant Recommendation System")

    recommend_by_city = st.selectbox("Select a City:", list(city_df.columns.to_list()), index=None)

    recommend_by_cuisine = st.selectbox("Select a Cuisine:", list(cuisine_df.columns.to_list()), index=None)

    if st.button('Show Recommendation'):

        if (recommend_by_city == None) & (recommend_by_cuisine == None):
            st.subheader(f"Please select a City or Cuisine for Restaurant Recommendations")

        if recommend_by_city != None:
            st.subheader(f"Top 5 Restaurant Recommendations for the city {recommend_by_city}:")
            recommended_restaurants = get_recommended_restaurants(recommend_by_city, encoded_df, 5)
            st.dataframe(recommended_restaurants, hide_index=True)

        if recommend_by_cuisine != None:
            st.subheader(f"Top 5 Restaurant Recommendations for the cuisine {recommend_by_cuisine}:")
            recommended_restaurants = get_recommended_restaurants(recommend_by_cuisine, encoded_df, 5)
            st.dataframe(recommended_restaurants, hide_index=True)

   
main()

