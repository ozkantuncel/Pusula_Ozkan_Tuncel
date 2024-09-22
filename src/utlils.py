

def plot_top_drugs(data, n=15):
    top_drugs = data['Ilac_Adi'].value_counts().nlargest(n).index
    return top_drugs
