import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Create Sample Dataset
data = {
    'Age': [63, 37, 41, 56, 57, 57, 56, 44, 52, 57],
    'Sex': [1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    'ChestPainType': [3, 2, 1, 1, 0, 0, 1, 3, 2, 2],
    'RestingBP': [145, 130, 130, 120, 120, 140, 140, 120, 172, 150],
    'Cholesterol': [233, 250, 204, 236, 354, 192, 294, 263, 199, 168],
    'FastingBS': [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    'MaxHR': [150, 187, 172, 178, 163, 148, 153, 173, 162, 174],
    'ExerciseAngina': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    'Oldpeak': [2.3, 3.5, 1.4, 0.8, 0.6, 0.4, 1.3, 0.0, 0.5, 1.6],
    'HeartDisease': [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
}

df = pd.DataFrame(data)

# 2. Export to CSV
df.to_csv('heart_disease_sample.csv', index=False)

# 3. Visualizations

# A. Countplot: Heart Disease by Gender
sns.countplot(x='Sex', hue='HeartDisease', data=df)
plt.title('Heart Disease Count by Gender (1 = Male, 0 = Female)')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.show()

# B. Histogram: Age Distribution by Heart Disease Status
sns.histplot(data=df, x='Age', hue='HeartDisease', kde=True, bins=5)
plt.title('Age Distribution by Heart Disease Status')
plt.show()

# C. Boxplot: Cholesterol Levels by Heart Disease
sns.boxplot(x='HeartDisease', y='Cholesterol', data=df)
plt.title('Cholesterol Levels vs Heart Disease')
plt.xlabel('Heart Disease (1 = Yes, 0 = No)')
plt.ylabel('Cholesterol')
plt.show()

# D. Correlation Heatmap
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.show()
