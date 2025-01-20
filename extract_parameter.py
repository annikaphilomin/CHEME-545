def extract_parameter(unit_name, parameter_name, index):
    unit_operations_data = {
        "distillation_column": {"temperature": [150, 160, 170], "pressure": [2, 2.5, 3], "flow_rate": [100, 110, 120]},
        "reactor": {"temperature": [250, 260, 270], "pressure": [5, 5.5, 6], "residence_time": [10, 12, 14]},
        "heat_exchanger": {"temperature_in": [80, 90, 100], "temperature_out": [50, 60, 70], "flow_rate": [200, 210, 220]}
    }
    
    try:
        # Get the parameter list for the given unit_name and parameter_name
        parameter_list = unit_operations_data[unit_name][parameter_name]
        
        # Retrieve the value at the specified index
        value = parameter_list[index]
        
        # Format and return the desired string
        return f"{unit_name}_{parameter_name}_{value}"
    except (KeyError, IndexError):
        # Handle missing keys or index out of range errors
        return "Invalid input"

# Example usage
print(extract_parameter("distillation_column", "temperature", 1))  # Should return "distillation_column_temperature_160"
print(extract_parameter("reactor", "pressure", 2))  # Should return "reactor_pressure_6"
print(extract_parameter("heat_exchanger", "flow_rate", 5))  # Should return "Invalid input"
print(extract_parameter("unknown_unit", "temperature", 0))  # Should return "Invalid input"

