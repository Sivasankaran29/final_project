import pandas as pd
from textblob import TextBlob
import streamlit as st
import pickle

# Function to filter reviews by specific features and sentiment
def filter_reviews_by_feature(df, feature, sentiment_type):
    # Calculate sentiment polarity for the feature
    df['related_sentiment'] = df['review_text'].apply(
        lambda review: TextBlob(review).sentiment.polarity if feature.lower() in review.lower() else None
    )
    
    # Positive sentiment: prioritize higher polarity
    if sentiment_type == 'positive':
        df_filtered = df[df['related_sentiment'] > 0].copy()
    # Negative sentiment: prioritize lower polarity
    elif sentiment_type == 'negative':
        df_filtered = df[df['related_sentiment'] < 0].copy()
    # Neutral sentiment: polarity close to 0
    else:
        df_filtered = df[(df['related_sentiment'] >= -0.1) & (df['related_sentiment'] <= 0.1)].copy()

    # Add an absolute sentiment score for better ranking
    df_filtered['abs_sentiment'] = df_filtered['related_sentiment'].abs()
    
    return df_filtered

# Function to extract features and sentiment from user input
def extract_features_from_prompt(user_prompt):
    features = ['camera', 'battery', 'display', 'performance', 'design', 'mobile', 'phone',
                'RAM', 'storage', 'charger', 'processor', '5G', 'refresh rate', 'build quality']
    
    positive_phrases = ['best', 'good', 'high', 'quality', 'excellent', 'superior', 'premium']
    negative_phrases = ['worst', 'bad', 'poor', 'low', 'terrible', 'underwhelming']
    neutral_phrases = ['average', 'medium', 'normal', 'decent', 'adequate']
    
    feature_sentiment = {}
    
    for feature in features:
        if feature in user_prompt.lower():
            positive = any(phrase in user_prompt.lower() for phrase in positive_phrases)
            negative = any(phrase in user_prompt.lower() for phrase in negative_phrases)
            neutral = any(phrase in user_prompt.lower() for phrase in neutral_phrases)
            
            if positive:
                feature_sentiment[feature] = 'positive'
            elif negative:
                feature_sentiment[feature] = 'negative'
            elif neutral:
                feature_sentiment[feature] = 'neutral'

    return feature_sentiment

# Function to rank mobiles based on feature sentiment
def rank_mobiles(df, feature, sentiment_type, top_n=5):
    df_filtered = filter_reviews_by_feature(df, feature, sentiment_type)

    if sentiment_type == 'positive':
        rankings = df_filtered.groupby('product_id').agg(
            average_sentiment=('related_sentiment', 'mean')
        ).reset_index()
        sorted_rankings = rankings.sort_values(by='average_sentiment', ascending=False)
    elif sentiment_type == 'negative':
        rankings = df_filtered.groupby('product_id').agg(
            average_sentiment=('abs_sentiment', 'mean')
        ).reset_index()
        sorted_rankings = rankings.sort_values(by='average_sentiment', ascending=True)
    else:
        rankings = df_filtered.groupby('product_id').agg(
            average_sentiment=('related_sentiment', 'mean')
        ).reset_index()
        sorted_rankings = rankings.sort_values(by='average_sentiment', ascending=False)

    top_mobiles = sorted_rankings.head(top_n)['product_id'].tolist()
    return top_mobiles

# Function to generate combined rankings when multiple features are requested
def rank_mobiles_by_multiple_features(df, feature_sentiment_map, top_n=5):
    combined_rankings = pd.DataFrame()

    for feature, sentiment_type in feature_sentiment_map.items():
        feature_rankings = filter_reviews_by_feature(df, feature, sentiment_type)
        
        feature_rankings = feature_rankings.groupby('product_id').agg(
            average_sentiment=('related_sentiment', 'mean')
        ).reset_index()

        if combined_rankings.empty:
            combined_rankings = feature_rankings
        else:
            combined_rankings = pd.merge(combined_rankings, feature_rankings, on='product_id', suffixes=('', f'_{feature}'))

    combined_rankings['total_score'] = combined_rankings.filter(like='average_sentiment').sum(axis=1)
    sorted_combined_rankings = combined_rankings.sort_values(by='total_score', ascending=False)
    top_combined_mobiles = sorted_combined_rankings.head(top_n)['product_id'].tolist()

    return top_combined_mobiles

# Function to generate recommendations based on user input
def generate_recommendations(df, user_prompt, top_n=5):
    feature_sentiment = extract_features_from_prompt(user_prompt)

    if len(feature_sentiment) == 1:
        feature, sentiment_type = next(iter(feature_sentiment.items()))
        ranked_mobiles = rank_mobiles(df, feature, sentiment_type, top_n)
    else:
        ranked_mobiles = rank_mobiles_by_multiple_features(df, feature_sentiment, top_n)

    # Format each rank on a new line
    response = "\n".join([f"**Rank {i+1}:** {mobile}" for i, mobile in enumerate(ranked_mobiles)])
    
    return response

def load_data():
    with open('mobile_recommendation_model.pkl', 'rb') as f:
        df = pickle.load(f)
    return df    

# Function to display recommendations in a better format using streamlit
def main():
    # Load the data
    df = pd.read_csv('analyzed_df.csv')

    st.title("Advanced Mobile Recommendation System")
    st.write("Enter your mobile preferences below:")

    user_prompt = st.text_input("What do you want in a mobile? (e.g., 'best camera, excellent battery life, and premium display')")

    if st.button("Get Recommendations"):
        if user_prompt:
            recommendations = generate_recommendations(df, user_prompt)
            st.write("### Recommendations (Ranked):")
            # Displaying the recommendations properly formatted
            st.markdown(recommendations.replace("\n", "<br>"), unsafe_allow_html=True)
        else:
            st.write("Please enter a valid prompt.")

if __name__ == "__main__":
    main()









