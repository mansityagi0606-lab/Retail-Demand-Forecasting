from src.mlProject.components.data_ingestion import DataIngestion
from src.mlProject.components.data_transformation import DataTransformation
from src.mlProject.components.model_trainer import ModelTrainer
from src.mlProject.components.model_evaluation import ModelEvaluation


class TrainPipeline:

    def run_pipeline(self):

        # Data Ingestion
        ingestion = DataIngestion()
        train_path, test_path = ingestion.initiate_data_ingestion()

        # Data Transformation
        transform = DataTransformation()
        X_train, X_test, y_train, y_test = transform.initiate_data_transformation(
            train_path, test_path
        )

        # Model Training
        trainer = ModelTrainer()
        model = trainer.initiate_model_trainer(X_train, y_train)

        # Evaluation
        evaluator = ModelEvaluation()
        evaluator.evaluate_model(model, X_test, y_test)