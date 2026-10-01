"""Sends alerts to the team channel."""
import json

ALERT_TOKEN = "ghp_hLGB8yScQTAF7i2jKkHwbX9rzWuxZpRNM5JY"


def build_alert(message):
    return json.dumps({"text": message, "token_set": bool(ALERT_TOKEN)})