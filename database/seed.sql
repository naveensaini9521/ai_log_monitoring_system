INSERT INTO logs (timestamp, level, message, source, service, host, raw_log)
VALUES (
    NOW(),
    'INFO',
    'System started',
    'linux',
    'core-service',
    'server-01',
    '{"msg": "System started"}'
);