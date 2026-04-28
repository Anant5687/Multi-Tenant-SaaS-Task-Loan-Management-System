from pydantic import BaseModel


class TenantRequest(BaseModel):
    id: str
    company_name: str 



class TenantResponse(TenantRequest):
    pass

    class Config:
        from_attributes: True