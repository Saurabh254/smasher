from pydantic import BaseModel, constr


class SmsResponse(BaseModel):
    phone: constr(max_length=10, min_length=10)
    otp: constr(max_length=4, min_length=4)
