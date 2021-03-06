from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool
from src.config import DB_URL
from src.database.db import Base
from src.database.objects.announce import Announce  # noqa: F401
from src.database.objects.background import Background  # noqa: F401
from src.database.objects.effect import Effect  # noqa: F401
from src.database.objects.engine import Engine  # noqa: F401
from src.database.objects.favorite import Favorite  # noqa: F401
from src.database.objects.genre import Genre  # noqa: F401
from src.database.objects.level import Level  # noqa: F401
from src.database.objects.like import Like  # noqa: F401
from src.database.objects.log import Log  # noqa: F401
from src.database.objects.particle import Particle  # noqa: F401
from src.database.objects.pickup import Pickup  # noqa: F401
from src.database.objects.skin import Skin  # noqa: F401
from src.database.objects.upload import Upload  # noqa: F401
from src.database.objects.user import User  # noqa: F401
from src.database.objects.vote import Vote  # noqa: F401

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    context.configure(
        url=DB_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = DB_URL
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
