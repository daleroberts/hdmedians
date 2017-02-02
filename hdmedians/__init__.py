from .medoid import medoid

try:
    from .geomedian import geomedian, nangeomedian
except ImportError:
    print("Error: package not compiled.")