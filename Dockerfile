FROM python:3.8.3
WORKDIR /code
COPY data/requirements.txt .
RUN pip3 -q install pip --upgrade
RUN pip install -r requirements.txt
COPY notebooks/app.py .
COPY data/pipline.pickle .
COPY data/columnNames.pickle .
EXPOSE 5000
CMD ["python", "app.py"]