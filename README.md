# 🧠 ALPHA: Alzheimer's Disease Prediction Using Machine Learning

An academic AI project exploring Alzheimer's disease prediction through machine learning, Explainable AI (XAI), and an integrated AI chatbot.

## 📌 About the Project

Alzheimer's disease is a progressive neurological condition that affects memory, thinking, and everyday activities. Identifying patterns associated with the disease is an important area of healthcare research.

**ALPHA** is a machine-learning research project designed to predict Alzheimer's-related outcomes using structured health, lifestyle, and clinical assessment data. The project also explores Explainable AI to improve model interpretability and an AI chatbot to provide an interactive user experience.

The project includes a web-based prediction prototype built with FastAPI.

## ✨ Key Features

- 🧠 **Machine Learning:** Classification of Alzheimer's-related outcomes using trained machine-learning models.
- 📊 **Data Analysis:** Exploratory data analysis, data preprocessing, and investigation of class imbalance.
- 🔍 **Explainable AI (XAI):** Feature importance and SHAP-based interpretability, as described in the project presentation.
- 💬 **AI Chatbot:** A conversational assistant described in the project architecture.
- 🌐 **Web Application:** A FastAPI-based interface for submitting assessment scores and viewing predictions.
- 📈 **Model Evaluation:** Evaluation using metrics such as accuracy, precision, recall, F1-score, and ROC-AUC.

*Note: The uploaded web application code currently implements the basic prediction workflow. The complete XAI and chatbot source code should be included in the repository to make those components reproducible.*

## 🛠️ Technologies Used

- Python
- FastAPI
- NumPy
- scikit-learn
- XGBoost
- Joblib
- Jupyter Notebook
- HTML and CSS

## 🧪 Dataset and Model Development

According to the project presentation, two public Kaggle datasets were combined to create a dataset containing 2,149 samples and 33 features.

The research explores demographic, lifestyle, medical-history, and clinical information.

The uploaded training notebook focuses on five features:

- `MemoryComplaints`
- `BehavioralProblems`
- `ADL`
- `MMSE`
- `FunctionalAssessment`

The notebook also explores data preprocessing, class imbalance handling, and comparison of classification models.

## 🔍 Explainable AI

Explainable AI aims to make machine-learning predictions easier to interpret.

The project presentation describes using feature importance and SHAP to investigate which features influence model predictions.

The goal is to provide more transparency than a prediction label alone.

## 💬 AI Chatbot

The project presentation describes an AI chatbot architecture involving a language model and retrieval-augmented generation (RAG).

The chatbot is intended to provide a conversational interface for user questions. Its model configuration, retrieval sources, and setup instructions should be documented alongside the corresponding source code.

## 📂 Project Structure

The expected application structure is:

```text
Alzheimers-Prediction/
├── README.md
├── main.py
├── requirements.txt
├── form.html
├── model/
│   ├── xgb_alzheimer_model.pkl
│   └── minmax_scaler.pkl
├── notebooks/
│   └── final_project_for_5_feature.ipynb
├── xai/
└── chatbot/
```

The `model/`, `notebooks/`, `xai/`, and `chatbot/` directories must be added as applicable. The structure above is a proposed layout, not a claim that every file is already present.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/MDMusaaddek/Alzheimers-Prediction.git
cd Alzheimers-Prediction
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

Install the packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

The current web application also requires the following packages if they are not already listed:

```bash
pip install jinja2 python-multipart
```

### 4. Add the trained model files

The application expects these files:

```text
model/xgb_alzheimer_model.pkl
model/minmax_scaler.pkl
```

Place the compatible model and scaler files in the `model/` directory before starting the application.

**Important:** The model, scaler, and input features must be compatible. The uploaded notebook and `main.py` currently use different input feature configurations, so this integration should be verified before relying on the predictions.


## 📊 Model Evaluation

The project presentation discusses comparing multiple machine-learning approaches and evaluating their performance using classification metrics.

Reported results should be accompanied by reproducible test-set evaluations before being presented as verified performance claims.

## 🚀 Future Improvements

- Complete integration of prediction, XAI, and chatbot components.
- Ensure consistent model input features and preprocessing.
- Add reproducible evaluation results and visualizations.
- Improve input validation and error handling.
- Add automated tests and deployment instructions.
- Expand documentation of the dataset and model limitations.

## ⚠️ Medical Disclaimer

This project is intended for educational and research purposes only. It is not a clinically validated diagnostic system and must not be used as a substitute for professional medical assessment.

Model predictions may be inaccurate and should not be used to make medical or treatment decisions.

## 👨‍💻 Author

MD Musaaddek

GitHub: [@MDMusaaddek](https://github.com/MDMusaaddek)

📄 License

A license has not yet been specified. Choose an appropriate license before distributing the source code, model files, or other project materials. Check the licenses of any third-party datasets and models before redistributing them.
