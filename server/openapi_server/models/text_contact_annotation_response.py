# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.text_contact_annotation import TextContactAnnotation
from openapi_server import util

from openapi_server.models.text_contact_annotation import TextContactAnnotation  # noqa: E501

class TextContactAnnotationResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, text_contact_annotations=None):  # noqa: E501
        """TextContactAnnotationResponse - a model defined in OpenAPI

        :param text_contact_annotations: The text_contact_annotations of this TextContactAnnotationResponse.  # noqa: E501
        :type text_contact_annotations: List[TextContactAnnotation]
        """
        self.openapi_types = {
            'text_contact_annotations': List[TextContactAnnotation]
        }

        self.attribute_map = {
            'text_contact_annotations': 'textContactAnnotations'
        }

        self.text_contact_annotations = text_contact_annotations

    @classmethod
    def from_dict(cls, dikt) -> 'TextContactAnnotationResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TextContactAnnotationResponse of this TextContactAnnotationResponse.  # noqa: E501
        :rtype: TextContactAnnotationResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def text_contact_annotations(self):
        """Gets the text_contact_annotations of this TextContactAnnotationResponse.

        A list of contact annotations  # noqa: E501

        :return: The text_contact_annotations of this TextContactAnnotationResponse.
        :rtype: List[TextContactAnnotation]
        """
        return self._text_contact_annotations

    @text_contact_annotations.setter
    def text_contact_annotations(self, text_contact_annotations):
        """Sets the text_contact_annotations of this TextContactAnnotationResponse.

        A list of contact annotations  # noqa: E501

        :param text_contact_annotations: The text_contact_annotations of this TextContactAnnotationResponse.
        :type text_contact_annotations: List[TextContactAnnotation]
        """
        if text_contact_annotations is None:
            raise ValueError("Invalid value for `text_contact_annotations`, must not be `None`")  # noqa: E501

        self._text_contact_annotations = text_contact_annotations
