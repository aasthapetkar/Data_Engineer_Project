import subprocess

def run_git_config(command):
    try:
        result = subprocess.run(
            ["git", "config"] + command.split(),
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"

# Examples:
print(run_git_config("--global user.name 'Your Name'"))
print(run_git_config("--global user.email 'your.email@example.com'"))
print(run_git_config("--list"))
print(run_git_config("user.name"))
