# Set image version and type.
FROM python:3.13-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy project files and set working directory.
WORKDIR /igknite
COPY . /igknite/

# Set proper frontend for Debian and install external dependencies.
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y --no-install-recommends ffmpeg
RUN rm -rf /var/lib/apt/lists/*
RUN uv sync

# Real-time project view.
ENV PYTHONUNBUFFERED 1

# Run.
ENTRYPOINT [ "uv", "run", "igknite", "run" ]
