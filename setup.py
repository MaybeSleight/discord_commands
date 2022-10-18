import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="discord_commands",
    version="1.0",
    author="Atidipt123",
    description="A python library for registering discord application commands using python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaybeSleight/discord_commands",
    project_urls={
        "Bug Tracker": "https://github.com/MaybeSleight/discord_commands/issues",
    },
    package_dir={"": "discord_commands"},
    packages=setuptools.find_packages(where="discord_commands"),
    python_requires=">=3.6",
)