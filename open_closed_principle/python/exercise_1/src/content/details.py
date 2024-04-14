from dataclasses import dataclass

@dataclass
class ContentDetails:
    """
    ContentDetails class is a data class that holds the content details
    for a content transaction.

    Attributes:
    name: str -- The content name. Example: My content
    type: str -- The content type. Example: video
    src: str -- The content source. Example: http://mycontent.com
    """
    name: str
    type: str
    src: str
