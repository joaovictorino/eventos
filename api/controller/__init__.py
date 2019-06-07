import lib.util
import os

controllersPath = os.path.dirname(__file__)
lib.util.ImportAllFromDir(controllersPath, "api.controller.")

