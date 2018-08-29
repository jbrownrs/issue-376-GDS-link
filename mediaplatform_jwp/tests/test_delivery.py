from unittest import mock

from django.test import TestCase

from mediaplatform_jwp.jwplatformapi import deliveryapi as jwplatform
from mediaplatform import models as mpmodels


class SourcesTestCase(TestCase):
    fixtures = ['mediaplatform_jwp/tests/fixtures/mediaitems.yaml']

    def setUp(self):
        self.dv_from_key_patcher = (
            mock.patch('mediaplatform_jwp.jwplatformapi.deliveryapi.DeliveryVideo.from_key'))
        self.dv_from_key = self.dv_from_key_patcher.start()
        self.dv_from_key.return_value = jwplatform.DeliveryVideo(DELIVERY_VIDEO_FIXTURE)
        self.addCleanup(self.dv_from_key_patcher.stop)

    def test_no_jwp_item(self):
        """If an item has no associated JWP video, sources list is empty."""
        item = mpmodels.MediaItem.objects.get(id='empty')
        self.assertFalse(hasattr(item, 'jwp'))
        self.assertEqual(item.sources, [])

    def test_wp_item(self):
        """If an item has an associated JWP video, the sources list is returned."""
        item = mpmodels.MediaItem.objects.get(id='existing')
        item.downloadable = True
        item.save()
        self.assertTrue(hasattr(item, 'jwp'))
        source_urls = set(source.url for source in item.sources)
        expected_urls = set(source['file'] for source in DELIVERY_VIDEO_FIXTURE['sources'])
        self.assertEqual(source_urls, expected_urls)


DELIVERY_VIDEO_FIXTURE = {
    'key': 'mock1',
    'title': 'Mock 1',
    'description': 'Description for mock 1',
    'date': 1234567,
    'duration': 54,
    'sms_acl': 'acl:WORLD:',
    'sms_media_id': 'media:1234:',
    'sources': [
        {
            'type': 'video/mp4', 'width': 1920, 'height': 1080,
            'file': 'http://cdn.invalid/vid1.mp4',
        },
        {
            'type': 'video/mp4', 'width': 720, 'height': 406,
            'file': 'http://cdn.invalid/vid2.mp4',
        },
    ],
}
