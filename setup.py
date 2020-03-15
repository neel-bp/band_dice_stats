from setuptools import setup


setup(
   name='band_dice_stats',
   version='0.1',
   description='simple cli program for finding probability distribution from dnd-style dicestrings inspired by anydice.com',
   author='Neelu',
   author_email='neelu0@protonmail.com',
   packages=['band_dice_stats'],  #same as name
   install_requires=['termgraph>=0.2.1'],  #external packages as dependencies
   url='https://github.com/neelu0/band_dice_stats',
   entry_points={
        "console_scripts": [
            "bandroll=band_dice_stats.__main__",
        ]
    }
)
