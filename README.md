# GitOps Workflow Project

![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![Framework](https://img.shields.io/badge/Framework-Flask-green.svg)
![CI/CD](https://img.shields.io/badge/CI/CD-GitHub_Actions-purple.svg)
![Containerization](https://img.shields.io/badge/Container-Docker-blue.svg)

This project demonstrates a complete Git and DevOps workflow, from version control to automated containerization and deployment. It showcases modern software development best practices.

---

##  About The Project

This repository contains a simple Flask web application that has been fully containerized with Docker and is set up for Continuous Integration and Continuous Deployment (CI/CD) using GitHub Actions.

The primary goals achieved in this project are:
-   **Version Control:** Professional Git branching strategy (`main`, `dev`, `feature`).
-   **Containerization:** A production-ready Docker setup using Gunicorn.
-   **Automation:** A CI/CD pipeline that automatically builds and pushes the Docker image to Docker Hub on every new release.

### 🔮 Future Vision

The long-term goal is to evolve this application into a **"DevOps Daily Quote Engine"** that displays a new, insightful quote about software development and operations on every page refresh.

---

## 🛠️ Getting Started

There are two ways to run this project: locally with Python or with Docker (recommended).

### Running with Docker

This is the easiest and most reliable way to run the application, as it works the same on any machine.

1.  **Ensure you have Docker installed.**
2.  **Pull the image from Docker Hub:**
    ```sh
    docker pull kingg123/gitops-workflow:latest
    ```
3.  **Run the container:**
    ```sh
    docker run -p 8080:8080 kingg123/gitops-workflow:latest
    ```
    The application will be available at `http://localhost:8080`.

---

##  workflow Git & CI/CD Workflow

This project follows a modern DevOps workflow to ensure code quality and deployment reliability.

1.  **Branching:** All new work is done on `feature/*` branches, which are branched off `dev`.
2.  **Pull Requests:** Features are merged into `dev` via Pull Requests for review.
3.  **Staging:** The `dev` branch serves as a staging area for integrated features.
4.  **Release:** When ready for a new release, `dev` is merged into `main`.
5.  **Automation:** A new version tag (e.g., `v1.2`) is created on `main`. This tag push automatically triggers the **GitHub Action**.
6.  **CI/CD Pipeline:** The GitHub Action builds a new Docker image, tags it with the release version, and pushes it to Docker Hub, making it ready for deployment.

---

## 🧠 Project Learnings & Troubleshooting

A key part of this project was setting up and debugging the CI/CD pipeline. Here are some of the challenges faced and lessons learned:

-   **Production Server:** The initial Flask development server was upgraded to a production-grade WSGI server (**Gunicorn**) to ensure the Docker container was suitable for real-world use.
-   **GitHub Actions Activation Issue: A significant challenge occurred where the GitHub Actions workflow was not being detected by the system. The "Actions" tab consistently showed "0 workflows" despite the .yml file being present in the correct .github/workflows/ directory on the main branch.

Troubleshooting Steps:

-   We repeatedly verified the file path and YAML syntax.

-   We confirmed that Actions were enabled in the repository settings.

-   We attempted to "unstick" the branch sync by making new commits and pull requests.

-   We even deleted and recreated the workflow file from scratch.

**The Solution: The issue was resolved through manual intervention. By navigating to the "Actions" tab and manually triggering the workflow, we were able to force the system to recognize, validate, and execute the pipeline. This successful manual run created the repository on Docker Hub and confirmed the automation is now correctly set up to run automatically on all future version tags. This was a valuable lesson in how to resolve platform-side synchronization issues.

This troubleshooting process was a valuable, real-world example of how to diagnose and solve issues in a DevOps environment. 

---
