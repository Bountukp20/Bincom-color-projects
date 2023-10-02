CREATE TABLE color_frequencies (
    color_name VARCHAR(50),
    frequency FLOAT 
);

INSERT INTO color_frequencies (color_name, frequency) VALUES
    ('green', 10),
    ('yellow', 5),
    ('brown', 6),
    ('blue', 31),
    ('pink', 5),
    ('orange', 9),
    ('cream', 2),
    ('red', 8),
    ('white', 16),
    ('ash', 1),
    ('black', 1),
    ('mean', "(R, G, B): (133, 122, 146)"),
    ('median', "blue"),
    ('mode', 31), -- Blue being the mode
    ('variance', 87.55371900826447),
    ('probability_green', 10.64),
    ('probability_yellow', 5.32),
    ('probability_brown', 6.38),
    ('probability_blue', 32.98),
    ('probability_pink', 5.32),
    ('probability_orange', 9.57),
    ('probability_cream', 2.13),
    ('probability_red', 8.51),
    ('probability_white', 17.02),
    ('probability_ash', 1.06),
    ('probability_black', 1.06)
;
