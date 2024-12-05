import unittest
from unittest.mock import patch, mock_open

from env import get_home_path
from util.io.secret_key_reader import get_secret_api_key


class TestGetSecretApi(unittest.TestCase):
    """
    Test get_secret_api_key func.
    """

    @patch("builtins.open", new_callable=mock_open, read_data="api_keys:\n  test_key: 'secret_value'")
    def test_get_secret_api_key(self, mock_file):
        """
        Test whether the get_secret_api_key func succeeds.
        """
        # Given

        # When
        ### 함수 호출
        result = get_secret_api_key("test_key")

        # Then
        ### 결과 검증
        self.assertEqual(result, "secret_value")
        ### open 함수 호출 검증
        mock_file.assert_called_once_with(get_home_path() + "/" + "secret_key.yaml", "r", encoding="utf-8")
