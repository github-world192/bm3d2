from flask import Flask, request, jsonify, render_template
import os
os.environ["OPENCV_IO_MAX_THREADS"] = "1"  # 讓 OpenCV 只使用一個執行緒
import cv2
import numpy as np
from bm3d import bm3d

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
# 計算 PSNR
def calculate_psnr(original, denoised):
    mse = np.mean((original - denoised) ** 2)
    if mse == 0:  # 完全一致的情況
        return float('inf')
    max_pixel = 1.0  # 影像像素範圍
    psnr = 10 * np.log10((max_pixel ** 2) / mse)
    return psnr

# 加高斯噪聲
def add_gaussian_noise(image, sigma=0.1):
    row, col = image.shape
    mean = 0
    gaussian_noise = np.random.normal(mean, sigma, (row, col))
    noisy_image = np.clip(image + gaussian_noise, 0, 1)  # 讓圖片值不超過範圍
    return noisy_image
print(cv2.getBuildInformation())
# 這是主處理邏輯
@app.route('/process', methods=['POST'])
def process_image():
    # 接收上傳的圖片
    uploaded_file = request.files['image']
    
    # 讀取圖片並轉成灰階圖
    img = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_GRAYSCALE) / 255.0
    
    # 計算原圖（做為比較用）
    original = img

    # 加上高斯噪聲
    noisy_img = add_gaussian_noise(img, sigma=0.1)  # 可以根據需求改變 sigma 參數

    # 執行 BM3D 去噪
    denoised_img = bm3d(noisy_img, sigma_psd=0.1)

    # 計算 PSNR（比較去噪後的圖像與原圖）
    psnr = calculate_psnr(original, denoised_img)

    # 將去噪後的圖片轉為圖檔格式（例如 PNG），準備回傳
    denoised_img = (denoised_img * 255).astype(np.uint8)  # 恢復到 0~255
    _, img_encoded = cv2.imencode('.png', denoised_img)

    # 回傳去噪後的圖片以及 PSNR
    return jsonify({
        'psnr': psnr,
        'denoised_image': img_encoded.tobytes().decode('latin1')  # 轉為 base64 字串
    })

if __name__ == '__main__':
    app.run(debug=False)