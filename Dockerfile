FROM apache/airflow:2.7.2-python3.8

RUN mkdir /home/airflow/docker
RUN mkdir /home/airflow/src
RUN mkdir /home/airflow/gcs

RUN python -m pip install --upgrade pip

COPY ./airflow/requirements.txt /home/airflow/docker/requirements.txt
RUN pip3 install -r /home/airflow/docker/requirements.txt
