/*Añadir usuarios y registro de logs en la BD*/
CREATE TABLE users(
    id INT GENERATED ALWAYS AS IDENTITY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL,
    status VARCHAR(50),
    PRIMARY KEY(id)
);

CREATE TABLE login_logs(
    id INT GENERATED ALWAYS AS IDENTITY,
    user_id INT NOT NULL,
    attempt_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(50),
    PRIMARY KEY(id),
    CONSTRAINT fk_user
    FOREIGN KEY(user_id) 
    REFERENCES users(id)
    ON DELETE CASCADE
);

CREATE INDEX idx_attempt_date ON login_logs (attempt_date);

INSERT INTO users (username, email, status) 
VALUES (
    'user1',
    'user@mail.com',
    'active'
);

INSERT INTO users (username ,email , status)
VALUES(
    'user2',
    'user2@mail.com',
    'paused'
);

INSERT INTO login_logs (user_id, attempt_date, ip_address)
VALUES(
    1,
    '2026-01-01 00:53:05',
    '192.3.167.8'
);

INSERT INTO login_logs (user_id, attempt_date, ip_address)
VALUES(
    2,
    '2026-01-01 08:42:59',
    '192.2.169.6'
);

INSERT INTO login_logs (user_id, attempt_date, ip_address)
VALUES(
    1,
    '2026-01-01 09:00:05',
    '192.3.167.8'
);

INSERT INTO login_logs (user_id, attempt_date, ip_address)
VALUES(
    1,
    '2026-01-01 12:00:01',
    '192.3.167.8'
);

INSERT INTO login_logs (user_id, attempt_date, ip_address)
VALUES(
    2,
    '2026-01-01 13:02:10',
    '192.2.169.6'
);

SELECT u.username, l.attempt_date FROM users u
INNER JOIN login_logs l 
ON u.id = l.user_id;

/* AI Version

-- 1. Tabla de Usuarios (Entidad Maestra)
CREATE TABLE users (
    id INT GENERATED ALWAYS AS IDENTITY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL,
    status VARCHAR(20) DEFAULT 'active',
    PRIMARY KEY (id),
    -- Restricción para asegurar integridad de datos en el status
    CONSTRAINT chk_status CHECK (status IN ('active', 'blocked', 'paused'))
);

-- 2. Tabla de Logs (Entidad Transaccional)
CREATE TABLE login_logs (
    id INT GENERATED ALWAYS AS IDENTITY,
    user_id INT NOT NULL,
    attempt_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(45), -- VARCHAR(45) cubre IPv6
    is_success BOOLEAN DEFAULT FALSE, -- Para identificar intentos fallidos
    PRIMARY KEY (id),
    -- Aquí es donde vive el CASCADE
    CONSTRAINT fk_user 
        FOREIGN KEY (user_id) 
        REFERENCES users(id) 
        ON DELETE CASCADE
);

-- 3. Índice para rendimiento (Sargability)
-- Según "SQL Performance Explained", los índices en fechas son vitales para reportes.
CREATE INDEX idx_login_attempts_date ON login_logs (attempt_date);

-- 4. Inserción de datos (Omitida por brevedad, los tuyos están bien)

-- 5. Consulta de Auditoría (El JOIN correcto)
-- Proyectamos columnas de ambas tablas
SELECT 
    u.username, 
    l.attempt_date, 
    l.ip_address,
    l.is_success
FROM users u
INNER JOIN login_logs l ON u.id = l.user_id
WHERE l.is_success = FALSE
ORDER BY l.attempt_date DESC; */

