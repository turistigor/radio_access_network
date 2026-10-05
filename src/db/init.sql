CREATE TABLE IF NOT EXISTS devices (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'inactive',
    last_updated TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_devices_last_updated ON devices(last_updated);
CREATE INDEX IF NOT EXISTS idx_devices_status ON devices(status);

INSERT INTO devices (name, status)
VALUES 
    ('YADRO BTS8100', 'active'),
    ('ИРТЕЯ-1.5', 'active'),
    ('БС GSM-LTE', 'active'),
    ('Huawei BTS3900', 'active'),
    ('Huawei BTS5900', 'active'),
    ('ERS BBU 5216', 'active'),
    ('ERS BBU 6630', 'active'),
    ('Nokia AirScale', 'active'),
    ('Nokia Flexi Multiradio', 'active'),
    ('ZTE ZXSDR BS8900', 'active'),
    ('ZTE ZXSDR BS8912', 'active')
ON CONFLICT (id) DO NOTHING;