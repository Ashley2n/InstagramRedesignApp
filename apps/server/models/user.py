import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Sequence, func
from sqlalchemy.dialects.postgresql.base import UUID

from apps.server.core.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String,nullable=False)
    email = Column(String, unique=True, nullable=True)
    password = Column(String, nullable=False)
    profile_images_url = Column(String, nullable=True, default='default_profile_image.png')
    bio = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
