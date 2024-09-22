from src.data_loader import DataLoader
from src.eda import EDA
from src.preprocessor import Preprocessor
from src.visualizer import Visualizer
from src.side_effect_analyzer import SideEffectAnalyzer

def main():
    # Data Loading
    data_loader = DataLoader('data/raw/side_effect_data_1.xlsx')
    df = data_loader.load_data()

    # EDA
    eda = EDA(df)
    eda.basic_info()
    eda.missing_values()


    # Visualization
    visualizer = Visualizer(df) 
    visualizer.plot_missing_data()
    visualizer.plot_class_distribution('Yan_Etki')
    visualizer.plot_gender_analysis() 
    visualizer.plot_blood_weight_analysis()
    visualizer.plot_blood_weight_drug_analysis()
    visualizer.plot_drug_side_effect_heatmap()
   

    preprocessor = Preprocessor(df)
    preprocessor.fill_missing_values(method="knn")
    preprocessor.encode_categorical(method="label")
    preprocessor.remove_rare_categories(threshold=0.05)
    processed_data = preprocessor.scale_features(scaling_method="standard")

    # Correlation Matrix
    visualizer = Visualizer(processed_data) 
    visualizer.plot_correlation_matrix()


    # Side Effect Analysis
    side_effect_analyzer = SideEffectAnalyzer(processed_data)
    side_effect_analyzer.most_common_side_effects()
    side_effect_analyzer.drug_side_effect_relationship()
    side_effect_analyzer.analyze_effect_of_chronic_conditions()


if __name__ == "__main__":
    main()