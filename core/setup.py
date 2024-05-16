from setuptools import setup, find_packages

setup(
    name='news_agent',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here.
        # For example: 'requests>=2.25.1',
        'playwright', 
        'torch',
        'transformers',
        'langchain',
        'openai',
        'gradio',
        'python-dotenv',
        'pandas',
        'numpy',
    ],
)