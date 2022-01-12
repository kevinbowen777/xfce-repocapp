import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xfce-repocapp-KEVIN-BOWEN",
    version="0.8.5",
    author="Kevin Bowen",
    author_email="kevin.bowen@gmail.com",
    description="Build scripts for managing Xfce repositories",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/kevinbowen/xfce-repocapp",
    project_urls={
        "Bug Tracker": "https://gitlab.com/kevinbowen/xfce-repocapp/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: POSIX :: Linux',
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Version Control',
        'Topic :: Utilities',
    ],
    package_dir={},
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
)
