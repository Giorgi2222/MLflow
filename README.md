## Getting Started

Follow the instructions below to set up the project on your local machine.

### Prerequisites

- Python 3.11 must be installed. You can download it from [here](https://www.python.org/downloads/).

### Creating a Virtual Environment

1. Ensure that Python is installed by running:
   ```bash
   py --version
   
2. Create Virtual Environment:
   ```bash
   py -3.11 -m venv venv

3. Activate the Virtual Environment:
   ```bash
   .\venv\Scripts\activate
4. Once the virtual environment is activated, install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
5. Launch Jupyter notebook and open and follow tracking_quickstart.ipynb
   ```bash
   jupyter notebook
### Deploying the model
#### Once you save the model on MLflow tracking server and download it, you can deploy it.
   ```bash
   mlflow models serve -m ./downloaded_model -p 8000 --no-conda
```
#### You can test the deployed model by running test_deployed.py:
   ```bash
   python test_deployed.py
