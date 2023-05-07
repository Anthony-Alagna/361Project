# First stage: Copy the code
FROM python:3.9-slim as code-copier
WORKDIR /code
COPY . /code

# Second stage: Build the final container
FROM python:3.9-slim
WORKDIR /code

# Copy the code from the first stage
COPY --from=code-copier /code /code

COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/
COPY ./entrypoint.sh /entrypoint.sh
EXPOSE 8000
ENTRYPOINT ["./entrypoint.sh"]