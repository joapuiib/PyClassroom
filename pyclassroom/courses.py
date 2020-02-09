from pydrive.apiattr import ApiAttribute
from pydrive.apiattr import ApiAttributeMixin
from pydrive.apiattr import ApiResource
from pydrive.apiattr import ApiResourceList
from pydrive.auth import LoadAuth

class CourseList(ApiResourceList):
  """Google Classtroom CourseList instance.

  Equivalent to Courses.list() in Classtroom APIs.
  """

  def __init__(self, auth=None, param=None):
    """Create an instance of GoogleDriveFileList."""
    super().__init__(auth=auth, metadata=param)

  @LoadAuth
  def _GetList(self):
    """Overwritten method which actually makes API call to list files.

    :returns: list -- list of pyclassroom.courses.Course
    """

    self.metadata = self.auth.classroom_service.courses().list(**dict(self)).execute(
      http=self.http)

    result = []
    for course_metadata in self.metadata['courses']:
      tmp_file = Course(
          auth=self.auth,
          metadata=course_metadata,
          uploaded=True)
      result.append(tmp_file)
    return result


class Course(ApiAttributeMixin, ApiResource):
  """Google Classroom Course instance.

  Inherits ApiResource which inherits dict.
  Can access and modify metadata like dictionary.
  """
  uploaded = ApiAttribute('uploaded')
  metadata = ApiAttribute('metadata')

  def __init__(self, auth=None, metadata=None, uploaded=False):
    """Create an instance of Course

    :param auth: authorized GoogleAuth instance.
    :type auth: pydrive.auth.GoogleAuth
    :param metadata: file resource to initialize GoogleDriveFile with.
    :type metadata: dict.
    :param uploaded: True if this file is confirmed to be uploaded.
    :type uploaded: bool.
    """
    ApiAttributeMixin.__init__(self)
    ApiResource.__init__(self)
    self.metadata = {}
    self.dirty = {'content': False}
    self.auth = auth
    self.uploaded = uploaded
    if uploaded:
      self.UpdateMetadata(metadata)
    elif metadata:
      self.update(metadata)
    self._ALL_FIELDS = 'updateTime,description,room,enrollmentCode,courseGroupEmail,section,' \
            'guardiansEnabled,creationTime,teacherGroupEmail,courseMaterialSets,calendarId,' \
            'teacherFolder,courseState,ownerId,alternateLink,id,descriptionHeading,name'

  def __getitem__(self, key):
    """Overwrites manner of accessing Course resource.

    If this cxourse instance is not uploaded and id is specified,
    it will try to look for metadata with Course.get().

    :param key: key of dictionary query.
    :type key: str.
    :returns: value of Files resource
    :raises: KeyError, FileNotUploadedError
    """
    try:
      return dict.__getitem__(self, key)
    except KeyError as e:
      if self.uploaded:
        raise KeyError(e)
      if self.get('id'):
        self.FetchMetadata()
        return dict.__getitem__(self, key)
      else:
        raise FileNotUploadedError()
