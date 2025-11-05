FROM python:3.12

# Install dependencies
COPY requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r /requirements.txt

# Start Flask server
COPY api.py /api.py
CMD ["python", "api.py"]
