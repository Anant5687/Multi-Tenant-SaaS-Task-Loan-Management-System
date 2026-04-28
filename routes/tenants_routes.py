from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from models.tenants_models import Tenants_Schema
from schemas.tenants_schemas import TenantRequest, TenantResponse
from db.conn import get_db
from services.tenants_services import TenantService

router = APIRouter(prefix="/tenants", tags=["Tenants"])

@router.post("/create", response_model=TenantResponse)
def create_tenant(data: TenantRequest, db: Session= Depends(get_db)):
    return TenantService.create_tenant(data, db)

@router.get("/all", response_model=list[TenantResponse])
def get_all_tenants(db:Session=Depends(get_db)):
    return TenantService.get_tenants(db)

@router.get("/tenant/{id}", response_model=TenantResponse)
def get_tenant_by_id(id: str, db:Session=Depends(get_db)):
    return TenantService.get_tenant_by_id(id, db)

@router.put("/tenant/{id}", response_model=TenantResponse)
def update_tenant(id: str, data: TenantResponse, db: Session=Depends(get_db)):
    return TenantService.update_tenant(data, db)