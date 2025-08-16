# GitOps Workflow Project 🚀

![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![Framework](https://img.shields.io/badge/Framework-Flask-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen)

A demonstration of a standard Git and DevOps workflow, created as part of the Elevate Labs Internship. This project serves as a practical example of version control best practices.

---

## ✨ About The Project

This repository contains a simple Flask web application. The primary goal is to practice and showcase a professional version control workflow, including:

-   **Branching Strategy:** Utilizing `main`, `dev`, and `feature` branches.
-   **Pull Requests:** Using PRs for code review and safe merging.
-   **Documentation:** Maintaining clear documentation with proper commit messages and version tags.

### 🔮 Future Vision

The long-term goal is to evolve this simple application into a modern frontend webpage

---

## 🛠️ Getting Started

Follow these steps to get a local copy up and running.

### Prerequisites

-   Python 3.9+
-   `pip` (Python package installer)

### Installation & Running

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/YOUR_USERNAME/gitops-workflow.git](https://github.com/YOUR_USERNAME/gitops-workflow.git)
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd gitops-workflow
    ```
3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```
4.  **Run the application:**
    ```sh
    python app.py
    ```
    The application will be available at `http://127.0.0.1:5000`.

---

##  workflow Git Workflow

This project follows a standard Git branching model to ensure a clean and manageable codebase.

-   **`main`**: This branch contains the production-ready, stable code. All merges into `main` are done from the `dev` branch and result in a new version tag.
-   **`dev`**: This is the primary development branch. All completed feature branches are merged into `dev` for integration testing.
-   **`feature/*`**: All new features or bug fixes are developed on a dedicated `feature` branch (e.g., `feature/add-new-quote-source`). These are merged into `dev` upon completion.

**Future Vision:** To evolve this into a mordern aesthetic website
