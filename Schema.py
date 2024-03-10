from sqlalchemy import Column, Integer, String, Text, DateTime, Decimal, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ProductCategory(Base):
    __tablename__ = 'product_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    desc = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    modified_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    products = relationship('Product', back_populates='category')

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    product_inventory = Column(Text)
    category_id = Column(Integer, ForeignKey('product_category.id'))
    category = relationship('ProductCategory', back_populates='products')
    created_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime)
    price = Column(Decimal(10, 2))
    discount_id = Column(Integer, ForeignKey('discount.id'))
    discount = relationship('Discount')

class ProductInventory(Base):
    __tablename__ = 'product_inventory'
    id = Column(Integer, primary_key = True)
    quality = Column(Integer)
    created_at = Column(DateTime, default = datetime.utcnow)
    modify_at = Column(DateTime)
    deleted_at = Column(DateTime)

class Discount(Base):
    __tablename__ = 'discount'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    desc = Column(Text)
    discount_percent = Column(Decimal(5, 2), nullable=False)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    modified_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime)

# Example of how to create the tables in a database (SQLite in this case)
from sqlalchemy import create_engine

engine = create_engine('')
Base.metadata.create_all(engine)