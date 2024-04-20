from setuptools import find_packages, setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="yolobytetrackcamera",
    version="0.1",
    description="A tracker package for easy use of YOLOv8-ByteTrack",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="BP",
    author_email="<barnapet00@gmail.com>",
    url="https://github.com/barnapet00/YOLOv8-ByteTrack",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent"
    ],
    install_requires=['opencv-python',
                      'ultralytics'],
    extras_require={
        "dev": ["pytest", "twine"]
    },
    python_requires=">=3.8",
)