import os

project_name = "Retail_Demand_Forecasting"

folders = [
    f"{project_name}/src/mlProject/components",
    f"{project_name}/src/mlProject/pipeline",
    f"{project_name}/notebook",
    f"{project_name}/data",
    f"{project_name}/artifacts",
    f"{project_name}/logs"
]

files = [
    f"{project_name}/src/mlProject/components/data_ingestion.py",
    f"{project_name}/src/mlProject/components/data_transformation.py",
    f"{project_name}/src/mlProject/components/model_trainer.py",
    f"{project_name}/src/mlProject/components/model_evaluation.py",

    f"{project_name}/src/mlProject/pipeline/train_pipeline.py",
    f"{project_name}/src/mlProject/pipeline/predict_pipeline.py",

    f"{project_name}/src/mlProject/utils.py",
    f"{project_name}/src/mlProject/logger.py",

    f"{project_name}/src/mlProject/__init__.py",
    f"{project_name}/src/mlProject/components/__init__.py",
    f"{project_name}/src/mlProject/pipeline/__init__.py",

    f"{project_name}/main.py",
    f"{project_name}/requirements.txt",
    f"{project_name}/README.md",
    f"{project_name}/.gitignore"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    with open(file, "w") as f:
        pass

print("Project structure created successfully!")