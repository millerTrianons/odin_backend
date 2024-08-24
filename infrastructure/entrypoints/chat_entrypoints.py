from presentation.start_run_data import StartRunData
from presentation.chat_message_data import ChatMessageData
from presentation.create_chat_data import CreateChatData
from usecases.chat_usecase import ChatUsecase
from fastapi import APIRouter, Body, Depends, UploadFile
from infrastructure.entrypoints.dependencies import get_chat_usecase

router = APIRouter()

@router.post("/add_message", summary="This is the endpoint where the messages will be added")
async def add_message(
    content: ChatMessageData,
    usecase: ChatUsecase = Depends(get_chat_usecase)
):
    return await usecase.add_message(content)

@router.post("/create_chat", summary="Create a new chat")
async def create_chat(
    content: CreateChatData=Body(...),
    usecase: ChatUsecase = Depends(get_chat_usecase)
):
    return await usecase.create_chat(content.user_site_uuid)

@router.post("/start_run", summary="Start process message")
async def start_run(
    content: StartRunData=Body(...),
    usecase: ChatUsecase = Depends(get_chat_usecase)
):
    return await usecase.start_run(content)

@router.get("/get_status/", summary="This is the endpoint where the messages will be added")
async def get_status(
    run_id: str,
    usecase: ChatUsecase = Depends(get_chat_usecase)
):
    return await usecase.get_status(run_id)


@router.get("/get_response/", summary="This is the endpoint return the response when runnig finish")
async def get_response(
    run_id: str,
    usecase: ChatUsecase = Depends(get_chat_usecase)
):
    return await usecase.get_response(run_id)

@router.put('/cancel_run', summary='cancel a run')
async def cancel_run(
    run_id: str,
    usecase: ChatUsecase = Depends(get_chat_usecase)
):
    return await usecase.cancel_run(run_id)

@router.post('/upload_file', summary='Receive a file')
async def upĺoad_file(
    chat_uuid: str,
    file: UploadFile
):
    return file.headers


@router.get("/get_messages/", summary="This is the endpoint that returns the messages")
async def get_response(
    chat_uuid: str,
    usecase: ChatUsecase = Depends(get_chat_usecase)
):
    return await usecase.get_messages(chat_uuid)


@router.get("/get_last_messages/", summary="This is the endpoint that returns the messages")
async def get_response(
    chat_uuid: str,
    message_uuid: str,
    usecase: ChatUsecase = Depends(get_chat_usecase)
):
    return await usecase.get_last_messages(chat_uuid, message_uuid)

