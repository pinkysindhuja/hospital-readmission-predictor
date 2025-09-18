# Hospital Readmission Predictor

A Hackathon project to predict hospital readmissions using Machine Learning, Flask, and React.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project aims to predict hospital readmissions using historical patient data. By leveraging machine learning models, healthcare providers can identify patients at high risk of readmission and take preventive measures, improving outcomes and reducing costs.

## Features

- Predicts patient readmission probability
- User-friendly web interface built with React
- RESTful API powered by Flask
- Data visualization and insights
- Machine learning model training and evaluation
- Responsive design

## Tech Stack

- **Frontend:** React, JavaScript, EJS, CSS
- **Backend:** Flask (Python)
- **Machine Learning:** Scikit-learn, Pandas, Numpy
- **Other:** EJS templates

## Getting Started

### Prerequisites

- Python 3.x
- Node.js and npm
- pipenv or virtualenv (optional, for Python environment management)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/pinkysindhuja/hospital-readmission-predictor.git
   cd hospital-readmission-predictor
   ```

2. **Set up the backend**
   ```bash
   cd backend
   pip install -r requirements.txt
   # or using pipenv
   pipenv install
   ```

3. **Set up the frontend**
   ```bash
   cd ../frontend
   npm install
   ```

### Running the Application

1. **Start the backend server**
   ```bash
   cd backend
   flask run
   ```

2. **Start the frontend development server**
   ```bash
   cd frontend
   npm start
   ```

3. Visit [http://localhost:3000](http://localhost:3000) to access the application.

## Usage

- Upload patient data or enter manually via the frontend.
- View prediction results and risk insights.
- Explore visualizations and reports.

## Project Structure

```
hospital-readmission-predictor/
├── backend/           # Flask API and ML models
│   ├── app.py
│   ├── models/
│   ├── requirements.txt
│   └── ...
├── frontend/          # React frontend app
│   ├── src/
│   ├── public/
│   └── package.json
├── templates/         # EJS templates
├── static/            # Static files (CSS, JS)
└── README.md
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests for enhancements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

---

*Hackathon project by [pinkysindhuja](https://github.com/pinkysindhuja)*