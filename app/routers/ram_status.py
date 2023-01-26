from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.clients.database import get_session
from app.queries.ram_status import ram_status_list
from docs.example_responses.ram_status import RAM_STATUS_LIST_SUCCESS_RESPONSE
from app.schemas.ram_status import RamStatusListResponseSchema

ram_status_router = APIRouter(prefix='/ram_status', tags=['ram_status'])


@ram_status_router.get('/',
                       response_model=RamStatusListResponseSchema,
                       responses={
                           200: {
                               'content': {'application/json': {'example': RAM_STATUS_LIST_SUCCESS_RESPONSE}}
                           },
                           500: {}
                       }
                       )
async def list_activities(n: int = 10,
                          db: Session = Depends(get_session)):
    return {'data': ram_status_list(db, n, ), }
