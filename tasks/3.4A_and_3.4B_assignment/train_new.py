import fire
import mlflow
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score, mean_squared_error
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import datasets

def setup_pipeline(k):
    regression_model = LogisticRegression()
    pipe = make_pipeline( regression_model)
    return pipe


def track_with_mlflow(model, x_test, y_test, mlflow, model_metadata):
    
    y_pred = model.predict(x_test)
    
    mlflow.log_params(model_metadata)
    mlflow.log_metric("f1_score", f1_score(y_test, y_pred,average="micro"))
    mlflow.log_metric("accuracy", model.score(x_test, y_test))
    mlflow.sklearn.log_model(model, "logisticRegression", registered_model_name="sklearn_classification_assignment")

def main(file_name: str, max_k: int):
    breast_cancer_df= datasets.load_breast_cancer()
    
    x=breast_cancer_df.data[:,:2]
    y=breast_cancer_df.target
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,shuffle=True)
    # let's check some other k
    k_list = range(1, max_k)

    for k in k_list:
        with mlflow.start_run():
            regression_pipe = setup_pipeline(k)
            regression_pipe.fit(x_train, y_train)
            model_metadata = {"k": k}
            track_with_mlflow(regression_pipe, x_test, y_test, mlflow, model_metadata)


if __name__ == "__main__":
    fire.Fire(main)