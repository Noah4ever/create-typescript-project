#!/usr/bin/env python3

import os
import subprocess
import json

# Colors
GREEN = '\033[0;32m'
CYAN = '\033[0;36m'
NC = '\033[0m'  # No Color

# Function to check if a command is available


def command_exists(command):
    return subprocess.run([command, '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0

# Function to install a package using apt


def install_package(package):
    if command_exists("sudo"):
        subprocess.run(['sudo', 'apt-get', 'update'],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(['sudo', 'apt-get', 'install', '-y', package],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        print(f"Please install {package} manually to continue.")
        exit(1)


# Check if jq is installed, if not, install it
if not command_exists("jq"):
    print(f"{CYAN}Installing jq...{NC}")
    install_package("jq")

# Check if git is installed, if not, install it
if not command_exists("git"):
    print(f"{CYAN}Installing git...{NC}")
    install_package("git")

# Prompt user for project name
project_name = input(f"{CYAN}Please provide a project name: {NC}")

# Create directory for the project
print(f"\n{CYAN}Creating project directory...{NC}")
os.makedirs(project_name, exist_ok=True)
os.chdir(project_name)

# Initialize npm project
print(f"{CYAN}Initializing npm project...{NC}")
subprocess.run(['npm', 'init', '-y'], stdout=subprocess.DEVNULL,
               stderr=subprocess.DEVNULL)

# Install required dependencies
print(f"{CYAN}Installing dependencies...{NC}")
subprocess.run(['npm', 'i', 'typescript', '@types/node', 'ts-node-dev',
               '--save-dev'], stdout=subprocess.DEVNULL)

# Initialize TypeScript configuration
print(f"{CYAN}Initializing TypeScript configuration...{NC}")
subprocess.run(['npx', 'tsc', '--init', '--rootDir', 'src', '--outDir', 'build', '--esModuleInterop', '--resolveJsonModule', '--lib',
               'es6', '--module', 'commonjs', '--allowJs', 'true', '--noImplicitAny', 'true'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Create source directory
print(f"{CYAN}Creating source directory...{NC}")
os.makedirs('src', exist_ok=True)

# Create a basic TypeScript file
print(f"{CYAN}Creating initial TypeScript file...{NC}")
with open('src/index.ts', 'w') as file:
    file.write("console.log('Hello, TypeScript!');\n")

# Update package.json with start script
print(f"{CYAN}Updating package.json...{NC}")
with open('package.json', 'r') as file:
    data = json.load(file)
    data['scripts']['dev'] = "ts-node-dev --pretty --respawn ./src/index.ts"
with open('package.json', 'w') as file:
    json.dump(data, file, indent=2)

# Replace occurrences of placeholder with project name
print(f"{CYAN}Setting up project name...{NC}")
with open('package.json', 'r') as file:
    contents = file.read()
contents = contents.replace('PROJECT_NAME', project_name)
with open('package.json', 'w') as file:
    file.write(contents)

# Initialize Git repository
print(f"{CYAN}Initializing Git repository...{NC}")
subprocess.run(['git', 'init'], stdout=subprocess.DEVNULL,
               stderr=subprocess.DEVNULL)
with open('.gitignore', 'w') as file:
    file.write('.DS_Store\n')
subprocess.run(['git', 'add', '.'], stdout=subprocess.DEVNULL,
               stderr=subprocess.DEVNULL)
subprocess.run(['git', 'commit', '-m', 'Initial commit'],
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print(f"\n{GREEN}Project setup completed successfully in the directory: {project_name}{NC}")
print("You can now navigate into the project folder and start editing the 'index.ts' file.")
print("Use the following command to navigate into the project folder:")
print(f"    cd {project_name}")
