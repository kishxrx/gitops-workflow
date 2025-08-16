Project Tasks Checklist
Phase 1: Version Control Setup
[x] Repository created on GitHub.

[x] main and dev branches established.

[x] .gitignore file configured.

[x] Initial project structure pushed.

Phase 2: Application & Documentation
[x] Simple Flask application created on a feature branch.

[x] requirements.txt file added.

[x] Detailed README.md written.

[x] All features merged using Pull Requests.

Phase 3: Containerization
[x] Dockerfile created to containerize the application.

[x] Upgraded app to use a production-grade Gunicorn server.

[x] .dockerignore file added to keep the image small and secure.

[x] Docker image successfully built and tested locally.

Phase 4: CI/CD Automation
[x] GitHub Actions workflow created to automate builds.

[x] Workflow configured to trigger on new version tags (e.g., v1.1).

[x] Repository secrets (DOCKERHUB_USERNAME, DOCKERHUB_TOKEN) configured for secure login.

[x] Workflow successfully pushes the tagged Docker image to Docker Hub.

Phase 5: Release
[x] v1.0 tag created for the initial version.

[x] Subsequent version tags (v1.1, etc.) created to trigger the CI/CD pipeline.