from database import get_connection
def add_risk_level(data):

    def classify_risk(risk):

        if risk >= 0.8:
            return "高风险"
        elif risk >= 0.6:
            return "中风险"
        else:
            return "低风险"

    data["risk_level"] = data["risk"].apply(classify_risk)

    return data



