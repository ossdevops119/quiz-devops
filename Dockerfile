FROM python:3-slim 
WORKDIR /app 
COPY . /app 
RUN pip install --root-user-action=ignore --upgrade pip
RUN pip install --root-user-action=ignore --trusted-host pypi.python.org -r requirements.txt
#### config port to mathc application
EXPOSE XXXX
ENV WORLD "OSS-LAB-Docker"
### Input your ID
ENV EMP_ID "XXXX"
### Input your Name	 
ENV NAME "<< Name Surname >>"	 
CMD ["python", "app.py"]
