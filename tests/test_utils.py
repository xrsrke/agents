from prodgpt.utils import load_yaml


def test_load_yaml():
    config = load_yaml("./configs/default.yaml")

    assert isinstance(config, dict)
    assert isinstance(config["gcloud_storage"]["bucket_name"], str)
