from setuptools import setup, find_packages

setup(
    name='your_project_name',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask==2.0.1',
        'requests==2.26.0',
        'numpy==1.21.2',
        # Add more dependencies as needed
    ],
    entry_points={
        'console_scripts': [
            'your_script_name=your_module:main',
        ],
    },
)
