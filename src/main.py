from sql_query import load_city_risk_data
from analysis import add_risk_level
from data_validation import validate_data, validation_passed



data = load_city_risk_data()

validation_result =  validate_data(data)

if validation_passed(validation_result):
    print("数据验证通过\n")
    print(data,"\n")

    result = add_risk_level(data)

    result .to_csv ("../output/city_risk_result.csv",index=False,encoding="utf-8-sig")

else:
    print("数据验证失败")
    print(validation_result,"\n")