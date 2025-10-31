from pydantic import Field,BaseModel,ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
class CourseSchema(BaseModel):
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: FileSchema
    estimatedTime: str
    createdByUser: UserSchema

class CreateCourseResponseSchema(BaseModel):
    course: CourseSchema

class GetCoursesQuerySchema(BaseModel):
    userId: str

class CreateCourseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: str
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    description: str
    estimated_time: str = Field(alias='estimatedTime')
    preview_file_id: str = Field(alias='previewFileId')
    created_by_user_id: str = Field(alias='createdByUserId')

class UpdateCourseRequestSchema(BaseModel):
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None