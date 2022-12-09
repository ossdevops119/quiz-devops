FROM python:3-slim 
WORKDIR /app 
COPY . /app 
RUN pip install --root-user-action=ignore --upgrade pip
RUN pip install --root-user-action=ignore --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8081
ENV WORLD "OSS-LAB-Docker"

ENV EMP_ID "0272"	 
ENV NAME "Donchayut"	 
CMD ["python", "app.py"]
