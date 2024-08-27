CREATE TABLE eva_prompt ( 
        id INT GENERATED ALWAYS AS IDENTITY,
        content TEXT NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE NOT NULL
);


CREATE TABLE eva_message ( 
        id INT GENERATED ALWAYS AS IDENTITY,
        content TEXT NOT NULL,
        role INT NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE NOT NULL
);