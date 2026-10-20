from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base


database_uri = f'postgresql://postgres:ran_password@localhost:5432/ran'
db_engine = create_engine(database_uri, pool_pre_ping=True)

base = automap_base()
base.prepare(autoload_with=db_engine)

DeviceModel = base.classes.devices
