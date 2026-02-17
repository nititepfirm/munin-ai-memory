from setuptools import setup, find_packages

# Read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="munin-ai",
    version="0.1.0",
    description="An AI Memory Manager that fixes hallucinations via Smart Pruning & Active Forgetting.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/firmiii/munin",  # Placeholder based on user path, likely needs manual update
    author="Your Name",
    author_email="your.email@example.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="ai, memory, llm, chromadb, rag, hallucination-prevention",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "fastapi",
        "uvicorn",
        "chromadb",
        "sentence-transformers",
        "pydantic",
        "streamlit",
    ],
)
