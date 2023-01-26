from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

### Import Router ###
from app.clients.fastapi_task import repeat_every
from app.tasks.ram_observor import get_and_save_ram_ifo
from app.routers import ram_status_router

app = FastAPI(docs_url='/docs/',
              description='Hub APIs')

origins = ['*', ]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"], )


@app.on_event("startup")
@repeat_every(seconds=60)
async def on_startup():
    get_and_save_ram_ifo()

app.include_router(ram_status_router,)
