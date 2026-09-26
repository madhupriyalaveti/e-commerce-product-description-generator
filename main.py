import os
from datetime import datetime

import gradio as gr
import matplotlib.pyplot as plt
import requests


class ProductDescriptionGenerator:
    """Generate and analyze e-commerce product descriptions using Groq."""

    def __init__(self):
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        self.groq_api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.generated_descriptions = []

    def generate_product_description(
        self, product_name, category, features
    ):
        """Generate a description for a single product."""

        product_name = product_name.strip()
        category = category.strip()
        features = features.strip()

        if not all([product_name, category, features]):
            return "Error: Please fill in all fields.", None

        if not self.groq_api_key:
            return (
                "Error: GROQ_API_KEY environment variable is not configured.",
                None,
            )

        prompt = (
            "Generate a compelling e-commerce product description "
            "(100-150 words) for:\n\n"
            f"Product Name: {product_name}\n"
            f"Category: {category}\n"
            f"Key Features: {features}\n\n"
            "Description:"
        )

        data = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are an AI assistant that creates "
                        "professional e-commerce product descriptions."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            "max_tokens": 200,
            "temperature": 0.7,
        }

        try:
            response = requests.post(
                self.groq_api_url,
                headers={
                    "Authorization": f"Bearer {self.groq_api_key}",
                    "Content-Type": "application/json",
                },
                json=data,
                timeout=30,
            )

            response.raise_for_status()

            response_data = response.json()
            description = (
                response_data["choices"][0]["message"]["content"].strip()
            )

            self.generated_descriptions.append(
                {
                    "product": product_name,
                    "text": description,
                    "word_count": len(description.split()),
                }
            )

            visualization = self.analyze_description_length()

            return description, visualization

        except requests.exceptions.RequestException as error:
            return (
                f"Error: Unable to connect to the Groq API. {error}",
                None,
            )

        except (KeyError, IndexError, TypeError):
            return (
                "Error: Unexpected response received from the Groq API.",
                None,
            )

    def batch_generate_descriptions(self, product_list):
        """Generate descriptions for multiple products."""

        product_list = product_list.strip()

        if not product_list:
            return "Error: Please enter at least one product.", None

        self.generated_descriptions = []
        results = []

        for product in product_list.splitlines():
            product = product.strip()

            if not product:
                continue

            parts = [part.strip() for part in product.split("|")]

            if len(parts) != 3:
                results.append(
                    f"Error processing '{product}': "
                    "Use the format Name | Category | Features."
                )
                continue

            name, category, features = parts

            if not all([name, category, features]):
                results.append(
                    f"Error processing '{product}': "
                    "All fields are required."
                )
                continue

            description, _ = self.generate_product_description(
                name,
                category,
                features,
            )

            results.append(
                f"Product: {name}\n"
                f"{description}\n"
                f"{'-' * 50}"
            )

        visualization = self.analyze_description_length()

        if not results:
            return "Error: No valid products were provided.", None

        return "\n".join(results), visualization

    def analyze_description_length(self):
        """Create a visualization of generated description word counts."""

        if not self.generated_descriptions:
            return None

        lengths = [
            description["word_count"]
            for description in self.generated_descriptions
        ]

        figure, axis = plt.subplots(figsize=(9, 5))

        axis.hist(
            lengths,
            bins=min(10, max(1, len(set(lengths)))),
            edgecolor="black",
        )

        axis.axvline(
            100,
            linestyle="--",
            label="Minimum Target (100)",
        )

        axis.axvline(
            150,
            linestyle="--",
            label="Maximum Target (150)",
        )

        average_length = sum(lengths) / len(lengths)

        axis.set_title("Product Description Word Count")
        axis.set_xlabel("Word Count")
        axis.set_ylabel("Number of Descriptions")

        axis.text(
            0.95,
            0.95,
            f"Average: {average_length:.1f} words\n"
            f"Descriptions: {len(lengths)}",
            transform=axis.transAxes,
            ha="right",
            va="top",
        )

        axis.legend()
        figure.tight_layout()

        output_path = (
            f"description_length_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        )

        figure.savefig(output_path)
        plt.close(figure)

        return output_path


generator = ProductDescriptionGenerator()


with gr.Blocks(
    title="E-Commerce Product Description Generator"
) as demo:

    gr.Markdown(
        """
        # 🛍️ E-Commerce Product Description Generator

        Generate AI-powered product descriptions using the Groq API.
        """
    )

    with gr.Tab("✨ Single Product"):

        with gr.Row():

            with gr.Column():

                single_name = gr.Textbox(
                    label="Product Name",
                    placeholder="e.g., Wireless Earbuds",
                )

                single_category = gr.Textbox(
                    label="Category",
                    placeholder="e.g., Electronics",
                )

                single_features = gr.Textbox(
                    label="Key Features",
                    placeholder=(
                        "e.g., Noise cancelling, "
                        "20-hour battery, waterproof"
                    ),
                )

                single_button = gr.Button(
                    "Generate Description"
                )

            with gr.Column():

                single_output = gr.Textbox(
                    label="Generated Description",
                    lines=10,
                )

                single_viz = gr.Image(
                    label="Description Length Analysis"
                )

    with gr.Tab("📦 Batch Processing"):

        with gr.Row():

            with gr.Column():

                batch_input = gr.Textbox(
                    label="Product List",
                    placeholder=(
                        "Name | Category | Features\n"
                        "Wireless Earbuds | Electronics | "
                        "Noise cancelling, 20-hour battery\n"
                        "Smart Watch | Wearables | "
                        "Heart rate monitor, waterproof"
                    ),
                    lines=7,
                )

                batch_button = gr.Button(
                    "Generate Batch Descriptions"
                )

            with gr.Column():

                batch_output = gr.Textbox(
                    label="Batch Results",
                    lines=15,
                )

                batch_viz = gr.Image(
                    label="Description Length Analysis"
                )

    single_button.click(
        fn=generator.generate_product_description,
        inputs=[
            single_name,
            single_category,
            single_features,
        ],
        outputs=[
            single_output,
            single_viz,
        ],
    )

    batch_button.click(
        fn=generator.batch_generate_descriptions,
        inputs=batch_input,
        outputs=[
            batch_output,
            batch_viz,
        ],
    )


if __name__ == "__main__":
    demo.launch()
