from setuptools import setup, find_packages

setup(
    name='qr_code',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'qrcode[pil]',
        'Pillow',
        'opencv-python',
    ],
    entry_points={
        'console_scripts': [
            'qr-encode=qr_code_lib.encoder:generate_qr_code',
            'qr-decode=qr_code_lib.decoder:decode_qr_code',
        ],
    },
    author='Abhilash Sanne',
    author_email='sanne.abhi@gmail.com',
    description='A library for encoding and decoding QR codes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sanneabhilash/qr_code',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
