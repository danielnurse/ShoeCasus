# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# MongoDB
# -------------------------------------------------------------------------
MONGO_HOST = 'localhost'
MONGO_PORT = 27100
MONGO_DBNAME = 'shoecase'

# -------------------------------------------------------------------------
# Debug Flag
# -------------------------------------------------------------------------
DEBUG = True

# -------------------------------------------------------------------------
# Application HTTP Server
# -------------------------------------------------------------------------
HOST = '0.0.0.0'
PORT = 5000

# -------------------------------------------------------------------------
# Set Server Name if needed
# -------------------------------------------------------------------------
# SERVER_NAME = '%s:%s' % (HOST, PORT)

# -------------------------------------------------------------------------
# Dataset Configuration
# -------------------------------------------------------------------------
ZIENGS_PROVIDER_DATASETS_FILEPATH = './dataset/crawl_ziengs.nl_2016-05-30T23-15-20.jl'
OMODA_PROVIDER_DATASETS_FILEPATH = './dataset/crawl_omoda.nl_2016-05-30T23-14-58.jl'
ZALANDO_PROVIDER_DATASETS_FILEPATH = './dataset/crawl_zalando.nl_2016-05-30T23-14-36.jl'
