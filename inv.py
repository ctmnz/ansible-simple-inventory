#!/usr/bin/env python3

import json

output = {
        "_meta": {
            "hostvars": {
                "google.com": {
                    "http_port": 443
                },
                "dir.bg": {
                    "http_port": 443
                }
            }
        },
        "webprod": {
            "hosts": [
                "google.com",
                "dir.bg",
                "yahoo.com",
                "mail.bg",
                "msn.com",
                "sliven.net"
            ]
        }
    }
print(json.dumps(output))
