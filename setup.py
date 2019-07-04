from setuptools import setup, find_packages

setup(name='ost',
      packages=find_packages(),
      include_package_data=True,
      version='0.8.1',
      description='High-level functionality for the inventory, download '
                  'and pre-processing of Sentinel-1 data',
      install_requires=['numpy',
                        'tqdm',
                        'matplotlib',
                        'psycopg2',
                        'requests',
                        'fiona',
                        'shapely',
                        'rtree',
                        'rasterio',
                        'descartes',
                        'pandas',
                        'geopandas',
                        'gdal',
                        'scipy'
                        ],
      url='https://github.com/ESA-PhiLab/OpenSarToolkit',
      author='Andreas Vollrath',
      author_email='andreas.vollrath[at]esa.int',
      license='MIT License',
      keywords=['Sentinel-1', 'ESA', 'SAR', 'Radar',
                'Earth Observation', 'Remote Sensing',
                'Synthetic Aperture Radar'],
      zip_safe=False)
