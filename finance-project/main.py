from fastapi import FastAPI

app = FastAPI(
    debug=True,
    title="Fintech Portfolio API",
    description="A webserver with a REST API for keeping track of your different financial assets,"
    " stock & crypto, and see/compare their evolution",
    version="0.0.1",
)

if __name__ == "__main__":
    import subprocess
    subprocess.run(["uvicorn", "finance-project.main:app", "--reload"])