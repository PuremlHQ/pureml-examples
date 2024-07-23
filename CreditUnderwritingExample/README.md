
# SuperAlign 

## Introduction

Introducing SuperAlign, the premier AI Governance software designed to protect and manage all AI initiatives, including generative AI, Large Language Models (LLMs), in-house, third-party vendor, and embedded systems, without compromising on innovation.

## Getting Started

### Prerequisites

- Git
- Python
- Jupyter Notebook
- Necessary credentials for R2 or S3 if using those storage options
- SuperAlign Credentails. [use this create](https://app.superalign.ai/auth/sign-in?redirectUrl=/dashboard)

### Installation Steps

1. **Clone the Example Folder from GitHub:**
   ```bash
   git clone https://github.com/PuremlHQ/pureml-examples.git
   cd CreditUnderwritingExample
   ```

2. **Give Executable Permission for the Script File:**
   For Linux or MacOS:
   ```bash
   chmod +x script_for_local_storage.sh
   chmod +x script_for_r2_storage.sh
   ```

   For Windows, you can run the scripts directly in Git Bash or use a compatible shell like PowerShell for execution:
   ```powershell
   ./script_for_local_storage.sh
   ./script_for_r2_storage.sh
   ```

3. **Run the Appropriate Script File:**
   - For Local Storage:
     ```bash
     ./script_for_local_storage.sh
     ```


   - For R2 Storage:
     ```bash
     ./script_for_r2_storage.sh
     ```



4. **Log In:**
   When prompted, enter your credentials and select the appropriate organization.

5. **Configure Model and Dataset:**
   Edit the configuration to change the model name and dataset name as required.

6. **Run the Jupyter Notebook:**
   Launch Jupyter Notebook and run your notebooks to start using the package.

## Detailed Instructions

### Local Storage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/PuremlHQ/pureml-examples.git
   cd CreditUnderwritingExample
   ```


2. **Set Script Permissions:**
   ```bash
   chmod +x script_for_local_storage.sh
   ```

   For Windows, you can run the script directly:
   ```powershell
   ./script_for_local_storage.sh
   ```

3. **Run the Script:**
   ```bash
   ./script_for_local_storage.sh
   ```


4. **Login and Configuration:**
   Enter your credentials when prompted and select your organization.

5. **Edit Configuration:**
   Open the configuration file and modify the model name and dataset name as required.

6. **Run Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```


### R2 or S3 Storage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/PuremlHQ/pureml-examples.git
   cd CreditUnderwritingExample
   ```


2. **Set Script Permissions:**
   ```bash
   chmod +x script_for_r2_storage.sh
   ```

   For Windows, you can run the scripts directly:
   ```powershell
   ./script_for_r2_storage.sh
   ```

3. **Run the Appropriate Script:**
     ```bash
     ./script_for_r2_storage.sh
     ```


   
4. **Login and Configuration:**
   Enter your credentials when prompted and select your organization.

5. **Edit Configuration:**
   Open the configuration file and modify the model name and dataset name as required.

6. **Run Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```


## Notes

- **For R2 Storage:** In `script_for_r2_storage.sh`, you will be asked to provide the URL path after `https://` when setting the `public_url`.
- **Required in `script_for_r2_storage.sh`:**
  ```bash
  secret_name=""
  access_key_id=""
  access_key_secret=""
  account_id=""
  bucket_name=""
  public_url=""
  ```

- Ensure you have the necessary credentials and permissions for R2 or S3 storage options.
- Modify the scripts as needed to suit your environment and configuration requirements.

## Troubleshooting

- **Permission Issues:** Ensure you have the necessary permissions to execute the script files.
- **Credential Issues:** Verify your credentials are correct and have the necessary access rights.
- **Configuration Errors:** Double-check the configuration file for any typos or incorrect settings.

