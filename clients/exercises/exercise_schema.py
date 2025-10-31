
from pydantic import BaseModel,Field,ConfigDict


class ExerciseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')

class GetExercisesQuerySchema(BaseModel):
    courseId: str

class GetExercisesResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    exercise: ExerciseSchema

class CreateExerciseResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    exercise: ExerciseSchema

class UpdateExerciseResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    exercise: ExerciseSchema

class CreateExerciseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')

class UpdateExerciseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: str
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')