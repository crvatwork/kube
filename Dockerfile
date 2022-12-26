FROM python:3.8-buster

# metadata
LABEL version="0.1"
LABEL org.opencontainers.image.source https://github.com/crvatwork/kube

# sets the working directory
WORKDIR /cvapp

# include files
ADD yep.py /cvapp/yep.py
ADD requirements.txt /cvapp/requirements.txt

# setup needed items and pull code
RUN apt-get update
RUN pip3 install -r requirements.txt

# run the app
EXPOSE 5000
# CMD python3 yep.py
ENTRYPOINT [ "python3", "/cvapp/yep.py" ]
