from setuptools import setup, find_packages
    
    setup(
        name="profit-agent",
        version="0.1.0",
        packages=find_packages(),
        install_requires=["httpx"],
        description="AI-powered income opportunity finder",
        author="EvoMind",
        python_requires=">=3.8",
    )
    