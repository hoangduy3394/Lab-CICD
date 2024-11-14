# Sử dụng Python image chính thức
FROM python:3.12-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Cài đặt các gói yêu cầu
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy mã nguồn
COPY . .

# Expose port
EXPOSE 5000

# Chạy ứng dụng Flask
CMD ["python", "app.py"]
