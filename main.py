from src.mlProject.pipeline.train_pipeline import TrainPipeline

if __name__ == "__main__":

    print("Starting Retail Demand Forecasting Pipeline")

    pipeline = TrainPipeline()
    pipeline.run_pipeline()

    print("Pipeline Finished Successfully")