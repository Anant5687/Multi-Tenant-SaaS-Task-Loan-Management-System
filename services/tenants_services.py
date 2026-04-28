from sqlalchemy.orm import Session
from models.tenants_models import Tenants_Schema
from schemas.tenants_schemas import TenantRequest, TenantResponse
from fastapi import HTTPException

class TenantService:

    @staticmethod
    def create_tenant(data: TenantRequest, db: Session):

        existing_tenant = db.query(Tenants_Schema).filter(Tenants_Schema.company_name == data.company_name).first()

        if existing_tenant:
            raise HTTPException(status_code=400, detail= "Tenant already registered with same name")

        new_tenant = Tenants_Schema(**data.dict())
        tenant_count = db.query(Tenants_Schema).count()
        new_tenant.id = f"TN-{tenant_count + 1}"

        db.add(new_tenant)
        db.commit()
        db.refresh(new_tenant)
        return new_tenant
    
    @staticmethod
    def get_tenants(db: Session):
        return db.query(Tenants_Schema).all()
    
    @staticmethod 
    def get_tenant_by_id(id: str, db: Session):
        is_tenant = db.query(Tenants_Schema).filter(Tenants_Schema.id == id).first()

        if not is_tenant:
            raise HTTPException(status_code=404, detail="No tenant found")

        return is_tenant
    
    @staticmethod
    def update_tenant(data: TenantRequest, db:Session):
        tenant = TenantService.get_tenant_by_id(data.id, db)
        for key, value in data.dict().items():
            setattr(tenant, key, value)

        db.commit()
        db.refresh(tenant)

        return tenant