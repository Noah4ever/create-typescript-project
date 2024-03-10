# How to Use the Create TypeScript Project Script

The "Create TypeScript Project" script is a tool designed to streamline the process of setting up a new TypeScript project with Node.js. This guide will walk you through the steps to use the script effectively.

Prerequisites
Before using the script, make sure you have the following prerequisites installed on your system:

- Python 3.x
- jq
- Node.js
- npm (Node Package Manager)

## Step 1: Download the Script

You may either download and run the script manually, or use the following cURL or Wget command:

```bash
curl -sO https://raw.githubusercontent.com/Noah4ever/create-typescript-project/main/init.py && python3 init.py
```

```bash
wget -qO- https://raw.githubusercontent.com/Noah4ever/create-typescript-project/main/init.py && python3 init.py
```

## Step 2: Follow the Prompts

The script will guide you through the setup process. It will prompt you for the project name and then proceed to set up the project structure, initialize npm, install dependencies, configure TypeScript, create source files, update package.json, and initialize a Git repository.

## Step 3: Start Developing

After the script completes successfully, you can navigate into the newly created project directory and start developing your TypeScript application.

```bash
cd <project-name>
```

You can now edit the index.ts file and any other files in the project to build your TypeScript application.
