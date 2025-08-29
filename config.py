import os

class Config:
    # Cấu hình URI cơ sở dữ liệu
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'sqlite:///site.db'
    # Tắt theo dõi sự thay đổi để tiết kiệm tài nguyên
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Cấu hình thêm có thể được thêm vào đây trong tương lai
    # Các thiết lập khác có thể được thêm vào nếu cần thiết
    # Ví dụ: 'DEBUG' có thể được thêm cho môi trường phát triển
    DEBUG = os.getenv('DEBUG', 'False') == 'True'