FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc curl git sshpass && rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir ansible==9.* flask docker


RUN ansible-galaxy collection install community.docker

WORKDIR /app
COPY app.py /app/app.py
COPY ansible/ /app/ansible/

EXPOSE 5001
CMD ["python", "app.py"]
