import lib.util
import os

modelsPath = os.path.dirname(__file__)
lib.util.ImportAllFromDir(modelsPath, "api.model.")

