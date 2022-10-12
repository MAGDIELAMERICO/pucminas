import pandas as pd
from airflow.decorators import dag, task
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta

URL = "https://raw.githubusercontent.com/neylsoncrepalde/titanic_data_with_semicolon/main/titanic.csv"

default_args = {
    'owner': "Magdiel",
    "depends_on_past": False,
    'start_date': datetime(2022, 10, 12)
}

@dag(default_args=default_args, schedule='@once', catchup=False, tags=['Titanicdag2'])
def trabalho2_dag2():
    @task
    def media_total():
        NOME_TABELA = "/airflow-docker/resultados.csv"
        file = r'C:\airflow-docker\tabela_unica.csv'
        df = pd.read_csv(file, sep=";")
        res1 = df.groupby(['Sex'])['PassengerId', 'Fare', 'SibSp', 'Parch'].mean().reset_index()
        res1.to_csv(NOME_TABELA, index=False, sep=";")

    fim = EmptyOperator(task_id="fim")

    indicador = media_total()


    indicador >> fim

execucao = trabalho2_dag2()