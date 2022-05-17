from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Pedido
from src.infra.sqlalchemy.repository.pedido import RepositoryPedido

router = APIRouter()

@router.post('/pedidos', status_code=status.HTTP_201_CREATED, response_model=Pedido)
def fazer_pedido(pedido: Pedido, session_db: Session = Depends(get_db)):
    pedido = RepositoryPedido(session_db).criar(pedido)
    return pedido

@router.get('/pedidos/{pedido_id}', response_model=Pedido)
def exibir_pedido(pedido_id: int, session_db: Session = Depends(get_db)):
    pass

@router.get('/pedidos', response_model=List[Pedido])
def listar_pedidos(session_db: Session = Depends(get_db)):
    pedidos = RepositoryPedido(session_db).listar()
    return pedidos