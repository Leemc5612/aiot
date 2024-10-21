from setuptools import find_packages, setup

package_name = 'homework'

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
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "hello_msub = homework.hello_msub:main",
            "hello_mpub = homework.hello_mpub:main"
        ],
    },
)
