import os
import setuptools
import sys

import shuup_setup_utils as utils

TOPDIR = os.path.abspath(os.path.dirname(__file__))
LONG_DESCRIPTION_FILE = os.path.join(TOPDIR, "README.rst")
VERSION_FILE = os.path.join(TOPDIR, "shuup", "_version.py")

VERSION = "3.1.0.post0.dev"
CLASSIFIERS = """
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
License :: Other/Proprietary License
Natural Language :: English
Natural Language :: Chinese (Simplified)
Natural Language :: Finnish
Natural Language :: Japanese
Natural Language :: Portuguese (Brazilian)
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Topic :: Internet :: WWW/HTTP :: Dynamic Content
Topic :: Internet :: WWW/HTTP :: Site Management
Topic :: Office/Business
Topic :: Software Development :: Libraries :: Application Frameworks
Topic :: Software Development :: Libraries :: Python Modules
""".strip().splitlines()

EXCLUDED_PACKAGES = [
    "shuup_tests",
    "shuup_tests.*",
]

utils.add_exclude_patterns(
    [
        "build",
        "doc",
        "var",
        "LC_MESSAGES",
        "local_settings.py",
    ]
)

REQUIRES = [
    "Babel==2.5.3",
    "bleach==3.1.5",
    "django>=1.11,<2.3",
    "django-bootstrap3>=11,<11.1",
    "django-countries>=6.1.2,<6.2",
    "django-enumfields>=2.0.0,<2.1",
    "django-filer>=1.7,<1.8",
    "django-filter>=2.2.0,<2.3",
    "django-jinja==2.5.0",
    "django-mptt==0.9.1",
    "django-parler==2.0.1",
    "django-polymorphic==2.1.2",
    "django-registration-redux==2.7",
    "django-reversion==3.0.5",
    "django-timezone-field==3.1",
    "djangorestframework==3.11",
    "factory-boy==2.7.0",
    "fake-factory>=0.5.0,<0.5.4",
    "Jinja2==2.8.1",
    "jsonfield>=1,<3",
    "keyring>=23",
    "keyrings.alt>=4",
    "lxml>=4,<5",
    "Markdown>=3,<4",
    "openpyxl>=3.0.7,<4",
    "python-dateutil>=2.8",
    "shuup-mirage-field>=2.2.0,<3",
    "toml>=0.10.0,<1",
    "pytz>=2015.4",
    "requests>=2.7,<3",
    "six>=1.9,<2",
    "unicodecsv==0.14.1",
    "xlrd>=1",
]

if __name__ == "__main__":
    if "upload" in sys.argv:
        raise EnvironmentError("Uploading is blacklisted")

    version = utils.get_version(VERSION, TOPDIR, VERSION_FILE)
    utils.write_version_to_file(version, VERSION_FILE)

    with open(LONG_DESCRIPTION_FILE, "r") as f:
        long_description = f.read()

    setuptools.setup(
        name="shuup", 
        version=version,
        description="E-Commerce Website",  
        long_description=long_description,
        long_description_content_type="text/x-rst",
        classifiers=CLASSIFIERS,
        install_requires=REQUIRES,
        python_requires=">=3.6",
        packages=utils.find_packages(exclude=EXCLUDED_PACKAGES),
        include_package_data=True,
        cmdclass=utils.COMMANDS,
    )
