# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GH1eT5taoYcx0C4-ESkSlrjEjcpGVB45
"""

import numpy as np # linear algebra
import pandas as pd # data processing

import os

desired_filename = "Titanic-Dataset.csv"

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        if filename == desired_filename:
            print(os.path.join(dirname, filename))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 200)
pd.set_option("display.float_format", lambda x: "%.5f" % x)

from sklearn.metrics import (f1_score,accuracy_score,recall_score,precision_score,confusion_matrix,roc_auc_score,classification_report,precision_recall_curve)
from sklearn import metrics
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn import tree

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("/Titanic-Dataset.csv")

df.head(10)

print('There are',df.shape[0] ,'rows and',len(df.axes[1]),'columns')

df.info()

df.isnull().sum()

df.duplicated().sum()

df.describe(include="all")

f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={'height_ratios': (.15, .85)}, figsize=(10, 6))
sns.set_style("darkgrid")

# Add a graph in each part
sns.boxplot(data=df, x="Age", ax=ax_box)
sns.histplot(data=df, x="Age", kde=True, ax=ax_hist)
ax_box.set(xlabel="Age")
plt.xlabel("Age(years)")

plt.show()

sns.set_theme(style="whitegrid")
sns.histplot( df, x="Age", hue="Survived", multiple="dodge")
plt.xticks(rotation=90)
plt.xlabel("Age")
plt.ylabel("Pasanger Count")
plt.title("Survival based on Age")
plt.show()

sns.violinplot(data=df, x='Survived', y= "Age" , inner='quartile')
plt.title("Survival Based on Age")
plt.xlabel("Survied (No = 0 or Yes = 1)")
plt.ylabel("Age(yrs)")

plt.show()

sns.set_theme(style="whitegrid")
sns.histplot( df, x="Sex", hue="Survived", multiple="dodge")
plt.xticks(rotation=90)
plt.xlabel("Age")
plt.ylabel("Pasanger Count")
plt.title("Sex Distribution by Age")
plt.show()

sns.violinplot(data=df, x='Sex', y= "Survived" , inner='quartile')
plt.title("Survival Based on Sex Distribution")
plt.xlabel("Survaved")
plt.ylabel("Survived (Yes = 1 or No = 0)")

plt.show()

f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={'height_ratios': (.15, .85)}, figsize=(10, 6))
sns.set_style("darkgrid")

# Add a graph in each part
sns.boxplot(data=df, x="Fare", ax=ax_box)
sns.histplot(data=df, x="Fare", kde=True, ax=ax_hist)
ax_box.set(xlabel="Fare")
plt.xlabel("Fare Price ($)")

plt.show()



sns.set_theme(style="whitegrid")
sns.histplot( df, x="Fare", hue="Survived", multiple="dodge")
plt.xticks(rotation=90)
plt.xlabel("Fare ($)")
plt.ylabel("Pasanger Count")
plt.title("Survival based on Fare")
plt.show()

sns.violinplot(data=df, x='Survived', y= "Fare" , inner='quartile')
plt.title("Survival Based on Fare")
plt.xlabel("Survied (No = 0 or Yes = 1)")
plt.ylabel("Fare ($)")

plt.show()

sns.violinplot(data=df, y='Survived', x= "SibSp" , inner='quartile')
plt.title("Survival Based Numbers Family members")
plt.xlabel("Family members")
plt.ylabel("Survied (No = 0 or Yes = 1)")

plt.show()

sns.violinplot(data=df, y='Survived', x= "Parch" , inner='quartile')
plt.title("Survival Based on Parch")
plt.xlabel("Parch")
plt.ylabel("Survied (No = 0 or Yes = 1)")

plt.show()