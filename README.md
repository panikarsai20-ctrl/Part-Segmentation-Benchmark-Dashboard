# 🔬 Part Segmentation Benchmark Dashboard

An interactive Streamlit dashboard built to evaluate and compare visual segmentation outputs across different model architectures including **CLIP**, **DINOv3**, **CLIP-SAM**, and **DINOv3-SAM**.

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing.

### 📋 Prerequisites

Make sure you have Python installed on your system (Python 3.8 or higher is recommended). You can verify your version by running:

```bash
python --version
```

🛠️ Installation & Setup
Clone the repository (or navigate to your downloaded project directory):
Run the following command to download the project files.

```ash
git clone [https://github.com/panikarsai20-ctrl/Part-Segmentation-Benchmark-Dashboard.git](https://github.com/panikarsai20-ctrl/Part-Segmentation-Benchmark-Dashboard.git)
```
💡 Note: By default, this creates a folder named Part-Segmentation-Benchmark-Dashboard. If you want the folder to be named my_web_app instead, run this command:

```bash
git clone [https://github.com/panikarsai20-ctrl/Part-Segmentation-Benchmark-Dashboard.git](https://github.com/panikarsai20-ctrl/Part-Segmentation-Benchmark-Dashboard.git) my_web_app
```

```bash
cd Parts-Segmentation-Benchmark-Dashboard
```
(Or cd my_web_app if you used the shortcut name above)
#Optional
Create a virtual environment (Optional but highly recommended):

```bash
python -m venv venv
```
Activate the virtual environment:

Windows:

```bash
.\venv\Scripts\activate
```
Mac/Linux:

```bash
source venv/bin/activate
```
#Continue 

Install the required packages:

```bash
pip install -r requirements.txt
```
🖥️ Running the Web App
To launch the dashboard server, run the following command in your terminal:

```bash
streamlit run app.py
```
Once the server initializes, it will automatically spin up the interface in your default web browser. If it doesn't open automatically, look at your terminal output and copy/paste one of the following URLs:

Local URL: http://localhost:8501 (To view on the machine running the code)

Network URL: http://<your-local-ip>:8501 (To view from another device, like your phone, connected to the same Wi-Fi network)

📂 Project Structure
For the application to dynamically parse the target files correctly, ensure your directory layout exactly matches this structure:

The RNS(Retrieve and Segment ) model was ran on an subset Dataset where we took 7 classes of PasacalVOC2012 Datasets and each class has 15 images ,along with that we created the fine grained classes of those 7 classes.
<img width="1896" height="834" alt="image" src="https://github.com/user-attachments/assets/770143c8-d8a0-4858-9adf-3bdfd3d96511" />
You can see how the predicted segmentation images are looking like ,and compre based on different settings on which RNS was ran on for the Dataset

Plaintext
my_web_app/
│
├── app.py                     # Main Streamlit application script
├── requirements.txt           # Python package dependencies
├── .gitignore                 # Files/folders excluded from version control
└── evaluation_outs/           # Root directory for model output images
    ├── CLIP/
    │   ├── with labels/       # 3-panel layout images
    │   └── without labels/    # 2-panel layout images
    ├── DINOv3/
    │   ├── with labels/
    │   └── without labels/
    ├── CLIP-SAM/
    |    ├── with labels/
    │    └── without labels/
    └── DINOv3-SAM/
        ├── with labels/
        └── without labels/
    
📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
