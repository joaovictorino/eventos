import lib.util
import os

testPath = os.path.dirname(__file__)
lib.util.ImportAllFromDir(testPath, "tests.")
