FROM python:3.8.3
WORKDIR code/
COPY requirements.txt .
RUN pip3 -q install pip --upgrade
RUN pip install -r requirements.txt
COPY notebooks/app.py .notebooks/
COPY data/pipline.pickle .data/
EXPOSE 5000
CMD ["python", "notebooks/app.py"]