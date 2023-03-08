import setuptools

setuptools.setup(
    name='glhmm',
    version='0.1.1',
    description='Gaussian Linear Hidden Markov Model',
    url='https://github.com/vidaurre/glhmm',
    author='Diego Vidaurre',
    author_email = "dvidaurre@cfin.au.dk",
    install_requires=['scipy','numpy','sklearn','matplotlib','numba'],
    packages=["glhmm"],
    zip_safe=False,
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3"]
    )

