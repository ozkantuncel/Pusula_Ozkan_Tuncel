import matplotlib.pyplot as plt
import seaborn as sns
from .utlils import plot_top_drugs

class Visualizer:
    def __init__(self, data):
        self.data = data

    def plot_missing_data(self):
        plt.figure(figsize=(12, 6))
        sns.heatmap(self.data.isnull(), cbar=False, cmap='viridis')
        plt.title('Missing Data Heatmap')
        plt.show()


    def plot_class_distribution(self, column):
        plt.figure(figsize=(8, 6))
        sns.countplot(x=self.data[column], palette="Set2")
        plt.title(f"Distribution of {column}")
        plt.xticks(rotation=90)
        plt.show()

    def plot_correlation_matrix(self):
        plt.figure(figsize=(10, 8))
        sns.heatmap(self.data.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
        plt.title("Correlation Matrix")
        plt.show()


    def plot_bar_chart(self, column):
        plt.figure(figsize=(10, 6))
        self.data[column].value_counts().plot(kind='bar')
        plt.xlabel(column)
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_gender_analysis(self):
        plt.figure(figsize=(15, 10))
        sns.boxplot(x='Yan_Etki', y='Kilo', hue='Cinsiyet', data=self.data, palette='Set2')
        plt.title('Cinsiyet ve Yan Etkiye Göre Kilo Dağılımı')
        plt.xlabel('Yan Etkiler', fontsize=8)  
        plt.ylabel('Kilo')
        plt.xticks(fontsize=8, rotation=90) 
        plt.tight_layout()
        plt.show()
    
    def plot_drug_side_effect_heatmap(self):
        pivot = self.data.pivot_table(index='Ilac_Adi', columns='Yan_Etki', aggfunc='size', fill_value=0)
        plt.figure(figsize=(16, 12))
        sns.heatmap(pivot, cmap='YlOrRd')
        plt.title('İlaç-Yan Etki İlişki Haritası')
        plt.xlabel('Yan Etkiler', fontsize=10)  
        plt.ylabel('İlaçlar')
        plt.xticks(fontsize=8, rotation=90) 
        plt.tight_layout()
        plt.show()

    def plot_blood_weight_analysis(self):
        plt.figure(figsize=(15, 10))
        sns.boxplot(x='Yan_Etki', y='Kilo', hue='Kan Grubu', data=self.data, palette='coolwarm')
        plt.title('Kan Grubu ve Yan Etkiye Göre Kilo Dağılımı')
        plt.xlabel('Yan Etki')
        plt.ylabel('Kilo')
        plt.xticks(fontsize=8, rotation=90) 
        plt.tight_layout()
        plt.show()

    def plot_blood_weight_drug_analysis(self):
        top_drugs = plot_top_drugs(self.data) 
        filtered_data = self.data[self.data['Ilac_Adi'].isin(top_drugs)] 

        plt.figure(figsize=(15, 10))
        sns.countplot(x='Ilac_Adi', hue='Cinsiyet', data=filtered_data, palette='coolwarm')
        plt.title('İlaç Adını Kullanan Kişilerin Cinsiyete Göre Dağılımı (En Sık 15 İlaç)')
        plt.xlabel('İlaç Adı')
        plt.ylabel('Kullanıcı Sayısı')
        plt.xticks(fontsize=8, rotation=90) 
        plt.tight_layout()
        plt.show()