from logger import app_logger
from fact_generator import FactGenerator, FactGeneratorInput, Levels

if __name__ == "__main__":
    # Add your subject and expertise here
    subjects = [
        # Fundamentals
        FactGeneratorInput(
            subject="Operating System",
            level=Levels.INTERMEDIATE,
        ),
        FactGeneratorInput(
            subject="Networking",
            level=Levels.INTERMEDIATE,
        ),
        
        # Job
        FactGeneratorInput(
            subject="System Infrastructure",
            level=Levels.INTERMEDIATE,
        ),
        FactGeneratorInput(
            subject="System Design",
            level=Levels.INTERMEDIATE,
        ),
        FactGeneratorInput(
            subject="Cyber Security",
            level=Levels.INTERMEDIATE,
        ),

        ## Infra/DevOps
        FactGeneratorInput(
            subject="Docker",
            level=Levels.INTERMEDIATE,
        ),
        FactGeneratorInput(
            subject="Kubernets",
            level=Levels.BEGINNER,
        ),

        ## DBs/Cache
        FactGeneratorInput(
            subject="MongoDB",
            level=Levels.INTERMEDIATE,
        ),
        FactGeneratorInput(
            subject="DynamoDB",
            level=Levels.INTERMEDIATE,
        ),
        FactGeneratorInput(
            subject="Postgres",
            level=Levels.INTERMEDIATE,
        ),
        FactGeneratorInput(
            subject="Redis",
            level=Levels.INTERMEDIATE,
        ),
        FactGeneratorInput(
            subject="RabbitMQ",
            level=Levels.INTERMEDIATE,
        ),


        # Languages
        FactGeneratorInput(
            subject="Python",
            level=Levels.PROFESSIONAL,
        ),
        FactGeneratorInput(
            subject="Golang",
            level=Levels.INTERMEDIATE,
        ),
        FactGeneratorInput(
            subject="Javascript",
            level=Levels.BEGINNER,
        ),
        FactGeneratorInput(
            subject="ReactJS",
            level=Levels.BEGINNER,
        ),
    ]

    for subject in subjects[:1]:
        app_logger.info(f"The subject is {subject}")
        fact_generator = FactGenerator(subject)
        fact_generator.get_fact()
