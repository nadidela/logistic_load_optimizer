import pandas as pd
import numpy as np
import re
import time

# load dataset
file_path = "Amazon_Products.csv"

df = pd.read_csv(
    file_path,
    engine="python",
    on_bad_lines="skip"
)

print("Original Dataset Shape:", df.shape)

# selecting relevant columns
columns_needed = [
    'product_name',
    'price',
    'product_information',
    'amazon_category_and_sub_category',
    'average_review_rating'
]

columns_needed = [col for col in columns_needed if col in df.columns]
df = df[columns_needed].copy()

print("After Column Selection:", df.shape)

#cleaning the price column
def clean_price(price):
    if pd.isna(price):
        return np.nan

    price = str(price)
    match = re.search(r'[\d,.]+', price)

    if match:
        return float(match.group(0).replace(',', ''))

    return np.nan


df['price_cleaned'] = df['price'].apply(clean_price)
df.dropna(subset=['price_cleaned'], inplace=True)

#extracting product weights
def extract_weight(text):
    if pd.isna(text):
        return np.nan

    text = str(text).lower()

    kg_match = re.search(r'(\d+\.?\d*)\s*kg', text)
    if kg_match:
        return float(kg_match.group(1)) * 1000

    g_match = re.search(r'(\d+\.?\d*)\s*g', text)
    if g_match:
        return float(g_match.group(1))

    lb_match = re.search(r'(\d+\.?\d*)\s*lb', text)
    if lb_match:
        return float(lb_match.group(1)) * 453.592

    oz_match = re.search(r'(\d+\.?\d*)\s*oz', text)
    if oz_match:
        return float(oz_match.group(1)) * 28.3495

    return np.nan

# cleaning data
df['weight_grams'] = df['product_information'].apply(extract_weight)
df.dropna(subset=['weight_grams'], inplace=True)

df = df[
    (df['price_cleaned'] > 0) &
    (df['weight_grams'] > 0) &
    (df['weight_grams'] <= 50000)
].copy()

df['weight_grams'] = df['weight_grams'].round().astype(int)

# Avoid extremely tiny item weights
df['weight_grams'] = df['weight_grams'].clip(lower=10)

df['product_name'] = (
    df['product_name']
    .astype(str)
    .str.strip()
    .str.replace(r'\s+', ' ', regex=True)
)

print("After Cleaning:", df.shape)

#sample the data
df = df.sample(n=min(5000, len(df)), random_state=42).copy()

print("After Sampling:", df.shape

#preparing Knapsack
weights = df['weight_grams'].astype(int).tolist()
values = df['price_cleaned'].astype(int).tolist()
products = df['product_name'].tolist()

#knapsack
def knapsack_optimized(weights, values, capacity):

    n = len(weights)

    dp = [0] * (capacity + 1)
    keep = [[False] * (capacity + 1) for _ in range(n)]

    for i in range(n):

        w = weights[i]
        v = values[i]

        if w > capacity:
            continue

        for cap in range(capacity, w - 1, -1):

            if dp[cap - w] + v > dp[cap]:
                dp[cap] = dp[cap - w] + v
                keep[i][cap] = True

    selected_items = []
    total_weight = 0
    cap = capacity

    for i in range(n - 1, -1, -1):

        if keep[i][cap]:
            selected_items.append(i)
            total_weight += weights[i]
            cap -= weights[i]

    selected_items.reverse()

    return dp[capacity], total_weight, selected_items

#greedy baseline
def greedy_baseline(weights, values, capacity):

    items = []

    for i in range(len(weights)):
        items.append((values[i], i))

    items.sort(reverse=True)

    total_value = 0
    total_weight = 0
    selected = []

    for value, i in items:

        if total_weight + weights[i] <= capacity:
            selected.append(i)
            total_weight += weights[i]
            total_value += values[i]

    return total_value, total_weight, selected

#user input
capacity = int(input("\nEnter Container Capacity in grams: "))

#run dynamic programming
start_time = time.time()

optimal_value, optimal_weight, selected_items = knapsack_optimized(
    weights,
    values,
    capacity
)

dp_time = time.time() - start_time

#greedy baseline
start_time = time.time()

baseline_value, baseline_weight, baseline_selected = greedy_baseline(
    weights,
    values,
    capacity
)



baseline_time = time.time() - start_time
