from .base import ContentBase, ContentDetails

class ContentManager:
    def display_content(self, content: ContentBase, details: ContentDetails):
        return content.display(details)
