import os
import sys
from environs import Env

env = Env()
env.read_env()

NASA_API = env('NASA_API')


print(NASA_API)
