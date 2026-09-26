# 🛍️ E-Commerce Product Description Generator

An AI-powered tool that generates engaging product descriptions for e-commerce websites using the **Groq API**.

The application supports both **single-product** and **batch product description generation**, along with a visualization feature for analyzing the word-count distribution of generated descriptions.

## 🚀 Features

### ✨ Single Product Description

Generate a product description by providing:

- Product name
- Product category
- Key product features

The application sends the information to the Groq API and generates an AI-powered product description.

### 📦 Batch Processing

Generate descriptions for multiple products at once.

Use the following format for each product:

```text
Product Name | Category | Key Features
```

Example:

```text
Wireless Headphones | Electronics | Bluetooth, Noise Cancellation, 30-hour battery
Coffee Mug | Kitchen | Ceramic, 350ml, Dishwasher Safe
```

### 📊 Description Length Analysis

Analyze the generated descriptions by visualizing their word-count distribution.

This helps understand the length and consistency of generated product descriptions.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Groq API | AI-powered text generation |
| Gradio | Web-based user interface |
| Requests | HTTP requests to the Groq API |
| Matplotlib | Data visualization |
| Seaborn | Visualization styling |
| Pandas | Data manipulation and analysis |

## 📋 Requirements

- Python 3.9 or later
- A Groq API key
- Internet connection

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

Replace `YOUR-USERNAME` and `YOUR-REPOSITORY` with your GitHub username and repository name.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install requests gradio pandas matplotlib seaborn
```

## 🔑 API Configuration

This project requires a **Groq API key**.

For security, do not hard-code your API key directly into your Python source code.

Instead, store it as an environment variable.

### Windows

```bash
set GROQ_API_KEY=your_api_key_here
```

### macOS/Linux

```bash
export GROQ_API_KEY=your_api_key_here
```

Your application can then access the key from the environment.

> ⚠️ Never commit API keys, passwords, or other secrets to GitHub.

## ▶️ Running the Application

After installing the dependencies and configuring your API key, run the Python application:

```bash
python main.py
```

The Gradio interface will start locally and provide a URL that you can open in your web browser.

## 🧪 Example Workflow

### Single Product

Enter:

```text
Product Name: Wireless Headphones
Category: Electronics
Features: Bluetooth, Noise Cancellation, 30-hour battery
```

The application generates an AI-powered product description.

### Batch Processing

Enter multiple products:

```text
Wireless Headphones | Electronics | Bluetooth, Noise Cancellation, 30-hour battery
Coffee Mug | Kitchen | Ceramic, 350ml, Dishwasher Safe
Running Shoes | Sports | Lightweight, Breathable, Non-slip sole
```

The application processes each product and generates descriptions.

## 📊 Description Analysis

The application calculates the number of words in generated descriptions and provides a visualization of the distribution.

This can be useful for:

- Comparing description lengths
- Identifying unusually short or long descriptions
- Understanding generated content patterns

## 📂 Project Structure

```text
e-commerce-product-description-generator/
│
├── main.py
├── README.md
└── .gitignore
```

> The exact Python filename may differ depending on your project. If your application file has a different name, update the run command and project structure accordingly.

## 🔒 Security

Never expose your Groq API key in:

- Source code
- GitHub repositories
- README files
- Screenshots
- Public configuration files

Use environment variables or a secure secrets-management solution instead.

If an API key is accidentally exposed, revoke it immediately and generate a new one.

## 🔮 Future Improvements

Possible improvements include:

- Add support for multiple AI models
- Add customizable description tone and style
- Add adjustable description length
- Export generated descriptions to CSV or Excel
- Add product image generation
- Add additional analytics
- Add automated tests
- Add a downloadable results feature

## 📄 License

This project is intended for educational and demonstration purposes.
