<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<header>
    <h1>Legal AI for Bankruptcy Cases 🏛️🤖</h1>
</header>

<section>
    <h2>Overview 📜</h2>
    <p>
        The <strong>"Legal AI for Bankruptcy Cases"</strong> project is an advanced AI-driven system designed to assist legal professionals in navigating the complexities of bankruptcy law. This system employs a Retrieval-Augmented Generation (RAG) architecture to deliver precise and contextually relevant information from legal documents.
    </p>
</section>

<section>
    <h2>Components 🛠️</h2>
    <h3>Dependencies</h3>
    <p>The project leverages several libraries and APIs:</p>
    <ul>
        <li><strong>Pinecone</strong> 🌲: Used for high-performance vector search and similarity queries.</li>
        <li><strong>Cohere</strong> ✍️: Provides text generation and ranking functionalities.</li>
        <li><strong>Ollama</strong> 📝: Offers additional text generation capabilities.</li>
        <li><strong>Gemini</strong> ✨: Includes advanced text generation models.</li>
        <li><strong>LangGraph</strong> 🧩: Manages state graphs and message handling for complex workflows.</li>
        <li><strong>xml.etree.ElementTree</strong> 🗂️: Handles XML parsing and manipulation.</li>
    </ul>
    <h3>Key Imports</h3>
    <ul>
        <li><code>Annotated</code> from <code>typing</code>: Provides type annotations for more explicit type hints.</li>
        <li><code>TypedDict</code> from <code>typing_extensions</code>: Used for creating dictionary-like objects with a fixed set of keys.</li>
        <li><code>pinecone_query</code> from <code>pinecone_utils</code>: Handles querying Pinecone for vector search results.</li>
        <li><code>cohere_text_generation</code> and <code>cohere_rerank</code> from <code>cohere_utils</code>: Utilized for generating and ranking text using Cohere's models.</li>
        <li><code>ollama_text_generation</code> from <code>ollama_utils</code>: Facilitates text generation using Ollama's models.</li>
        <li><code>gemini_text_generation</code> from <code>gemini_utils</code>: Provides text generation capabilities with Gemini's models.</li>
        <li><code>StateGraph</code>, <code>START</code>, and <code>END</code> from <code>langgraph.graph</code>: Manages state transitions and workflows within the legal AI system.</li>
        <li><code>add_messages</code> from <code>langgraph.graph.message</code>: Handles message addition and management in the state graph.</li>
        <li><code>ET</code> from <code>xml.etree.ElementTree</code>: Parses and manipulates XML data.</li>
    </ul>
</section>

<section>
    <h2>Functionality ⚙️</h2>
    <h3>AI Components</h3>
    <h4>Text Generation:</h4>
    <ul>
        <li><strong>Cohere</strong> ✍️: Utilizes Cohere's models for generating relevant text based on input data and context.</li>
        <li><strong>Ollama</strong> 📝: Provides additional text generation options for varied scenarios.</li>
        <li><strong>Gemini</strong> ✨: Offers advanced text generation capabilities for complex legal contexts.</li>
    </ul>
    <h4>Text Ranking:</h4>
    <ul>
        <li><strong>Cohere</strong> 🔍: Ranks generated text to ensure the most relevant content is highlighted.</li>
    </ul>
    <h4>Vector Search:</h4>
    <ul>
        <li><strong>Pinecone</strong> 🌲: Allows efficient querying and retrieval of similar vectors based on legal data.</li>
    </ul>
    <h3>State Management</h3>
    <p><strong>LangGraph</strong> 🧩: Manages the state transitions and workflows within the legal AI system. It handles various states of the legal process and manages transitions based on user interactions and system responses.</p>
    <h3>XML Handling</h3>
    <p><strong>xml.etree.ElementTree</strong> 🗂️: Used for parsing and manipulating XML data, which might be necessary for handling legal documents or case files in XML format.</p>
</section>

<section>
    <h2>Usage 🛠️</h2>
    <p>To utilize the components effectively, ensure that all required libraries and dependencies are installed and properly configured. The system is designed to integrate various AI models and handle complex legal workflows, making it a powerful tool for legal professionals dealing with bankruptcy cases.</p>
</section>

<section>
    <h2>License 📜</h2>
    <p>The project is licensed under the <a href="LICENSE">MIT License</a>. See the LICENSE file for more details.</p>
</section>

<section>
    <h2>Contact 📧</h2>
    <p>For any inquiries or support, please contact <a href="mailto:sneh.vora126@gmail.com">sneh.vora126@gmail.com</a>.</p>
</section>

<footer>
    <p>&copy; 2024 Legal AI for Bankruptcy Cases. All rights reserved.</p>
</footer>

</body>
</html>

