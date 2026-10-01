def test_config_loads():
    from app import config
    assert hasattr(config, "AWS_ACCESS_KEY_ID")
    assert hasattr(config, "DEBUG")


def test_db_module_loads():
    from app import db
    assert callable(db.get_connection)




    

def test_alerts_work():
    from app import alerts
    assert "hi" in alerts.build_alert("hi")