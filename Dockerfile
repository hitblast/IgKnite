# Set image version and type.
FROM python:3.13

# Copy project files and set working directory.
WORKDIR /igknite
COPY . /igknite/

# Set proper frontend for Debian and install external dependencies.
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y --no-install-recommends ffmpeg uv
RUN uv sync
RUN rm -rf /var/lib/apt/lists/*

# Real-time project view.
ENV PYTHONUNBUFFERED 1

# Run.
CMD [ "igknite", "deploy" ]
