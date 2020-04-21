from setuptools import find_packages, setup

setup(
    name='gift_planner',
    version='1.0',
    license='MIT',
    description='Gift organizer',
    author='Mohamed Osman',
    author_email='mohamedtosman@cmail.carleton.ca',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'python-dateutil'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)