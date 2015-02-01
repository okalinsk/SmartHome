import smart_home
import unittest
from mock import patch


class SmartHomeTestCase(unittest.TestCase):
    def setUp(self):
        smart_home.app.config['TESTING'] = True
        self.app = smart_home.app.test_client()

    def tearDown(self):
        pass

    @patch('xbmc.start_music')
    def test_play_music(self, xbmc_music_mock):
        self.app.post('/', data=dict(Action='Music'))
        assert xbmc_music_mock.called

    @patch('arduino.send_power')
    @patch('display.switch_monitor_state')
    def test_open_tv(self, arduino_mock, display_mock):
        self.app.post('/', data=dict(Action='Power'))
        assert arduino_mock.called
        assert display_mock.called


if __name__ == '__main__':
    unittest.main()
