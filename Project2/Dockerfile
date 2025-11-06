FROM python:3.12

# Copy files from VM to container
COPY requirements.txt /requirements.txt
COPY api.py /api.py
COPY best_model.keras /best_model.keras

# Install dependencies
RUN pip3 install --no-cache-dir -r /requirements.txt

# Start Flask server
CMD ["python", "api.py"]
