import os
import subprocess

repo_path = "C:/Projecten/Retail-Sales-Predictive-Platform"
os.chdir(repo_path)

# Pull laatste changes
subprocess.run(["git", "pull", "--rebase"])

# Retrain lokaal model (optioneel, of gebruik GitHub artifact)
subprocess.run(["python", "app/ml/retrain_model.py"])

print("Pulled latest changes and retrained model")
