"""Schemas for the dnd_class table and its CRUD operations."""
from typing import List, Optional

from pydantic import BaseModel, Field


class DndClassBase(BaseModel):
    """Schema base for where everything is optional."""

    id: Optional[int] = Field(title="ID", description="Class ID (generated)")
    source_id: Optional[int] = Field(title="Source ID", description="FK - Source ID")
    name: Optional[str] = Field(
        title="Name", description="Name of the class (will be set to lowercase)"
    )
    description: Optional[str] = Field(
        title="Description", description="Class description"
    )
    hit_die: Optional[str] = Field(title="Hit Die", description="In 1d8 format")
    primary_ability: Optional[str] = Field(
        title="Primary Ability", description="Primary ability for the class."
    )
    saving_throw_proficiencies: Optional[str] = Field(
        title="Saving Throw Proficiencies",
        description="Saving threows the class is proficient in.",
    )
    armor_proficiencies: Optional[List[str]] = Field(
        title="Armor Proficiencies",
        description='List of armor tags this class is proficient in. ["armor"] means all armor.',
        default=[],
    )
    shield_proficiencies: Optional[List[str]] = Field(
        title="Shield Proficiencies",
        description='List of shield tags this class is proficient in. ["shield"] means all shields.',
        default=[],
    )
    weapon_proficiencies: Optional[List[str]] = Field(
        title="Shield Proficiencies",
        description='List of weapon tags this class is proficient in. ["weapon"] means all weapons.',
        default=[],
    )


class DndClassCreate(DndClassBase):
    """Schema for creation with required overrides and aditonal fields."""

    id: int = Field(title="ID", description="Class ID (generated)")
    source_id: int = Field(title="Source ID", description="FK - Source ID")
    name: str = Field(
        title="Name", description="Name of the class (will be set to lowercase)"
    )
    description: str = Field(title="Description", description="Class description")
    hit_die: str = Field(title="Hit Die", description="In 1d8 format")
    primary_ability: str = Field(
        title="Primary Ability", description="Primary ability for the class."
    )
    saving_throw_proficiencies: str = Field(
        title="Saving Throw Proficiencies",
        description="Saving threows the class is proficient in.",
    )


class DndClassUpdate(DndClassBase):
    """Schema for updating model with required overrides and aditonal fields."""

    id: int = Field(title="ID", description="Class ID (generated)")


class DndClassResponse(DndClassBase):
    """Schema for transforming ORM Model into a response object."""

    class Config:
        """Pydantic model configuration."""

        orm_mode = True
