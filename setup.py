#Copyright 2025 Hasan Agit Ünal

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.


from setuptools import setup, find_packages

setup(
    name="termelon",
    version="1.9.2",
    description="Terminal game creator tools",
    author="Hasan Agit Ünal",
    license="Apache-2.0",
    packages=find_packages(include=["termelon", "termelon.*"]),
    entry_points={
        "console_scripts": [
            "tgit=termelon.tgit:main",
        ],
    },
    install_requires=["dulwich"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
