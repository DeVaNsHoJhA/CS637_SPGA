from setuptools import find_packages, setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='spga',
    version='0.0.0',
    description='Self-Preserving Genetic Algorithms for Safe Learning in Discrete Action Spaces',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/pkrobinette/spga',
    author='Preston Robinette',
    author_email='preston.k.robinette@vanderbilt.edu',
    license='',
    python_requires='>=3.7',
    install_requires=[
        'absl-py==1.4.0',
        'aiohttp==3.8.1',
        'aiohttp-cors==0.7.0',
        'aioredis==1.3.1',
        'aiorwlock==1.3.0',
        'aiosignal==1.2.0',
        'anyio==3.5.0',
        'arcade==2.6.13',
        'asgiref==3.5.0',
        'astunparse==1.6.3',
        'async-timeout==4.0.2',
        'attrs==21.4.0',
        'blessed==1.19.1',
        'cachetools==5.0.0',
        'cffi==1.15.0',
        'charset-normalizer==2.0.12',
        'click==8.0.4',
        'cloudpickle==1.6.0',
        'colorful==0.5.4',
        'deprecated==1.2.13',
        'distlib==0.3.6',
        'dm-tree==0.1.6',
        'fastapi==0.74.1',
        'filelock==3.6.0',
        'flatbuffers==23.1.21',
        'fonttools==4.29.1',
        'frozenlist==1.3.0',
        'gast==0.4.0',
        'google-api-core==2.6.0',
        'google-auth==2.6.0',
        'google-auth-oauthlib==0.4.6',
        'google-pasta==0.2.0',
        'googleapis-common-protos==1.55.0',
        'gpustat==1.0.0',
        'gridworld==0.1',
        'grpcio==1.43.0',
        'gym==0.19.0',
        'gym-notices==0.0.4',
        'h11==0.13.0',
        'h5py==3.8.0',
        'hiredis==2.0.0',
        'idna==3.3',
        'imageio==2.16.1',
        'importlib-metadata==4.11.2',
        'jsonschema==4.4.0',
        'keras==2.11.0',
        'kiwisolver==1.3.2',
        'libclang==15.0.6.1',
        'lz4==4.0.0',
        'markdown==3.4.1',
        'markdown-it-py==2.1.0',
        'markupsafe==2.1.2',
        'matplotlib==3.5.1',
        'mdurl==0.1.2',
        'msgpack==1.0.3',
        'multidict==6.0.2',
        'networkx==2.7',
        'numpy==1.22.2',
        'nvidia-ml-py==11.495.46',
        'nvidia-ml-py3==7.352.0',
        'oauthlib==3.2.2',
        'opencensus==0.8.0',
        'opencensus-context==0.1.2',
        'opt-einsum==3.3.0',
        'or-gym==0.5.0',
        'packaging==21.3',
        'pandas==1.4.1',
        'platformdirs==3.0.0',
        'prometheus-client==0.13.1',
        'protobuf==3.19.4',
        'psutil==5.9.0',
        'py-spy==0.3.11',
        'pyasn1==0.4.8',
        'pyasn1-modules==0.2.8',
        'pycparser==2.21',
        'pydantic==1.9.0',
        'pygame==2.1.2',
        'pyglet==2.0a2',
        'pygments==2.14.0',
        'pymunk==6.2.1',
        'pyparsing==3.0.7',
        'pyrsistent==0.18.1',
        'pytiled-parser==2.0.1',
        'pytz==2021.3',
        'pywavelets==1.2.0',
        'pyyaml==6.0',
        'ray==1.12.0',
        'redis==4.1.4',
        'requests==2.27.1',
        'requests-oauthlib==1.3.1',
        'rich==13.3.1',
        'rsa==4.8',
        'scikit-image==0.19.2',
        'scipy==1.8.0',
        'smart-open==5.2.1',
        'sniffio==1.2.0',
        'starlette==0.17.1',
        'tabulate==0.8.9',
        'tensorboard==2.11.2',
        'tensorboard-data-server==0.6.1',
        'tensorboard-plugin-wit==1.8.1',
        'tensorboardx==2.5',
        'tensorflow==2.11.0',
        'tensorflow-estimator==2.11.0',
        'tensorflow-io-gcs-filesystem==0.30.0',
        'termcolor==2.2.0',
        'tifffile==2022.2.9',
        'typer==0.7.0',
        'typing-extensions==4.1.1',
        'urllib3==1.26.8',
        'uvicorn==0.17.5',
        'virtualenv==20.19.0',
        'werkzeug==2.2.2',
        'wrapt==1.13.3',
        'yarl==1.7.2',
        'zipp==3.7.0',
    ],
    packages=find_packages(),

    classifiers=[
        'Programming Language :: Python :: 3.9',
    ],
)