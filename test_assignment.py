# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Load your dataset (replace 'your_dataset.csv' with your actual file)
# df = pd.read_csv('your_dataset.csv')

data = {
        'Age': [25, 30, 35],
        'StudyHour': [1, 3, 5],
        'PartTimeHour': [0.2, 1, 0.9],
        'CGPA': [3.55, 2.55, 4.00],
        }

df = pd.DataFrame(data)

# 1. Target Class Transformation
# Assuming your target attribute is 'CGPA'
# bins = [0, 2, 2.25, 2.99, 4]
# labels = ['Fail', 'Third class', 'Second class', 'First class']
# df['CGPA_Category'] = pd.cut(df['CGPA'], bins=bins, labels=labels, include_lowest=True)

# 2. Data Preprocessing
# i. Handle Null Values
imputer = SimpleImputer(strategy='mean')
df[['StudyHour', 'PartTimeHour']] = imputer.fit_transform(df[['StudyHour', 'PartTimeHour']])

# ii. Encoding
# If you have nominal values that need encoding, use LabelEncoder or One-Hot Encoding.

# iii. Outlier Detection (using Z-Score for example)
z_scores = np.abs((df - df.mean()) / df.std())
df_no_outliers = df[(z_scores < 3).all(axis=1)]

# iv. Homogeneous Data
# Ensure all values are in the same format if necessary.

# v. Remove Unnecessary Data
# Remove irrelevant or redundant data if any.

# vi. Normalization
scaler = StandardScaler()
df[['StudyHour', 'PartTimeHour']] = scaler.fit_transform(df[['StudyHour', 'PartTimeHour']])

# 3. Data Visualization
# i. Correlation
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# ii. Boxplots
for column in df.columns:
    sns.boxplot(x='CGPA', y=column, data=df)
    plt.title(f'Boxplot of {column} by CGPA Category')
    plt.show()

#Classification Models
# Split the data into features (X) and target (y)
X = df.drop('CGPA',axis=1)
y = df['CGPA']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
rf_model = RandomForestClassifier()
knn_model = KNeighborsClassifier()
nn_model = MLPClassifier()

# Fit models
rf_model.fit(X_train, y_train)
knn_model.fit(X_train, y_train)
nn_model.fit(X_train, y_train)

# Model Comparison
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    return accuracy, precision, recall, f1

#  Comparison Table
models = [rf_model, knn_model, nn_model]

metrics_columns = ['Model', 'Accuracy', 'Precision', 'Recall', 'F1_Score']
metrics_df = pd.DataFrame(columns=metrics_columns)

for model in models:
    model_name = str(model).split('(')[0]
    accuracy, precision, recall, f1_score = evaluate_model(model, X_test, y_test)
    new_row =  {'Model': model_name, 'Accuracy': accuracy, 'Precision': precision, 'Recall': recall, 'F1_Score': f1_score}
    metrics_df.loc[len(metrics_df)] = new_row
    
    # metrics_df.append(new_row, ignore_index=True)


print(metrics_df)

