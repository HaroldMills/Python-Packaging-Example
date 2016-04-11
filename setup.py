from setuptools import setup


setup(
    name='harold_packaging_example',
    version='0.1.0',
    description='Simple example of Python packaging.',
    url='https://github.com/HaroldMills/Python-Packaging-Example',
    author='Harold Mills',
    author_email='harold.mills@gmail.com',
    license='MIT',
    packages=['harold_packaging_example', 'harold_packaging_example.util'],
    entry_points={
        'console_scripts': [
            'test_script=harold_packaging_example.module:main'
        ]
    },
    include_package_data=True,
    zip_safe=False
)
