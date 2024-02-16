#!/bin/bash

# Colors
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Function to check if a command is available
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to install a package using apt
install_package() {
    if command_exists "sudo"; then
        sudo apt-get update
        sudo apt-get install -y "$1" >/dev/null 2>&1
    else
        echo "Please install $1 manually to continue."
        exit 1
    fi
}

# Check if jq is installed, if not, install it
if ! command_exists "jq"; then
    echo "${CYAN}Installing jq...${NC}"
    install_package "jq"
fi

# Check if git is installed, if not, install it
if ! command_exists "git"; then
    echo "${CYAN}Installing git...${NC}"
    install_package "git"
fi

# Check if a project name is provided
if [ -z "$1" ]; then
    echo "${CYAN}Please provide a project name.${NC}"
    exit 1
fi

# Assign project name to a variable
project_name="$1"

# Create directory for the project
echo "${CYAN}Creating project directory...${NC}"
mkdir "$project_name" >/dev/null 2>&1
cd "$project_name" || exit

# Initialize npm project
echo "${CYAN}Initializing npm project...${NC}"
npm init -y >/dev/null 2>&1

# Install required dependencies
echo "${CYAN}Installing dependencies...${NC}"
npm i typescript @types/node ts-node-dev --save-dev 

# Initialize TypeScript configuration
echo "${CYAN}Initializing TypeScript configuration...${NC}"
npx tsc --init --rootDir src --outDir build --esModuleInterop --resolveJsonModule --lib es6 --module commonjs --allowJs true --noImplicitAny true >/dev/null 2>&1

# Create source directory
echo "${CYAN}Creating source directory...${NC}"
mkdir src >/dev/null 2>&1

# Create a basic TypeScript file
echo "${CYAN}Creating initial TypeScript file...${NC}"
echo "console.log('Hello, TypeScript!');" > src/index.ts

# Update package.json with start script
echo "${CYAN}Updating package.json...${NC}"
jq '.scripts += { "dev": "ts-node-dev --pretty --respawn ./src/index.ts" }' package.json > temp.json && mv temp.json package.json

# Replace occurrences of placeholder with project name
echo "${CYAN}Setting up project name...${NC}"
sed -i "s/PROJECT_NAME/$project_name/g" package.json

# Initialize Git repository
echo "${CYAN}Initializing Git repository...${NC}"
git init >/dev/null 2>&1
echo ".DS_Store" > .gitignore # Ignore macOS .DS_Store files
git add .
git commit -m "Initial commit" >/dev/null 2>&1

echo "${GREEN}Project setup completed successfully in the directory: $project_name${NC}"

