FROM python

RUN pip install web.py
RUN pip install redis

RUN mkdir app
WORKDIR /app
COPY . /app
CMD bash -c "python src/index.py 0.0.0.0:8888"
EXPOSE 8888