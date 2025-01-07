# models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from config.settings import Base

class Security(Base):
    __tablename__ = 'securities'
    id = Column(Integer, primary_key=True)
    secid = Column(String, unique=True, nullable=False)
    shortname = Column(String)
    regnumber = Column(String)
    name = Column(String)
    isin = Column(String)
    is_traded = Column(Boolean)
    emitent_id = Column(Integer)
    emitent_title = Column(String)
    emitent_inn = Column(String)
    emitent_okpo = Column(String)
    gosreg = Column(DateTime)
    type = Column(String)
    group = Column(String)
    primary_boardid = Column(String)
    marketprice_boardid = Column(String)

class Price(Base):
    __tablename__ = 'prices'
    id = Column(Integer, primary_key=True)
    security_id = Column(Integer, ForeignKey('securities.id'))
    price = Column(Float)
    volume = Column(Integer)
    timestamp = Column(DateTime)
    # security = relationship("Security", back_populates="prices"

Security.prices = relationship("Price", order_by=Price.timestamp, back_populates="security")