"""
The overarching wrapper executable script that links the parsing, calibration analytics, and graphical engine pipelines together.
"""
from src.data_parser import CalibrationDataParser
from src.calibration_engine import CalibrationEngine
from src.visualization import plot_calibration_summary
import os

def run_pipeline():
    print("=== Starting Automotive Calibration Automation Pipeline ===")
    
    # Define filepaths
    raw_data_path = os.path.join("data", "raw", "wltp_test_log_raw.csv")
    config_path = os.path.join("config", "calibration_limits.json")
    processed_dir = os.path.join("data", "processed")
    
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)

    # 1. Parse and clean raw engine data
    parser = CalibrationDataParser(raw_data_path)
    clean_df = parser.load_and_clean_data()
    clean_df.to_csv(os.path.join(processed_dir, "clean_calibration_data.csv"), index=False)
    print("[1/3] Parsing Complete: Sensor signals isolated and cleaned.")

    # 2. Analyze thresholds and run automated Root Cause Analysis
    engine = CalibrationEngine(config_path)
    anomalies = engine.analyze_homologation_risks(clean_df)
    recommendations = engine.generate_calibration_recommendations(anomalies)
    
    print("[2/3] Analysis Complete: Homologation safety checks executed.")
    for rec in recommendations:
        print(f" -> {rec}")

    # 3. Generate engine data visual report
    plot_calibration_summary(clean_df)
    print("[3/3] Report Generation Complete. Pipeline Finished successfully.")

if __name__ == "__main__":
    run_pipeline()
  
