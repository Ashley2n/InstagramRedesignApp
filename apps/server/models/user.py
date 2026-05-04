import uuid
from datetime import datetime

from pyexpat.errors import messages
from sqlalchemy import Column, Integer, String, DateTime, Sequence, func
from sqlalchemy.dialects.postgresql.base import UUID

from apps.server.core.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    username = Column(String(30),nullable=False, unique=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)

    profile_images_url = Column(String(500), nullable=True, default='default_profile_image.png')
    bio = Column(String(160), nullable=True, default='')
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
