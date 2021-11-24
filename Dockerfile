FROM python:3.10-alpine3.14

# Add user (UID 4333, chosen randomly)
RUN addgroup -g 4333 -S spaceapi \
 && adduser -u 4333 -S -G spaceapi spaceapi

# Install system dependencies
RUN apk update && apk add bash dumb-init

# Install project dependencies
COPY requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

# Add code
COPY . /code
WORKDIR /code
RUN chown -R spaceapi:spaceapi  /code/

# Default config
ENV RELAY_INTERVAL_SECONDS=60

# Switch to non-privileged user
USER spaceapi

# Specify entrypoint
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["bash", "entrypoint.sh"]
