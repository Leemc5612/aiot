from setuptools import find_packages, setup

package_name = 'simpleRos'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lmc',
    maintainer_email='leemc5612@naver.com',
    description='simpleRos demo',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "hello = simpleRos.hello:main",
            "hello_class = simpleRos.hello_class:main",
            "hello_sub = simpleRos.hello_sub:main",
            "hello_pub = simpleRos.hello_pub:main",
            "time_pub = simpleRos.time_pub:main"
            ],
    },
)
