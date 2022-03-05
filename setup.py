from setuptools import setup
from glob import glob

package_name = 'move_rio'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, glob('launch/*.launch.py'))

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='helios',
    maintainer_email='gagemiller155@gmail.com',
    description='Rio Desc',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = move_rio.talker:main',
            'listener = move_rio.listener:main',
        ],
    },
)
