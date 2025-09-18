Hospital Readmission Prediction
it is an intelligent platform that predicts patient readmission risk using machine learning. It helps hospitals monitor and reduce avoidable readmissions through real-time analytics and risk assessment.

---

## Features

- Live dashboard displaying risk distribution and readmission trends
- Patient-centric risk prediction and history tracking
- Machine learning based prediction API using Python Flask
- Node.js backend with Express and MongoDB
- Interactive charts with Chart.js for data visualization
- Secure patient data management and analytics
---
## Technologies Used
- Node.js, Express.js
- MongoDB (Atlas or local)
- Python, Flask for prediction API
- Axios for API communication
- Chart.js for frontend charts
- Bootstrap 5 for UI styling
### Prerequisites
- Node.js (v14+)
- Python 3.x
- MongoDB instance (local or MongoDB Atlas)
- Git
### Installation
1. Clone the repository:
2. Install Node.js dependencies:
3. Install Python dependencies in the prediction API folder:
4. Setup environment variables:
Create a `.env` file in the root with variables:
---
## Running Locally
You can run both services simultaneously using `concurrently`:
This runs:
- Node.js backend on `http://localhost:3000`
- Flask prediction API on `http://localhost:5000`

