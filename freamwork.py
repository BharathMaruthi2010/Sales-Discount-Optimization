import pandas as pd
import numpy as np
import joblib
import random
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import os

def file():
    df = pd.read_csv("sales.csv")
    return df
df = file()

df = df.dropna(subset=["Profit", "Discount_Percent"])
df = df.fillna(0)

categorical_cols = ['Gender', 
                    'Category', 
                    'City', 
                    'Channel', 
                    'Payment_Method', 
                    'Device', 
                    'Marketing_Channel', 
                    'Season']

def cat_con(cat_cols):
    for col in cat_cols:
        if col in df.columns:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))

cat_con(categorical_cols)

features_for_cluster = ['Age', 
                        'Income', 
                        'Loyalty_Score', 
                        'Recency_Days', 
                        'Frequency_12m', 
                        'CLV_proxy']
def Clustring(feat):
    feat = [f for f in feat if f in df.columns]
    scaler = StandardScaler()
    X_cluster = scaler.fit_transform(df[feat])
    kmeans = KMeans(n_clusters=4, random_state=42)
    df["Cluster_ID"] = kmeans.fit_predict(X_cluster)

    df.to_csv("sales_data_with_clusters.csv", index=False)
    joblib.dump(kmeans, "kmeans_model.joblib")

    return df[["Customer_ID", "Cluster_ID"]].head()
Clustring(features_for_cluster)

feature_columns = ['Cluster_ID', 
                   'Discount_Percent', 
                   'Price', 
                   'Units_Sold', 
                   'Promotion_Flag', 
                   'Loyalty_Score']
def dis_prof(feat):
    
    feat = [c for c in feat if c in df.columns]
    
    X = df[feature_columns]
    y = df["Profit"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    r2 = r2_score(y_test, y_pred)
    
    print(f"🎯 Random Forest R² Score: {r2*100:.2f}%")
    
    joblib.dump(model, "random_forest_discount_profit.joblib")
    
dis_prof(feature_columns)

def Q_learning():
    print("\n🚀 Starting discount learning simulation...")

# Reload model and clustered data
    model = joblib.load("random_forest_discount_profit.joblib")
    df = pd.read_csv("sales_data_with_clusters.csv")

    ACTIONS = [0, 5, 10, 15]
    clusters = df["Cluster_ID"].unique()

# Initialize Q-table
    Q = {c: np.zeros(len(ACTIONS)) for c in clusters}

# Learning settings
    EPISODES = 7000

    ALPHA = 0.1
    EPSILON = 0.2

    for episode in range(EPISODES):
        row = df.sample(1).iloc[0]
        cluster = row["Cluster_ID"]

    # Choose action (epsilon-greedy)
        if random.random() < EPSILON:
            action_idx = random.randint(0, len(ACTIONS)-1)
        else:
            action_idx = np.argmax(Q[cluster])

    # Simulate environment (predict profit)
        test_row = row.copy()
        test_row["Discount_Percent"] = ACTIONS[action_idx]

        X_sim = pd.DataFrame([test_row])[feature_columns].fillna(0)
        reward = float(model.predict(X_sim)[0])

    # Q-value update
        old_value = Q[cluster][action_idx]
        Q[cluster][action_idx] = old_value + ALPHA * (reward - old_value)

# Extract best discount policy
    policy = []
    for c in clusters:
        best_idx = np.argmax(Q[c])
        best_discount = ACTIONS[best_idx]
        policy.append({"Cluster_ID": c, "Best_Discount": best_discount})

    policy_df = pd.DataFrame(policy)
    policy_df.to_csv("cluster_best_discounts.csv", index=False)

    print("\n✅ Learning complete! Best discounts per cluster:")
    print(policy_df)


    joblib.dump(Q,'q_table.pkl')

    if os.path.exists('q_table.pkl'):
        Q = joblib.load("q_table.pkl")
    else:
        Q = {cluster: [0]*len(ACTIONS) for cluster in clusters}

Q_learning()
