import sys
import os
from six.moves import urllib

filename2 = sys.argv[3]
filepath2 = os.path.join('/tmp/', 'img7.jpg')
filepath2, _ = urllib.request.urlretrieve(filename2, filepath2)
