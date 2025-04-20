FROM ubuntu:22.04
WORKDIR /Mise-en-production-project 
# Install Python
RUN apt-get -y update && \
    apt-get install -y python3-pip
# Install project dependencies
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN ln -s /usr/bin/python3 /usr/bin/python
EXPOSE 8000
CMD ["uvicorn", "app.api:app",  "--proxy-headers", "--host", "localhost", "--port", "8000"]