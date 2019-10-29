from distutils.core import setup

setup(
    version="0.1dev",
    name="timecli",
    author="Hernán Valdés",
    description="Time Tracking CLI App",
    author_email="hfvaldesg@gmail.com",
    packages=["timecli"],
    install_requires=["sqlalchemy"],
)