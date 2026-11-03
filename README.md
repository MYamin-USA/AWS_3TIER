# Enterprise Cloud DevOps Portfolio Portal

An interactive, production-ready Cloud & DevOps portfolio application built with **Python (Streamlit)**, containerized with **Docker**, and architected for scalable cloud deployment on **AWS EC2** with **Amazon RDS** backend integration.

---

## 🚀 Architecture & Tech Stack

* **Frontend & UI:** Python, Streamlit (`aws_python.py`, `inventory_system.py`)
* **Database & Persistence:** Amazon RDS (Relational Database management via `db_manager.py`)
* **Data Integration:** Structured datasets (`inventory_data.csv`) for dynamic metrics and tabular layouts
* **Containerization:** Docker (`Dockerfile` optimized with `python:3.10-slim`, exposing port 8080)
* **Cloud Infrastructure:** AWS EC2 (Ubuntu 22.04 LTS), AWS IAM, Security Groups
* **Networking & Security:** Nginx Reverse Proxy, Let's Encrypt SSL, DuckDNS mapping, environment variable isolation (`python-dotenv`)

---

## 📂 Repository File Structure

```text
├── .github/
│   └── workflows/          # Disabled deployment workflows (archived for security)
├── .dockerignore           # Excludes local secrets, virtual environments, and keys from container build
├── .gitignore              # Protects .env files, SSH keys (.pem), and local caches from Git tracking
├── Dockerfile              # Multi-layered Docker build recipe for containerized execution
├── aws_python.py           # Main Streamlit application entry point and view router
├── db_manager.py           # Database connection utility for relational CRUD operations
├── inventory_data.csv      # CSV dependency for dynamic inventory analytics
├── inventory_system.py     # Core logic module for inventory management
└── requirements.txt        # Python package dependencies


🔒 Security & Best Practices
Decoupled Secrets: Environment variables, database credentials, and access tokens are strictly isolated using .env files and excluded from version control via .gitignore and .dockerignore.

Container Optimization: Built on a lightweight python:3.10-slim base image with build-cache cleanup to minimize vulnerability footprint and image size.

Network Isolation: Runs behind an Nginx reverse proxy routing traffic securely, bypassing default framework ports.

💻 Local Setup & Installation
If you would like to run or test this portfolio application locally on your machine, follow these steps:

Clone the repository:

Bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME
Create and activate a virtual environment:

Bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
Configure your environment variables:
Create a .env file in the root directory and supply your local database credentials and configuration parameters:

Code snippet
DB_HOST=your_database_host
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=your_database_name
Run the Streamlit application:

Bash
streamlit run aws_python.py --server.port=8501
🐳 Running with Docker
To build and run the application inside a Docker container:

Build the Docker image:

Bash
docker build -t cloud-portfolio-app .
Run the container:

Bash
docker run -p 8080:8080 --env-file .env cloud-portfolio-app
Open your browser and navigate to http://localhost:8080.

👤 Author
Yamin

Cloud & DevOps Solutions Architect | Freelance Cloud Engineering Consultant

[LinkedIn Profile](https://www.linkedin.com/in/md-y-55b219123) | [GitHub Profile](https://github.com/MYamin-USA)
