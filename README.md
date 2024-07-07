# 🕵️ Mossad CTF

Welcome to the Mossad CTF challenge repository! 🎉

## 🧐 Overview

This repository contains the challenge details for the Mossad CTF. Participants are required to enter the Mossad website, receive a KEY and IV for AES encryption, and then use these to encrypt an image with AES-CBC. The challenge involves multiple stages, combining cryptographic tasks and investigative skills.

## 🕵️‍♂️ Challenge Details

### 🎯 Objective
- 🔍 Enter the Mossad website and obtain a KEY and IV for AES encryption.
- 🔐 Use the KEY and IV to encrypt a given image with AES-CBC mode.
- 🧩 Successfully navigate through various stages to find the final solution.

### 📝 Steps

#### 🕵️‍♀️ Step 1: Initial Clue
- 📄 **Receive a PDF file** containing a story and clues.
- 🕵️‍♂️ **Clues**:
  - 🌐 DNS query to find a domain name.
  - The story mentions a Mossad agent who forgot his password and provides a username.

#### 🌐 Step 2: DNS Query
- Perform a DNS query on the provided file to extract information.
- 📄 **Example**: Search for DNS-related information within the PDF.

#### 💻 Step 3: Access the Website
- Use the domain name found in the DNS query to access a website.
- Follow the instructions on the website to proceed to the next stage.

#### 🔑 Step 4: Obtain Encryption Keys
- 🔐 **Receive KEY and IV** for AES encryption from the website.
- 🖼️ **Clue**: The website provides an image and instructions to encrypt it using AES-CBC.

#### 🖼️ Step 5: Encrypt the Image
- 📥 **Download the image** provided on the website.
- Encrypt the image using the obtained KEY and IV with AES-CBC.
  - 🛠️ **Example command**: Use `openssl` or Python's cryptography library to perform the encryption.

#### 🧐 Step 6: Analyze Encrypted File
- 📁 **Receive an encrypted file** after uploading the image.
- 🕵️‍♂️ **Clue**: Use tools like hex editors or file type checkers to analyze the file.
  - 🛠️ **Example tool**: [CheckFileType](https://www.checkfiletype.com/).

#### 🔍 Step 7: Identify the File Type
- 📝 Rename the file extension based on the analysis (e.g., to `.jpg`).
- 🕵️‍♀️ **Clue**: The image contains hidden text.

#### 🖼️ Step 8: Extract Hidden Text
- 🔍 **Enlarge the image** to find hidden text.
- Use tools to extract text from the image.
  - 🛠️ **Example tool**: [ImageToText](https://www.imagetotext.info/).

#### 📺 Step 9: YouTube Clue
- The extracted text provides a **YouTube link and a hint** to check comments.
- 🕵️‍♂️ **Analyze YouTube comments** to find additional clues.
  - 🛠️ **Example tool**: [YouTube Comment Reader](https://chromewebstore.google.com/detail/youtube-comment-reader/jbjbjeceipecokoeocnkcfjpanlipamf).

#### 🔍 Step 10: Final Clue
- Search YouTube comments for specific keywords (e.g., `mossad`, `ctf`, `Eli Copter`, etc.).
- 🎯 **Goal**: Find the password hidden by the Mossad agent.

#### 🔑 Step 11: Login
- Use the obtained **username and password** to log in on the website.
  - **Username**: EliCopter
  - **Password**: MossadRules

#### 🎉 Step 12: Complete the CTF
- Successfully logging in completes the challenge.

## 🚀 Getting Started

### 📋 Prerequisites

- Python (version 3.6 or higher)
- pip (Python package installer)

### 🛠️ Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/avishaigonen123/Mossad_CTF.git
    cd Mossad_CTF
    ```

2. Install necessary libraries:
    ```sh
    pip install cryptography
    ```

## 📚 Usage

Follow the steps outlined in the challenge details to progress through each stage. Use the provided scripts and instructions to perform the necessary tasks.

## 📤 Submission

Submit your encrypted image and the script/code you used for the encryption. Ensure your code is well-documented and can be easily understood.

## 📖 Resources

- [Python Cryptography Documentation](https://cryptography.io/en/latest/)
- [AES Encryption Explanation](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

For any questions or issues, please open an issue in this repository or contact [avishaigonen@gmail.com].
