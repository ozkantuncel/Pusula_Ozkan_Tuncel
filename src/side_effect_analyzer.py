class SideEffectAnalyzer:
    def __init__(self, data):
        self.data = data

    def most_common_side_effects(self):
        print("Most common side effects:")
        print(self.data['Yan_Etki'].value_counts().head())

    def drug_side_effect_relationship(self):
        print("\nDrug and Side Effect Relationships:")
        drug_side_effect = self.data.groupby('Ilac_Adi')['Yan_Etki'].value_counts().unstack().fillna(0)
        print(drug_side_effect.head())

    def analyze_effect_of_chronic_conditions(self):
        print("\nEffect of Chronic Conditions on Side Effects:")
        chronic_side_effects = self.data.groupby('Kronik Hastaliklarim')['Yan_Etki'].value_counts().unstack().fillna(0)
        print(chronic_side_effects.head())
    
