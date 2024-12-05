import yaml

from env import get_home_path


def get_secret_api_key(api_key_name: str) -> str:
    """
    Get secret api key in secret_key.yaml

    value = get_secret_api_key(api_key_name = 'some-key-name')
    value       # 'asd-0dasd-eqwcx'
    """
    secret_key_file_path = "/".join([get_home_path(), "secret_key.yaml"])
    # YAML 파일 읽기
    with open(secret_key_file_path, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

        return data.get("api_keys", {}).get(api_key_name)
