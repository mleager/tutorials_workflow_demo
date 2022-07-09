# tutorials_workflow_demo

Objective:
  Create a GitHub Actions workflow to automate builing and testing a Django app.
  
 Workflow Breakdown:
  1. Create .github/workflows folders
  2. Create a new workflow via Actions tab --> New workflow
  3. Set instructions for the workflow:
      
      - Execute on push or pull requests to main branch, and run manually
      
            (even updating this README.md will execute the workflow) 
      
      - Set runner as ubuntu-latest
      
      - Define the steps of the job:
      
        - name the job 'build-and-test' 
        
                (to easily identify its purpose)  
      
        - Use an action to checkout your repo (makes all folders/files in the repo available)

        - Use another action to install Python 3.9 to the runner (VM)

        - Use ClI commands to upgrade pip and install the Django app's dependencies onto the runner 
        
                (uses the requirements.txt file --> Django, gunicorn, rest_framework, pytest, pytest-django)

        - Use CLI command to run migrations for the Django app

        - Use CLI command to initiate Pytest verbosely 
