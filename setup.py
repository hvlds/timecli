import setuptools

setuptools.setup(
    version="0.0.1dev",
    name="timecli",
    author="Hernán Valdés",
    description="Time Tracking CLI App",
    author_email="hfvaldesg@gmail.com",
    url="https://github.com/hfvaldesg/timecli",
    packages=setuptools.find_packages(),
    entry_points = {
        "console_scripts": ["timecli = timecli.timecli:main"]
    },
    install_requires=["sqlalchemy"],
    python_requires=">=3.6",
)