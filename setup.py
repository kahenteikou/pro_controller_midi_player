
from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license=f.read()
setup(
    name='pro_controller_midi_player',
    version='0.0.1',
    description='Pro Controller Midi Player',
    author='kokkiemouse',
    author_email='kokkiemouse@gmail.com',
    url='https://github.com/kokkiemouse/pro_controller_midi_player',
    license=license,
    entry_points={
        "console_scripts": [
            "pro_controller_midi_player=procon_midi.pro_midi:main",
        ]
    },
    packages=find_packages()
)