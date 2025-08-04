from contextlib import asynccontextmanager

from fastapi import FastAPI
from pydantic import BaseModel

from main import NLUProcessor, get_processor, process_command

processor: NLUProcessor | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global processor
    processor = await get_processor()
    yield
    processor = None  # type: ignore


class Command(BaseModel):
    command: str


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@app.post("/process_command")
async def classify(command: Command):
    print(f"🔍 Processing command: {command.command}")
    print(f"🔍 Processor: {processor}")
    return await process_command(command=command.command, processor=processor)
