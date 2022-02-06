from setuptools import setup

with open('README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='svgrasterize.py',
    description="This is very simple python+numpy SVG rasterize.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['.'],
    install_requires=['numpy'],
    url='https://github.com/aslpavel/svgrasterize.py',
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'font_speciment = font_speciment:main',
            'font_transform = font_transform:main',
            'spritify = spritify:main',
            'svgrasterize = svgrasterize:main',
            'ttf2svg = ttf2svg:main',
        ],
    },
)
