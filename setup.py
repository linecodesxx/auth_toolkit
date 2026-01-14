from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="auth-toolkit",
    version="0.1.0",
    author="linecodesx",
    author_email="feyte11@icloud.com",
    description="Flexible authentication toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/linecodexx/auth_toolkit",
    license_files=["LICENSE"],
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "PyJWT>=2.0.0",
        "pwdlib>=1.0.0",
    ],
    extras_require={
        "websocket": ["fastapi>=0.100.0"],
    },
)
