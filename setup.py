import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="الخدمات",
    version="0.0.1",
    author="Mohammad Quadri",
    author_email="quadrixm@example.com",
    description="Python service package for qalblang",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qalblang/qalblang-service",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)