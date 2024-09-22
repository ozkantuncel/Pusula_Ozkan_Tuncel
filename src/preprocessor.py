from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
import pandas as pd

class Preprocessor:
    def __init__(self, data):
        self.data = data

    def fill_missing_values(self, method="mean"):
        if method == "mean":
            imputer = SimpleImputer(strategy='mean')
        elif method == "knn":
            imputer = KNNImputer(n_neighbors=5)
        else:
            raise ValueError("Unsupported imputation method.")
        
        self.data[['Kilo', 'Boy']] = imputer.fit_transform(self.data[['Kilo', 'Boy']])
        self.data.fillna('Unknown', inplace=True)

    def encode_categorical(self, method="onehot"):
        if method == "label":
            label_encoder = LabelEncoder()
            for col in self.data.select_dtypes(include=['object']).columns:
                self.data[col] = label_encoder.fit_transform(self.data[col])
        elif method == "onehot":
            self.data = pd.get_dummies(self.data, drop_first=True)
        else:
            raise ValueError("Unsupported encoding method.")

    def scale_features(self, scaling_method="standard"):
        if scaling_method == "standard":
            scaler = StandardScaler()
        else:
            raise ValueError("Unsupported scaling method.")
        
        self.data[['Kilo', 'Boy']] = scaler.fit_transform(self.data[['Kilo', 'Boy']])
        return self.data

    def remove_rare_categories(self, threshold=0.01):
        for col in self.data.select_dtypes(include=['object']).columns:
            rare_categories = self.data[col].value_counts(normalize=True)[self.data[col].value_counts(normalize=True) < threshold].index
            self.data[col] = self.data[col].apply(lambda x: 'Rare' if x in rare_categories else x)