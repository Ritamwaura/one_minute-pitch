from __future__ import with_statement

import logging
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context



config=context.config



fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')
