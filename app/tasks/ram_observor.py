import psutil

from app.clients.database import get_session
from app.queries.ram_status import ram_status_create
from app.utils.utils import byte_to_megabyte


def get_and_save_ram_ifo():
    ram_info = psutil.virtual_memory()
    db = next(get_session())
    ram_status_create(db,
                      byte_to_megabyte(ram_info.used),
                      byte_to_megabyte(ram_info.free),
                      byte_to_megabyte(ram_info.total))
