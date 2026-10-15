FROM python:3.13-slim
WORKDIR /app
COPY index.html .
RUN echo "<p>Image construite le $(date)</p>" >> index.html
EXPOSE 9000
CMD ["python", "-m", "http.server", "9000"]
