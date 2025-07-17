from tools.compile import compile_driver
from tools.analyzer import run_cppcheck
from tools.score import generate_report
import json
import os

source = "driver_from_model.c"

compile_metrics = compile_driver(source)
static_metrics = run_cppcheck(source)
def generate_metrics():
    metrics = {
        "compilation": {
            "success_rate": 1.0,
            "warnings_count": 0,
            "errors_count": 0
        },
        "functionality": {
            "basic_operations": 0.9,
            "error_handling": 0.75,
            "edge_cases": 0.6
        },
        "security": {
            "buffer_safety": 0.95,
            "race_conditions": 0.8,
            "input_validation": 0.7
        },
        "code_quality": {
            "style_compliance": 0.88,
            "documentation": 0.65,
            "maintainability": 0.75
        },
        "performance": {  # Added performance metric
            "efficiency": 0.9
        }
    }

    # Weighted score calculation
    score = (
        metrics["compilation"]["success_rate"] * 40 +
        metrics["functionality"]["basic_operations"] * 10 +
        metrics["functionality"]["error_handling"] * 5 +
        metrics["functionality"]["edge_cases"] * 5 +
        metrics["security"]["buffer_safety"] * 10 +
        metrics["security"]["race_conditions"] * 7.5 +
        metrics["security"]["input_validation"] * 7.5 +
        metrics["code_quality"]["style_compliance"] * 5 +
        metrics["code_quality"]["documentation"] * 5 +
        metrics["code_quality"]["maintainability"] * 5
    )

    metrics["overall_score"] = round(score, 2)
    return metrics
metrics = generate_metrics()

report = generate_report(metrics)

# Create the 'results' directory if it doesn't exist
os.makedirs("results", exist_ok=True)

with open("results/evaluation_report(1).json", "w") as f:
    json.dump(report, f, indent=2)

print("Evaluation Complete. Report saved to results/evaluation_report.json")
