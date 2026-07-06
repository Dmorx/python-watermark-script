# 📸 Image Watermarker Script

A simple, lightweight, and efficient Python script designed to automatically batch-process images and overlay a logo watermark at the bottom-center. This tool is perfect for website administrators, developers, and content managers who need to secure and brand their media quickly.

---

## 🛠️ Features

* **Bulk Processing:** Automatically processes all images inside a designated folder.
* **Smart Positioning:** Places the watermark at the bottom-center with a clean 15px margin from the edge.
* **Auto-Resizing:** Resizes the source logo to a standard $100 \times 100\text{ px}$ to maintain a uniform look.
* **Format Support:** Works seamlessly with `.png`, `.jpg`, and `.jpeg` formats.

---

## 🚀 How to Use

### 1. Installation
First, ensure you have the required libraries installed. You can install them using the `requirements.txt` file:
```bash
pip install -r requirements.txt

2. Setup Directory Structure
Make sure your project folder is organized as follows before running the script:

python-watermark-script/
│
├── input/               # Drop your original images here
│   ├── image1.jpg
│   └── image2.png
│
├── logo.png             # Your transparent watermark logo
├── logo.py              # The main script file
└── requirements.txt     # Dependencies

📌 Note: Create a folder named input in the root directory if it doesn't exist, and place your images there. Your watermark must be named exactly logo.png and placed next to the script.

3. Run the Script
Execute the script using your terminal:

python3 logo.py

4. Get the Output
Once the terminal displays Done!, a new folder named output will be automatically created containing all your watermarked images.

📝 License
This project is open-source and free to use.
