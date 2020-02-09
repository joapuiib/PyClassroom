from pydrive.apiattr import ApiAttributeMixin
from pydrive.auth import LoadAuth

from .courses import CourseList


class GoogleClassroom(ApiAttributeMixin, object):
  """Main Google Classroom class."""

  def __init__(self, auth=None):
    """Create an instance of GoogleDrive.

    :param auth: authorized GoogleAuth instance.
    :type auth: pydrive.auth.GoogleAuth.
    """
    ApiAttributeMixin.__init__(self)
    self.auth = auth

  def ListCourses(self, param=None):
    """Create an instance of GoogleDriveFile with auth of this instance.

    This method would not upload a file to GoogleDrive.

    :param metadata: file resource to initialize GoogleDriveFile with.
    :type metadata: dict.
    :returns: pydrive.files.GoogleDriveFile -- initialized with auth of this instance.
    """
    return CourseList(auth=self.auth, param=param )

#
#def get_courses( query="", student=None, courseStates="ACTIVE" ):
#    '''Returns list of avilable courses'''
#    response_courses = []
#    page_token = None
#
#    while True:
#        response = pygc.service().classroom().courses().list( studentId=student, courseStates=courseStates, pageToken=page_token ).execute()
#        response_courses.extend(response.get('courses', []))
#        page_token = response.get('nextPageToken', None)
#        if not page_token:
#            break
#
#    if query :
#        response_courses = [ c for c in response_courses if query.lower() in c['name'].lower() ]
#    return [ pygc.Course( c ) for c in response_courses ]
#
#def get_course( courseId ) :
#    '''Return a course object corresponding to a courseId
#    
#    @args
#    courseId - Course identifier
#    '''
#    result = pygc.service().classroom().courses().get(id=courseId).execute()
#
#    return result
