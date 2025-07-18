import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name ="vpymodule",
    version=0.1,
    author="Vijaya Durga Giduthuri",
    author_email="vijayagiduthuri2@gmail.com",
    description="A Python package for data analysis and visualization using Pandas, NumPy, Matplotlib, and Seaborn.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pandas>=1.0",
        "numpy>=1.18",
        "matplotlib>=3.0",
        "seaborn>=0.10"
    ],
)