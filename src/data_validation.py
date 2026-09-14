def check_missing_values(data):

    missing = data.isnull().sum()

    return missing

def check_risk_range(data,min_value=0,max_value=1):
    invalid = data[
        (data["risk"] < min_value)|
        (data["risk"] > max_value)
    ]

    return invalid

def check_required_columns(data, required_columns): #遍历required_columns里面每一个column，如果这个column不在data.columns里面，就把它放进新列表。
    missing_columns = [
        column
        for column in required_columns
        if column not in data.columns
    ]

    return missing_columns

import pandas as pd

def check_numeric_columns(data,numeric_columns):
    invalid_columns = []

    for column in numeric_columns:
        if not pd.api.types.is_numeric_dtype(data[column]):
            invalid_columns.append(column)

    return invalid_columns

def validate_data(data):
    required_columns = [
        "city",
        "risk",
        "population"
    ]

    numeric_columns = [
        "risk",
        "population"
    ]

    validation_result = {
        "missing_columns": check_required_columns(data,required_columns),
        "missing_values": check_missing_values(data),
        "invalid_numeric_columns":check_numeric_columns(data,numeric_columns),
        "invalid_risk_rows": check_risk_range(data)
    }

    return validation_result

def validation_passed(validation_result):
    if validation_result["missing_columns"]:
        return False

    if validation_result["invalid_numeric_columns"]:
        return False

    if not validation_result["invalid_risk_rows"].empty:
        return False

    return True
