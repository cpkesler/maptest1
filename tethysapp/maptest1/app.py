from tethys_sdk.base import TethysAppBase, url_map_maker


class Maptest1(TethysAppBase):
    """
    Tethys app class for maptest1.
    """

    name = 'HAND Flood Map'
    index = 'maptest1:home'
    icon = 'maptest1/images/flood.jpg'
    package = 'maptest1'
    root_url = 'maptest1'
    color = '#00BFFF'
    description = 'Place a brief description of your app here.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='maptest1',
                           controller='maptest1.controllers.home'),
        )

        return url_maps