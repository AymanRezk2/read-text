FROM python:3

WORKDIR /app

# Copy the Python script and text file into the container
COPY app.py paragraphs.txt /app/

# Install nltk and download required data
RUN pip install nltk && \
    python -m nltk.downloader punkt stopwords

# Command to run the Python script
CMD ["python", "app.py"]
