"""
Generates actionable calibration charts mapping engine variables.
"""
import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_calibration_summary(data: pd.DataFrame, output_dir: str = "output"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    plt.figure(figsize=(10, 6))
    
    # Plot Engine Speed vs Exhaust Gas Temp
    plt.scatter(data['engine_speed_rpm'], data['egt_c'], c=data['lambda_sensor'], cmap='coolwarm', label='Data points')
    plt.colorbar(label='Lambda Sensor Value')
    plt.axhline(y=950.0, color='r', linestyle='--', label='Critical EGT Safety Threshold')
    
    plt.title('Engine Speed vs Exhaust Gas Temperature Mapping')
    plt.xlabel('Engine Speed (RPM)')
    plt.ylabel('EGT (°C)')
    plt.legend()
    
    output_path = os.path.join(output_dir, "calibration_mapping.png")
    plt.savefig(output_path)
    plt.close()
    print(f"[Success] Optimization visualization saved to {output_path}")
