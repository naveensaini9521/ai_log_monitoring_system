CREATE TABLE IF NOT EXISTS logs (
    id BIGSERIAL PRIMARY KEY,

    timestamp TIMESTAMP NOT NULL,
    level VARCHAR(10),
    message TEXT,

    source VARCHAR(50),        -- linux / windows / container
    service VARCHAR(100),      -- auth-service / payment
    host VARCHAR(100),         -- server name

    raw_log JSONB,             -- original log
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for fast search
CREATE INDEX idx_logs_timestamp ON logs(timestamp);
CREATE INDEX idx_logs_level ON logs(level);
CREATE INDEX idx_logs_service ON logs(service);