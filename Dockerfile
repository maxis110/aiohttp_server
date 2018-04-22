FROM python:3

RUN pip3 install --upgrade pip
RUN pip3 install virtualenv

COPY . /sendify_server

WORKDIR /sendify_server

RUN pip3 install --no-cache-dir -r requirements.txt

WORKDIR /sendify_server/sendify

EXPOSE 5000
CMD ["python", "main.py"]
