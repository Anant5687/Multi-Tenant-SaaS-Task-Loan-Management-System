from pydantic import BaseModel


class TenantRequest(BaseModel):
    company_name: str 



class TenantResponse(TenantRequest):
    id: str
    pass

    class Config:
        from_attributes: True