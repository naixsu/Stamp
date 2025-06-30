# FROM node:18-bullseye-slim

# # Install system dependencies
# RUN apt-get update && apt-get install -y \
#     python3 python3-venv python3-pip \
#     x11-xserver-utils libgtk-3-0 libnss3 libxss1 libasound2 \
#     libx11-xcb1 libxcomposite1 libxdamage1 libxtst6 libxcb1 \
#     libxrandr2 libxkbcommon-x11-0 libpangocairo-1.0-0 \
#     libdrm2 libgbm1 libxshmfence1 libglu1-mesa \
#     procps \
#     && rm -rf /var/lib/apt/lists/*

# WORKDIR /app

# # Backend: install with venv
# COPY backend/requirements.txt ./backend/requirements.txt
# RUN python3 -m venv /app/venv \
#     && . /app/venv/bin/activate \
#     && pip install --no-cache-dir -r backend/requirements.txt

# COPY backend/ ./backend/

# # Frontend: dev setup only
# COPY frontend/package*.json ./frontend/
# RUN cd frontend && npm install

# COPY frontend/ ./frontend/

# # Environment
# ENV DISPLAY=:0
# ENV PATH="/app/venv/bin:$PATH"

# # Final dev command
# CMD python3 backend/manage.py runserver 0.0.0.0:8000 & cd frontend && npm run dev


FROM node:18-bullseye-slim

WORKDIR /app

COPY frontend/ ./frontend/

RUN cd frontend && npm install

CMD ["npm", "run", "dev", "--prefix", "frontend"]
