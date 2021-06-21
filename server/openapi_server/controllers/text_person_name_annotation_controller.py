import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.text_person_name_annotation_request import TextPersonNameAnnotationRequest  # noqa: E501
from openapi_server.models.text_person_name_annotation_response import TextPersonNameAnnotationResponse  # noqa: E501
from openapi_server import util


def create_text_person_name_annotations(text_person_name_annotation_request=None):  # noqa: E501
    """Annotate person names in a clinical note

    Return the person name annotations found in a clinical note # noqa: E501

    :param text_person_name_annotation_request: 
    :type text_person_name_annotation_request: dict | bytes

    :rtype: TextPersonNameAnnotationResponse
    """
    if connexion.request.is_json:
        text_person_name_annotation_request = TextPersonNameAnnotationRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
