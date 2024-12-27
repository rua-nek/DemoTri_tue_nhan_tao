import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import NearestNeighbors

# Load datasets
print("Loading datasets...")
products = pd.read_csv('data/products.csv')
purchase_history = pd.read_csv('data/purchase_history.csv')
product_views = pd.read_csv('data/product_views.csv')
print("Datasets loaded successfully.")

# Merge datasets
print("Merging datasets...")
purchase_data = pd.merge(purchase_history, products, on='product_id')
view_data = pd.merge(product_views, products, on='product_id')
data = pd.concat([purchase_data, view_data])
print("Datasets merged successfully.")

# Encode categorical variables
print("Encoding categorical variables...")
le_user = LabelEncoder()
le_product = LabelEncoder()
data['user_id'] = le_user.fit_transform(data['user_id'])
data['product_id'] = le_product.fit_transform(data['product_id'])
print("Categorical variables encoded successfully.")

# Prepare data for training
print("Preparing data for training...")
X = data[['user_id', 'product_id']]
y = data['product_id']
print("Data prepared successfully.")

# Split data into training and testing sets
print("Splitting data into training and testing sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Data split successfully.")

# Build and train the recommendation model
print("Building and training the recommendation model...")
model = NearestNeighbors(n_neighbors=3, algorithm='auto')
model.fit(X_train)
print("Model trained successfully.")

# Evaluate the model
print("Evaluating the model...")
def evaluate_model(model, X_test, y_test):
    correct_recommendations = 0
    total_recommendations = 0
    for user_id in X_test['user_id'].unique():
        user_data = X_test[X_test['user_id'] == user_id]
        distances, indices = model.kneighbors(user_data, n_neighbors=3)
        recommended_product_ids = indices.flatten()
        # Filter out invalid product ids
        valid_recommended_product_ids = [pid for pid in recommended_product_ids if pid in le_product.classes_]
        actual_product_ids = y_test[X_test['user_id'] == user_id]
        correct_recommendations += sum([1 for product_id in valid_recommended_product_ids if product_id in actual_product_ids])
        total_recommendations += len(valid_recommended_product_ids)
    accuracy = correct_recommendations / total_recommendations
    return accuracy

accuracy = evaluate_model(model, X_test, y_test)
print(f'Model accuracy: {accuracy}')

# Function to make recommendations
def recommend_products(user_id, n_recommendations=3):
    user_encoded = le_user.transform([user_id])
    user_data = X[X['user_id'] == user_encoded[0]]
    distances, indices = model.kneighbors(user_data, n_neighbors=n_recommendations)
    recommended_product_ids = indices.flatten()
    # Filter out invalid product ids
    valid_recommended_product_ids = [pid for pid in recommended_product_ids if pid in le_product.classes_]
    recommended_products = products[products['product_id'].isin(valid_recommended_product_ids)]
    return recommended_products

# Example usage
user_id = 1
recommendations = recommend_products(user_id)
print(f'Recommendations for user {user_id}:')
print(recommendations)
