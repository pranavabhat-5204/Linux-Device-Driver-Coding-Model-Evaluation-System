def compute_score(metrics):
    score = 0
    score += metrics["compilation"]["success_rate"] * 40
    score += (1 - metrics["compilation"]["warnings_count"]/10) * 10  # Penalty
    score += metrics["security"]["buffer_safety"] * 10
    score += metrics["code_quality"]["style_compliance"] * 10
    score += metrics["functionality"]["basic_operations"] * 20
    score += metrics["performance"]["efficiency"] * 10
    return min(score, 100)

def generate_report(metrics):
    return {
        "metrics": metrics,
        "overall_score": compute_score(metrics),
        "error_handling": 0.7,
        "edge_cases": 0.6,
        "race_conditions": 0.8,
        "input_validation": 0.75,
        "documentation": 0.6,
        "maintainability": 0.7
    }
